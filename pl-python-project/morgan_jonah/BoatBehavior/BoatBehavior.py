from abc import ABC, abstractmethod


class BoatBehavior(ABC):
    @abstractmethod
    def get_update_distance(self, power: int, flow: int) -> int:
        pass
