from typing import List, Optional

from morgan_jonah.RiverSystem.RiverParts.Boat import Boat


class ReverseBoatListIterator:
    """
    Iterator for iterating over a list of boats in reverse order.

    Methods:
        __init__(self, boat_list)
            Initializes the iterator with a list of boats.

        __iter__(self)
            Returns the iterator object itself.

        __next__(self)
            Retrieves the next boat in reverse order.
            Raises StopIteration when there are no more boats to iterate.

    Example:
        boat_list = [boat1, boat2, boat3]
        reverse_iterator = ReverseBoatListIterator(boat_list)
        for boat in reverse_iterator:
            print(boat)
    """

    def __init__(self, boat_list: List[Optional[Boat]]):
        """
        Initializes the iterator with a list of boats.

        Args:
            boat_list (List[Optional[Boat]]): The list of boats to iterate over.

        Returns:
            None
        """
        self.boat_list: List[Optional[Boat]] = boat_list
        self.index: int = len(boat_list) - 1

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            Iterator object
        """
        return self

    def __next__(self):
        """
        Retrieves the next boat in reverse order.
        Raises StopIteration when there are no more boats to iterate.

        Returns:
            Boat: The next boat in reverse order.

        Raises:
            StopIteration: When there are no more boats to iterate.
        """
        if self.index >= 0:
            current_boat = self.boat_list[self.index]
            self.index -= 1
            return current_boat
        else:
            raise StopIteration
