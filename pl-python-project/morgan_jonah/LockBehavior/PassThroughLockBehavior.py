from morgan_jonah.LockBehavior.LockBehavior import LockBehavior


class PassThroughLockBehavior(LockBehavior):
    def handle_lock(self, lock):
        if lock.next is None:
            lock.boat = None
        if lock.boat is not None and lock.next.is_open():
            lock.next.receive_boat(lock.boat)
            lock.boat = None
