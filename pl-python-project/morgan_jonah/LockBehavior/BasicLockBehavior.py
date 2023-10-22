from morgan_jonah.LockBehavior.LockBehavior import LockBehavior


# GRADING: BASIC_FILL
class BasicLockBehavior(LockBehavior):
    """
    Represents the basic lock behavior in the river simulation.

    Methods:
        handle_lock(self, lock)
            Handles the behavior of the lock, including raising
            and lowering water levels and boat transfers.

    Example:
        basic_behavior = BasicLockBehavior()
    """

    def handle_lock(self, lock):
        """
        Handles the behavior of the lock, including raising
        and lowering water levels and boat transfers.

        Args:
            lock (Lock): The lock to which the behavior is applied.

        Returns:
            None
        """
        if lock.boat is not None and lock.water_level < lock.depth:
            lock.raise_water_level(1)
        if lock.boat is None:
            lock.lower_water_level(1)
        elif lock.water_level == lock.depth and lock.next is None:
            lock.boat = None
        if lock.next is not None and lock.water_level == lock.depth and lock.next.is_open():
            lock.next.receive_boat(lock.boat)
            lock.boat = None
