from typing import List

from morgan_jonah.RiverSystem.RiverParts.RiverPart import RiverPart


class ReverseRiverPartIterator:
    def __init__(self, river_parts: List[RiverPart]):
        self.river_parts: List[RiverPart] = river_parts
        self.idx = len(river_parts) - 1

    # GRADING: ITER_ALL
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= 0:
            current_part = self.river_parts[self.idx]
            self.idx -= 1
            return current_part
        else:
            raise StopIteration
