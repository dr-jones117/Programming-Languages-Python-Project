from typing import List

from morgan_jonah.RiverSystem.RiverParts.RiverPart import RiverPart


class RiverPartIterator:
    def __init__(self, river_parts: List[RiverPart]):
        self.river_parts: List[RiverPart] = river_parts
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.river_parts):
            current_part = self.river_parts[self.idx]
            self.idx += 1
            return current_part
        else:
            raise StopIteration


