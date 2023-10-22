from typing import List

from morgan_jonah.RiverSystem.RiverParts.RiverPart import RiverPart


class RiverPartIterator:
    """
    Iterator for iterating over a list of river parts.

    Methods:
        __init__(self, river_parts)
            Initializes the iterator with a list of river parts.

        __iter__(self)
            Returns the iterator object itself.

        __next__(self)
            Retrieves the next river part. Raises StopIteration
            when there are no more river parts to iterate.

    Example:
        river_parts = [part1, part2, part3]
        iterator = RiverPartIterator(river_parts)
        for part in iterator:
            print(part)
    """

    def __init__(self, river_parts: List[RiverPart]):
        """
        Initializes the iterator with a list of river parts.

        Args:
            river_parts (List[RiverPart]): The list of river
            parts to iterate over.

        Returns:
            None
        """
        self.river_parts: List[RiverPart] = river_parts
        self.idx = 0

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            Iterator object
        """
        return self

    def __next__(self):
        """
        Retrieves the next river part. Raises StopIteration when there
        are no more river parts to iterate.

        Returns:
            RiverPart: The next river part.

        Raises:
            StopIteration: When there are no more river parts to iterate.
        """
        if self.idx < len(self.river_parts):
            current_part = self.river_parts[self.idx]
            self.idx += 1
            return current_part
        else:
            raise StopIteration
