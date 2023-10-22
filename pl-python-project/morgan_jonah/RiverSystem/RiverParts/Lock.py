from typing import Optional

from morgan_jonah.LockBehavior.PassThroughLockBehavior import PassThroughLockBehavior
from morgan_jonah.RiverSystem.RiverParts.Boat import Boat
from morgan_jonah.RiverSystem.RiverParts.RiverPart import RiverPart


class Lock(RiverPart):
    def __init__(self, depth: int = 0, lock_behavior = None):
        super().__init__()
        self.depth: int = depth
        self.boat: Optional[Boat] = None
        self.water_level = 0
        self.__lock_behavior = lock_behavior or PassThroughLockBehavior()

    def update(self):
        self.__lock_behavior.handle_lock(self)


    def remove_boat(self, boat: Boat):
        boat = None

    def is_open(self) -> bool:

        if self.boat is None and self.water_level == 0:
            return True
        return False

    def receive_boat(self, boat: Boat):
        self.boat = boat

    def lower_water_level(self, amount: int):
        self.water_level -= amount
        if self.water_level < 0:
            self.water_level = 0

    def raise_water_level(self, amount: int):
        self.water_level += amount
        if self.water_level > self.depth:
            self.water_level = self.depth

    def __str__(self):
        if self.boat is None:
            return f'_X( {self.water_level})_'
        else:
            return f'_{str(self.boat)}( {self.water_level})_'

    def alt_str(self):
        if self.boat is None:
            return f'.......'
        else:
            return self.boat.get_id() + '.' * (7 - len(self.boat.get_id()))



