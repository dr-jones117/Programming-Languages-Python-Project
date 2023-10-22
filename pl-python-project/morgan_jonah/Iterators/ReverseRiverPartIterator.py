from typing import List

from morgan_jonah.RiverSystem.RiverParts.RiverPart import RiverPart


class ReverseRiverPartIterator:
    """
    Iterator for iterating over a list of river parts in reverse order.

    Methods:
        __init__(self, river_parts)
            Initializes the iterator with a list of river parts.

        __iter__(self)
            Returns the iterator object itself.

        __next__(self)
            Retrieves the next river part in reverse order.
            Raises StopIteration when there are no more river parts to iterate.

    Example:
        river_parts = [part1, part2, part3]
        reverse_iterator = ReverseRiverPartIterator(river_parts)
        for part in reverse_iterator:
            print(part)
    """

    def __init__(self, river_parts: List[RiverPart]):
        """
        Initializes the iterator with a list of river parts.

        Args:
            river_parts (List[RiverPart]): The list of river parts to iterate over.

        Returns:
            None
        """
        self.river_parts: List[RiverPart] = river_parts
        self.idx = len(river_parts) - 1

    # GRADING: ITER_ALL
    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            Iterator object
        """
        return self

    def __next__(self):
        """
        Retrieves the next river part in reverse order.
        Raises StopIteration when there are no more river parts to iterate.

        Returns:
            RiverPart: The next river part in reverse order.

        Raises:
            StopIteration: When there are no more river parts to iterate.
        """
        if self.idx >= 0:
            current_part = self.river_parts[self.idx]
            self.idx -= 1
            return current_part
        else:
            raise StopIteration
