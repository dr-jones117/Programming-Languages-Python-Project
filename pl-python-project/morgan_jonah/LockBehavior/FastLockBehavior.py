from morgan_jonah.LockBehavior.LockBehavior import LockBehavior


class FastLockBehavior(LockBehavior):
    def handle_lock(self, lock):
        if lock.boat is not None and lock.water_level < lock.depth:
            lock.raise_water_level(1)
        if lock.boat is None:
            lock.lower_water_level(2)
        if lock.water_level == lock.depth and lock.next is None:
            lock.boat = None
        elif lock.water_level == lock.depth and lock.next.is_open():
            lock.next.receive_boat(lock.boat)
            lock.boat = None