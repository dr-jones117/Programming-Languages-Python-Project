from abc import abstractmethod, ABC


class LockBehavior(ABC):
    @abstractmethod
    def handle_lock(self, lock):
        pass
