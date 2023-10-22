from typing import List, Optional

from morgan_jonah.RiverPart.Boat import Boat
from morgan_jonah.RiverPart.RiverPart import RiverPart

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
            if boat is not None:
                self.update_boat_at_pos(iter.index + 1)


    def update_boat_at_pos(self, start_idx: int):

        actual_start_idx = start_idx
        boat = self.boats[start_idx]
        distance = boat.boat_behavior.get_update_distance(boat.power, self.flow)

        handled_long_distance = False
        for i in range(distance):
            if handled_long_distance:
                break

            offset = start_idx + 1
            if offset >= len(self.boats):
                handled_long_distance = True

                if self.next is not None and self.next.is_open() and actual_start_idx == len(self.boats) - 1:
                    self.next.receive_boat(self.boats[start_idx])
                    self.boats[start_idx] = None
                elif self.next is None and actual_start_idx == start_idx:
                    self.boats[start_idx] = None
                else:
                    return

            elif self.boats[offset] is None:
                self.boats[offset] = self.boats[start_idx]
                self.boats[start_idx] = None
            elif self.boats[offset] is not None:
                return

            start_idx = offset

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

