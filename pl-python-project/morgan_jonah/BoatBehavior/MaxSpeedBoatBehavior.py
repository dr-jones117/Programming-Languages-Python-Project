# GRADING: MAX_TRAVEL
from morgan_jonah.BoatBehavior.BoatBehavior import BoatBehavior


class MaxSpeedBoatBehavior(BoatBehavior):
    def get_update_distance(self, power: int, flow: int) -> int:
        return max(power - flow, 1)
