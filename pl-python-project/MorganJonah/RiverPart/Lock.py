from typing import Optional

from MorganJonah.RiverPart.Boat import Boat
from MorganJonah.RiverPart.RiverPart import RiverPart


class Lock(RiverPart):
    def __init__(self, depth: int = 0):
        super().__init__()
        self.__depth: int = depth
        self.__boat: Optional[Boat] = None
        self.__water_level = 0

    def update(self):
        if self.__boat is not None and self.next.is_open():
            self.next.receive_boat(self.__boat)
            self.__boat = None

    def remove_boat(self, boat: Boat):
        boat = None

    def is_open(self) -> bool:
        if self.__boat is None:
            return True
        return False

    def receive_boat(self, boat: Boat):
        self.__boat = boat

    def __str__(self):
        if self.__boat is None:
            return f'_X( {self.__water_level})_'
        else:
            return f'_{str(self.__boat)}( {self.__water_level})_'

    def alt_str(self):
        if self.__boat is None:
            return f'.......'
        else:
            return self.__boat.get_id() + '.' * (7 - len(self.__boat.get_id()))
