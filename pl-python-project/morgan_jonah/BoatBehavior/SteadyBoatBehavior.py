from morgan_jonah.BoatBehavior.BoatBehavior import BoatBehavior


# GRADING: STEADY_TRAVEL
class SteadyBoatBehavior(BoatBehavior):
    def get_update_distance(self, power: int, flow: int) -> int:
        return 1