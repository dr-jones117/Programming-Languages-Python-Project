from morgan_jonah.LockBehavior.LockBehavior import LockBehavior


class BasicLockBehavior(LockBehavior):
    def handle_lock(self, lock):
        if lock.boat is not None and lock.water_level < lock.depth:
            lock.raise_water_level(1)
        if lock.boat is None:
            lock.lower_water_level(1)
        elif lock.water_level == lock.depth and lock.next is None:
            lock.boat = None
        if lock.next is not None and lock.water_level == lock.depth and lock.next.is_open():
            lock.next.receive_boat(lock.boat)
            lock.boat = None