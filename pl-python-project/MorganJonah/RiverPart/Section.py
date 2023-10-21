from typing import List, Optional

from MorganJonah.RiverPart.Boat import Boat
from MorganJonah.RiverPart.RiverPart import RiverPart


class Section(RiverPart):
    PRINT_DEBUG = False

    def __init__(self, length: int, flow: int):
        super().__init__()
        self.length: int = length
        self.flow: int = flow
        self.symbol: str = '〜'
        self.boats: List[Optional[Boat]] = []

        for i in range(self.length):
            self.boats.append(None)

        if self.PRINT_DEBUG:
            print(self.boats)

    def update(self):
        return

    def remove_boat(self, boat: Boat):
        pass

    def is_open(self) -> bool:
        if self.boats[0] is None:
            return True
        return False

    def receive_boat(self, boat: Boat):
        self.boats[0] = boat

    def __str__(self):
        section_str = ''

        for boat in self.boats:
            if boat is None:
                section_str += self.symbol * 3
            else:
                section_str += boat.symbol + (self.symbol * 2)

        return section_str

    def alt_str(self):
        section_str = ''

        for boat in self.boats:
            if boat is None:
                section_str += self.symbol * 3
            else:
                section_str += str(boat.id) + (self.symbol * 2)

        return section_str

