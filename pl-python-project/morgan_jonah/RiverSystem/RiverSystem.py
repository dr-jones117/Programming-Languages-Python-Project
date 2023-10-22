from typing import List

from morgan_jonah.Iterators.ReverseRiverPartIterator import ReverseRiverPartIterator
from morgan_jonah.LockBehavior.BasicLockBehavior import BasicLockBehavior
from morgan_jonah.LockBehavior.FastLockBehavior import FastLockBehavior
from morgan_jonah.RiverSystem.RiverParts import RiverPart, Boat
from morgan_jonah.RiverSystem.RiverParts.Lock import Lock
from morgan_jonah.RiverSystem.RiverParts.Section import Section
from morgan_jonah.Iterators.RiverPartIterator import RiverPartIterator
from morgan_jonah.Iterators.SectionIterator import SectionIterator

from typing import List


class RiverSystem:
    """
    Represents a river simulation system.

    This class models a river system containing various river components,
    including sections and locks. It allows the addition of boats to the
    river and provides methods for updating the simulation and displaying section details.

    Attributes:
        __river_parts (List[RiverPart]): A list of river parts, including sections and locks.

    Methods:
        __init__(self, create_default=True)
            Initializes a RiverSystem with optional default river components.

        add_river_part(self, part: RiverPart)
            Adds a river component (section or lock) to the river system.

        add_boat(self, boat: Boat) -> bool
            Attempts to add a boat to the river system.

        update(self)
            Updates the river system for one time step.

        show_section_details(self)
            Displays details of each section in the river system.

        clear(self)
            Clears all river components from the river system.

        make_tester_river(self)
            Creates a tester river with predefined river components for debugging.

        __str__(self)
            Returns a string representation of the river system.

    Example:
        my_river_system = RiverSystem(create_default=True)
        my_river_system.add_river_part(Section(5, 0, 1))
        my_river_system.add_river_part(Lock())
        my_river_system.add_river_part(Section(6, 2, 2))
    """

    def __init__(self, create_default=True):
        """
        Initialize a RiverSystem with optional default river components.

        Args:
            create_default (bool): If True, creates a river system
            with default river components. Default is True.

        Returns:
            None
        """
        self.__river_parts: List[RiverPart] = []

        if create_default:
            self.add_river_part(Section(6, 0, 1))
            self.add_river_part(Lock())
            self.add_river_part(Section(3, 1, 2))

    def add_river_part(self, part: RiverPart):
        """
        Add a river component (section or lock) to the river system.

        Args:
            part (RiverPart): The river component to be added.

        Returns:
            None
        """
        self.__river_parts.append(part)

        if len(self.__river_parts) > 1 and self.__river_parts[-2].next is None:
            self.__river_parts[-2].next = part

    def add_boat(self, boat: Boat) -> bool:
        """
        Attempt to add a boat to the river system.

        Args:
            boat (Boat): The boat to be added.

        Returns:
            bool: True if the boat was successfully added, False otherwise.
        """
        if len(self.__river_parts) == 0:
            return False

        first_part = self.__river_parts[0]

        if first_part.is_open():
            first_part.receive_boat(boat)
            return True

        return False

    # GRADING: LOOP_ALL
    def update(self):
        """
        Update the river system for one time step.

        Args:
            None

        Returns:
            None
        """
        river_part_itr = ReverseRiverPartIterator(self.__river_parts)
        for part in river_part_itr:
            part.update()

    def show_section_details(self):
        """
        Display details of each section in the river system.

        Args:
            None

        Returns:
            None
        """
        # GRADING: LOOP_RESTRICT
        iter = SectionIterator(self.__river_parts)
        for section in iter:
            print(section.details())
            print()

    def clear(self):
        """
        Clear all river components from the river system.

        Args:
            None

        Returns:
            None
        """
        self.__river_parts = []

    def make_tester_river(self):
        """
        Create a tester river with predefined river components for debugging.

        Args:
            None

        Returns:
            None
        """
        self.__river_parts = []
        self.add_river_part(Section(5, 0, 1))
        self.add_river_part(Lock())  # none/pass-through behavior
        self.add_river_part(Section(6, 2, 2))
        self.add_river_part(Lock(2, BasicLockBehavior()))
        self.add_river_part(Section(3, 3, 3))
        self.add_river_part(Lock(5, FastLockBehavior()))

    def __str__(self):
        """
        Return a string representation of the river system.

        Args:
            None

        Returns:
            str: A string representation of the river system.
        """
        river_str = ''

        river_itr = RiverPartIterator(self.__river_parts)
        for part in river_itr:
            river_str += str(part)

        river_str += '\n'

        river_itr = RiverPartIterator(self.__river_parts)
        for part in river_itr:
            river_str += part.alt_str()

        return river_str
