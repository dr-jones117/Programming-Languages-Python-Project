from morgan_jonah.BoatBehavior.BoatBehavior import BoatBehavior
from morgan_jonah.BoatBehavior.SteadyBoatBehavior import SteadyBoatBehavior


class Boat:
    """
    Represents a boat in the river simulation.

    Attributes:
        boat_behavior (BoatBehavior): The behavior of the boat (e.g., steady or max speed).
        __id (int): The unique identifier for the boat.
        power (int): The engine power of the boat.
        __symbol (str): The symbol representing the boat in the river.

    Methods:
        __init__(self, id: int, power: int = 1, boat_behavior: BoatBehavior = SteadyBoatBehavior())
            Initializes a Boat instance with the given ID, engine power, and behavior.

        __str__(self)
            Returns the string representation of the boat.

        get_id(self)
            Returns the unique ID of the boat.

    Example:
        my_boat = Boat(1, power=3, boat_behavior=MaxSpeedBoatBehavior())
    """

    def __init__(self, id: int, power: int = 1, boat_behavior: BoatBehavior = SteadyBoatBehavior()):
        """
        Initialize a Boat instance with the given ID, engine power, and behavior.

        Args:
            id (int): The unique identifier for the boat.
            power (int): The engine power of the boat. Default is 1.
            boat_behavior (BoatBehavior): The behavior of the boat.
            Default is SteadyBoatBehavior.

        Returns:
            None
        """
        self.boat_behavior = boat_behavior
        self.__id: int = id
        self.power: int = power
        self.__symbol: str = '⛴'

    def __str__(self):
        """
        Return the string representation of the boat.

        Args:
            None

        Returns:
            str: The string representation of the boat.
        """
        return self.__symbol

    def get_id(self):
        """
        Return the unique ID of the boat.

        Args:
            None

        Returns:
            str: The unique identifier of the boat.
        """
        return str(self.__id)
