from typing import List, Optional

from MorganJonah.RiverPart.Boat import Boat
from MorganJonah.RiverPart.RiverPart import RiverPart

class ReverseBoatListIterator:
    def __init__(self, boat_list: List[Optional[Boat]]):
        self.boat_list: List[Optional[Boat]] = boat_list
        self.index: int = len(boat_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            current_boat = self.boat_list[self.index]
            self.index -= 1
            return current_boat
        else:
            raise StopIteration

class Section(RiverPart):

    def __init__(self, length: int = 1, flow: int = 1, id: int = 1):
        super().__init__()
        self.length: int = length
        self.flow: int = flow
        self.symbol: str = '〜'
        self.boats: List[Optional[Boat]] = []
        self.id = id

        for i in range(self.length):
            self.boats.append(None)

    def update(self):
        iter = ReverseBoatListIterator(self.boats)
        for boat in iter:
            try:
                if boat is not None:
                    curr_idx = iter.index + 1
                    new_idx = curr_idx + 1
                    boat_is_gone = False
                    for _ in range(boat.boat_behavior.get_update_distance(boat.power, self.flow)):
                        if boat_is_gone:
                            break
                        if new_idx >= len(self.boats) and self.next is None:
                            self.boats[curr_idx] = None
                            boat_is_gone = True
                        elif new_idx >= len(self.boats) and self.next is not None and self.next.is_open():
                            self.next.receive_boat(self.boats[curr_idx])
                            self.boats[curr_idx] = None
                        elif self.boats[new_idx] is None:
                            self.boats[new_idx] = self.boats[curr_idx]
                            self.boats[curr_idx] = None
                        curr_idx = new_idx
                        new_idx += 1
            except:
                continue



    def remove_boat(self, boat: Boat):
        boat = None

    def is_open(self) -> bool:
        if self.boats[0] is None:
            return True
        return False

    def details(self) -> str:
        boat_amount = 0

        for boat in self.boats:
            if boat is not None:
                boat_amount += 1

        return f'Section {self.id}\nBoats: {boat_amount} Flow: {self.flow}'

    def receive_boat(self, boat: Boat):
        self.boats[0] = boat

    def __str__(self):
        section_str = ''

        for boat in self.boats:
            if boat is None:
                section_str += self.symbol * 3
            else:
                section_str += str(boat) + (self.symbol * 2)

        return section_str

    def alt_str(self):
        section_str = ''

        for boat in self.boats:
            if boat is None:
                section_str += self.symbol * 3
            else:
                section_str += boat.get_id() + (self.symbol * (3 - (len(boat.get_id()))))

        return section_str

