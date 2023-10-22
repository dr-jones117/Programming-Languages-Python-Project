from abc import abstractmethod, ABC
from typing import List, Optional

from morgan_jonah.RiverPart.Boat import Boat


class RiverPart(ABC):
    def __init__(self):
        self.next: Optional[RiverPart] = None

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def is_open(self) -> bool:
        pass

    @abstractmethod
    def remove_boat(self, boat: Boat):
        pass

    @abstractmethod
    def receive_boat(self, boat: Boat):
        pass

    @abstractmethod
    def alt_str(self):
        pass


