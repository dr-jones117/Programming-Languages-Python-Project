from typing import List, Optional

from morgan_jonah.RiverSystem.RiverParts.Boat import Boat


class SectionBoatsIterator:
    """
    Iterator for iterating over a list of boats in a section.

    Methods:
        __init__(self, boats)
            Initializes the iterator with a list of boats in a section.

        __iter__(self)
            Returns the iterator object itself.

        __next__(self)
            Retrieves the next boat in the section. Raises StopIteration
            when there are no more boats to iterate.

    Example:
        boats_in_section = [boat1, boat2, boat3]
        iterator = SectionBoatsIterator(boats_in_section)
        for boat in iterator:
            print(boat)
    """

    def __init__(self, boats: List[Optional[Boat]]):
        """
        Initializes the iterator with a list of boats in a section.

        Args:
            boats (List[Optional[Boat]]): The list of boats in the
            section to iterate over.

        Returns:
            None
        """
        self.boats = boats
        self.idx = 0
        self.length = len(self.boats)

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            Iterator object
        """
        return self

    def __next__(self):
        """
        Retrieves the next boat in the section. Raises StopIteration
        when there are no more boats to iterate.

        Returns:
            Boat: The next boat in the section.

        Raises:
            StopIteration: When there are no more boats to iterate.
        """
        if self.idx < self.length:
            value = self.boats[self.idx]
            self.idx += 1
            return value
        else:
            raise StopIteration
