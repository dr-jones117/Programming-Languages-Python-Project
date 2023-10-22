from abc import ABC, abstractmethod


class BoatBehavior(ABC):
    @abstractmethod
    def get_update_distance(self, power: int, flow: int) -> int:
        pass


# GRADING: STEADY_TRAVEL
class SteadyBoatBehavior(BoatBehavior):
    def get_update_distance(self, power: int, flow: int) -> int:
        return 1


# GRADING: MAX_TRAVEL
class MaxSpeedBoatBehavior(BoatBehavior):
    def get_update_distance(self, power: int, flow: int) -> int:
        return max(power - flow, 1)
