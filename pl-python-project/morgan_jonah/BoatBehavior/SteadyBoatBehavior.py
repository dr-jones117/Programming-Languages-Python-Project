from morgan_jonah.BoatBehavior.BoatBehavior import BoatBehavior


# GRADING: STEADY_TRAVEL
class SteadyBoatBehavior(BoatBehavior):
    """
    Behavior class for boats that goes a consistent speed of one.

    Methods:
        get_update_distance(self, power, flow)
            Calculates the update distance for a boat, which is always 1.

    Example:
        behavior = SteadyBoatBehavior()
        update_distance = behavior.get_update_distance(5, 3)
        print(update_distance)  # Output: 1
    """

    def get_update_distance(self, power: int, flow: int) -> int:
        """
        Calculates the update distance for a boat, which is always 1.

        Args:
            power (int): The power of the boat.
            flow (int): The flow of the river.

        Returns:
            int: The fixed update distance, which is always 1.
        """
        return 1
