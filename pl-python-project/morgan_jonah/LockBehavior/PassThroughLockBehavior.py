from morgan_jonah.LockBehavior.LockBehavior import LockBehavior


class PassThroughLockBehavior(LockBehavior):
    """
    Represents the pass-through lock behavior in the river simulation.

    Methods:
        handle_lock(self, lock)
            Handles the behavior of the pass-through lock,
            transferring boats to the next section when open.

    Example:
        passthrough_behavior = PassThroughLockBehavior()
    """

    def handle_lock(self, lock):
        """
        Handles the behavior of the pass-through lock,
        transferring boats to the next section when open.

        Args:
            lock (Lock): The lock to which the behavior is applied.

        Returns:
            None
        """
        if lock.next is None:
            lock.boat = None
        if lock.boat is not None and lock.next.is_open():
            lock.next.receive_boat(lock.boat)
            lock.boat = None

