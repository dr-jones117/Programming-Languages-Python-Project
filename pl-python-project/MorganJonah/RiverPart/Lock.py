from typing import Optional

from MorganJonah.RiverPart.Boat import Boat
from MorganJonah.RiverPart.RiverPart import RiverPart


class Lock(RiverPart):
    def __init__(self, depth: int = 0):
        super().__init__()
        self.depth: int = depth
        self.boat: Optional[Boat] = None

    def update(self):
        return

    def remove_boat(self, boat: Boat):
        self.boat = None

    def is_open(self) -> bool:
        if self.boat is None:
            return False
        return True

    def receive_boat(self, boat: Boat):
        self.boat = boat

    def __str__(self):
        if self.boat is None:
            return f'_X( {self.depth})_'
        else:
            return f'_{self.boat.symbol}( {self.depth})_'

    def alt_str(self):
        if self.boat is None:
            return f'.......'
        else:
            return f'{self.boat.id}.....'
