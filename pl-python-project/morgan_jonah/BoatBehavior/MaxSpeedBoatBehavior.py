from morgan_jonah.BoatBehavior.BoatBehavior import BoatBehavior


# GRADING: MAX_TRAVEL
class MaxSpeedBoatBehavior(BoatBehavior):
    """
    Behavior class for boats that get their speed from the engine power
    and the river flow

    Methods:
        get_update_distance(self, power, flow)
            gets the max possible distance a boat can travel in single
            tick based on the power and flow. minimum is 1

    Example:
        behavior = MaxSpeedBoatBehavior()
        update_distance = behavior.get_update_distance(5, 3)
        print(update_distance)  # Output: 2
    """

    def get_update_distance(self, power: int, flow: int) -> int:
        """
        Calculates the update distance for a boat based on its power and the flow in the river.

        Args:
            power (int): The power of the boat.
            flow (int): The flow of the river.

        Returns:
            int: The update distance calculated based on the boat's power and river flow.
        """
        return max(power - flow, 1)
