from typing import List

from morgan_jonah.RiverSystem.RiverParts.RiverPart import RiverPart
from morgan_jonah.RiverSystem.RiverParts.Section import Section


class SectionIterator:
    """
    Iterator for iterating over a list of sections in a river system.

    Methods:
        __init__(self, sections)
            Initializes the iterator with a list of river parts.

        __iter__(self)
            Returns the iterator object itself.

        __next__(self)
            Retrieves the next section in the river system.
            Raises StopIteration when there are no more sections to iterate.

    Example:
        river_parts = [part1, part2, part3]
        section_iterator = SectionIterator(river_parts)
        for section in section_iterator:
            print(section)
    """

    def __init__(self, sections: List[RiverPart]):
        """
        Initializes the iterator with a list of river parts.

        Args:
            sections (List[RiverPart]): The list of river parts to iterate over.

        Returns:
            None
        """
        self.sections: List[RiverPart] = sections
        self.idx = 0

    # GRADING: ITER_RESTRICT
    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            Iterator object
        """
        return self

    def __next__(self):
        """
        Retrieves the next section in the river system.
        Raises StopIteration when there are no more sections to iterate.

        Returns:
            Section: The next section in the river system.

        Raises:
            StopIteration: When there are no more sections to iterate.
        """
        while self.idx < len(self.sections):
            if isinstance(self.sections[self.idx], Section):
                section = self.sections[self.idx]
                self.idx += 1
                return section
            self.idx += 1

        raise StopIteration
