from morgan_jonah.BoatBehavior.BoatBehavior import BoatBehavior


# GRADING: MAX_TRAVEL
class MaxSpeedBoatBehavior(BoatBehavior):
    def get_update_distance(self, power: int, flow: int) -> int:
        return max(power - flow, 1)
