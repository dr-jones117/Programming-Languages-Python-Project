from abc import abstractmethod, ABC



class LockBehavior(ABC):
    @abstractmethod
    def handle_lock(self, lock):
        pass


class PassThroughLockBehavior(LockBehavior):
    def handle_lock(self, lock):
        if lock.boat is not None and lock.next.is_open():
            lock.next.receive_boat(lock.boat)
            lock.boat = None


class BasicLockBehavior(LockBehavior):
    def handle_lock(self, lock):
        return 1, 1


class FastLockBehavior(LockBehavior):
    def handle_lock(self, lock):
        return 1, 2