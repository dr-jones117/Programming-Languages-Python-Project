from typing import List, Optional

from morgan_jonah.Iterators.ReverseBoatListIterator import ReverseBoatListIterator
from morgan_jonah.RiverSystem.RiverParts.Boat import Boat
from morgan_jonah.RiverSystem.RiverParts.RiverPart import RiverPart



class Section(RiverPart):
    """
    Represents a section in the river simulation.

    Attributes:
        length (int): The length of the section.
        flow (int): The flow rate of the section.
        symbol (str): The symbol representing the section.
        boats (List[Optional[Boat]]): The list of boats within the section.
        id (int): The unique identifier for the section.

    Methods:
        __init__(self, length: int = 1, flow: int = 1, id: int = 1)
            Initializes a Section instance with the given length, flow rate, and ID.

        update(self)
            Updates the positions of boats within the section.

        update_boat_at_pos(self, start_idx: int)
            Updates the position of a boat starting from a specified index.

        remove_boat(self, boat: Boat)
            Removes a boat from the section.

        is_open(self) -> bool
            Checks if the section is open and can receive a boat.

        details(self) -> str
            Returns details about the section, including the number of boats and the flow rate.

        receive_boat(self, boat: Boat)
            Receives a boat into the section.

        __str__(self)
            Returns the string representation of the section.

        alt_str(self)
            Returns an alternative string representation of the section, useful for debugging.

    Example:
        my_section = Section(length=5, flow=2, id=2)
    """

    def __init__(self, length: int = 1, flow: int = 1, id: int = 1):
        """
        Initialize a Section instance with the given length, flow rate, and ID.

        Args:
            length (int): The length of the section. Default is 1.
            flow (int): The flow rate of the section. Default is 1.
            id (int): The unique identifier for the section. Default is 1.

        Returns:
            None
        """
        super().__init__()
        self.length: int = length
        self.flow: int = flow
        self.symbol: str = '〜'
        self.boats: List[Optional[Boat]] = []
        self.id = id

        for i in range(self.length):
            self.boats.append(None)

    def update(self):
        """
        Updates the positions of boats within the section.

        Args:
            None

        Returns:
            None
        """
        iter = ReverseBoatListIterator(self.boats)
        for boat in iter:
            if boat is not None:
                self.update_boat_at_pos(iter.index + 1)

    def update_boat_at_pos(self, start_idx: int):
        """
        Updates the position of a boat starting from a specified index.

        Args:
            start_idx (int): The index from which to start updating the boat's position.

        Returns:
            None
        """
        actual_start_idx = start_idx
        boat = self.boats[start_idx]
        distance = boat.boat_behavior.get_update_distance(boat.power, self.flow)

        handled_long_distance = False
        for i in range(distance):
            if handled_long_distance:
                break

            offset = start_idx + 1
            if offset >= len(self.boats):
                handled_long_distance = True

                if self.next is not None and self.next.is_open() and actual_start_idx == len(self.boats) - 1:
                    self.next.receive_boat(self.boats[start_idx])
                    self.boats[start_idx] = None
                elif self.next is None and actual_start_idx == start_idx:
                    self.boats[start_idx] = None
                else:
                    return

            elif self.boats[offset] is None:
                self.boats[offset] = self.boats[start_idx]
                self.boats[start_idx] = None
            elif self.boats[offset] is not None:
                return

            start_idx = offset

    def remove_boat(self, boat: Boat):
        """
        Removes a boat from the section.

        Args:
            boat (Boat): The boat to be removed.

        Returns:
            None
        """
        boat = None

    def is_open(self) -> bool:
        """
        Checks if the section is open and can receive a boat.

        Args:
            None

        Returns:
            bool: True if the section is open, False otherwise.
        """
        if self.boats[0] is None:
            return True
        return False

    def details(self) -> str:
        """
        Returns details about the section, including the number of boats and the flow rate.

        Args:
            None

        Returns:
            str: Details about the section.
        """
        boat_amount = 0

        for boat in self.boats:
            if boat is not None:
                boat_amount += 1

        return f'Section {self.id}\nBoats: {boat_amount} Flow: {self.flow}'

    def receive_boat(self, boat: Boat):
        """
        Receives a boat into the section.

        Args:
            boat (Boat): The boat to be received.

        Returns:
            None
        """
        self.boats[0] = boat

    def __str__(self):
        """
        Return the string representation of the section.

        Args:
            None

        Returns:
            str: The string representation of the section.
        """
        section_str = ''

        for boat in self.boats:
            if boat is None:
                section_str += self.symbol * 3
            else:
                section_str += str(boat) + (self.symbol * 2)

        return section_str

    def alt_str(self):
        """
        Return an alternative string representation of the section, useful for debugging.

        Args:
            None

        Returns:
            str: The alternative string representation of the section.
        """
        section_str = ''

        for boat in self.boats:
            if boat is None:
                section_str += self.symbol * 3
            else:
                section_str += boat.get_id() + (self.symbol * (3 - (len(boat.get_id()))))

        return section_str
