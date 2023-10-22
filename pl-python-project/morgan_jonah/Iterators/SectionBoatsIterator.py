from typing import List, Optional

from morgan_jonah.RiverSystem.RiverParts.Boat import Boat


class SectionBoatsIterator:
    def __init__(self, boats: List[Optional[Boat]]):
        self.boats = boats
        self.idx = 0
        self.length = len(self.boats)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.length:
            value = self.boats[self.idx]
            self.idx += 1
            return value
        else:
            raise StopIteration