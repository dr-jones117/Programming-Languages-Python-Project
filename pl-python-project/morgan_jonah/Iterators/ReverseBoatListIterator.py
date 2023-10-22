from typing import List, Optional

from morgan_jonah.RiverSystem.RiverParts.Boat import Boat


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