from abc import ABC, abstractmethod
from typing import Optional

from morgan_jonah.LockBehavior.LockBehavior import PassThroughLockBehavior
from morgan_jonah.RiverPart.Boat import Boat
from morgan_jonah.RiverPart.RiverPart import RiverPart


class Lock(RiverPart):
    def __init__(self, depth: int = 0, lock_behavior = None):
        super().__init__()
        self.__depth: int = depth
        self.boat: Optional[Boat] = None
        self.__water_level = 0
        self.__lock_behavior = lock_behavior or PassThroughLockBehavior()

    def update(self):
        self.__lock_behavior.handle_lock(self)


    def remove_boat(self, boat: Boat):
        boat = None

    def is_open(self) -> bool:
        if self.boat is None:
            return True
        return False

    def receive_boat(self, boat: Boat):
        self.boat = boat

    def __str__(self):
        if self.boat is None:
            return f'_X( {self.__water_level})_'
        else:
            return f'_{str(self.boat)}( {self.__water_level})_'

    def alt_str(self):
        if self.boat is None:
            return f'.......'
        else:
            return self.boat.get_id() + '.' * (7 - len(self.boat.get_id()))



