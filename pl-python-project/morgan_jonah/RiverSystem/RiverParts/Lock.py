from typing import Optional

from morgan_jonah.LockBehavior.PassThroughLockBehavior import PassThroughLockBehavior
from morgan_jonah.RiverSystem.RiverParts.Boat import Boat
from morgan_jonah.RiverSystem.RiverParts.RiverPart import RiverPart


class Lock(RiverPart):
    """
    Represents a lock in the river simulation.

    Attributes:
        depth (int): The depth of the lock.
        boat (Optional[Boat]): The boat currently inside the lock, if any.
        water_level (int): The current water level inside the lock.
        __lock_behavior (LockBehavior): The behavior of the lock
        (e.g., pass-through, basic, or fast empty).

    Methods:
        __init__(self, depth: int = 0, lock_behavior = None)
            Initializes a Lock instance with the given depth and lock behavior.

        update(self)
            Updates the lock according to its behavior.

        remove_boat(self, boat: Boat)
            Removes a boat from the lock.

        is_open(self) -> bool
            Checks if the lock is open and can receive a boat.

        receive_boat(self, boat: Boat)
            Receives a boat into the lock.

        lower_water_level(self, amount: int)
            Lowers the water level inside the lock.

        raise_water_level(self, amount: int)
            Raises the water level inside the lock.

        __str__(self)
            Returns the string representation of the lock.

        alt_str(self)
            Returns an alternative string representation of the lock,
            useful for debugging.

    Example:
        my_lock = Lock(depth=5, lock_behavior=BasicLockBehavior())
    """

    def __init__(self, depth: int = 0, lock_behavior = None):
        """
        Initialize a Lock instance with the given depth and lock behavior.

        Args:
            depth (int): The depth of the lock. Default is 0.
            lock_behavior (LockBehavior): The behavior of the lock.
            Default is PassThroughLockBehavior.

        Returns:
            None
        """
        super().__init__()
        self.depth: int = depth
        self.boat: Optional[Boat] = None
        self.water_level = 0
        self.__lock_behavior = lock_behavior or PassThroughLockBehavior()

    def update(self):
        """
        Update the lock according to its behavior.

        Args:
            None

        Returns:
            None
        """
        self.__lock_behavior.handle_lock(self)

    def remove_boat(self, boat: Boat):
        """
        Removes a boat from the lock.

        Args:
            boat (Boat): The boat to be removed.

        Returns:
            None
        """
        boat = None

    def is_open(self) -> bool:
        """
        Checks if the lock is open and can receive a boat.

        Args:
            None

        Returns:
            bool: True if the lock is open, False otherwise.
        """
        if self.boat is None and self.water_level == 0:
            return True
        return False

    def receive_boat(self, boat: Boat):
        """
        Receives a boat into the lock.

        Args:
            boat (Boat): The boat to be received.

        Returns:
            None
        """
        self.boat = boat

    def lower_water_level(self, amount: int):
        """
        Lowers the water level inside the lock.

        Args:
            amount (int): The amount by which to lower the water level.

        Returns:
            None
        """
        self.water_level -= amount
        if self.water_level < 0:
            self.water_level = 0

    def raise_water_level(self, amount: int):
        """
        Raises the water level inside the lock.

        Args:
            amount (int): The amount by which to raise the water level.

        Returns:
            None
        """
        self.water_level += amount
        if self.water_level > self.depth:
            self.water_level = self.depth

    def __str__(self):
        """
        Return the string representation of the lock.

        Args:
            None

        Returns:
            str: The string representation of the lock.
        """
        if self.boat is None:
            return f'_X( {self.water_level})_'
        else:
            return f'_{str(self.boat)}( {self.water_level})_'

    def alt_str(self):
        """
        Return an alternative string representation of the lock.

        Args:
            None

        Returns:
            str: The alternative string representation of the lock.
        """
        if self.boat is None:
            return f'.......'
        else:
            return self.boat.get_id() + '.' * (7 - len(self.boat.get_id()))
