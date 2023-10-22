from typing import List

from morgan_jonah.Iterators.ReverseRiverPartIterator import ReverseRiverPartIterator
from morgan_jonah.LockBehavior.BasicLockBehavior import BasicLockBehavior
from morgan_jonah.LockBehavior.FastLockBehavior import FastLockBehavior
from morgan_jonah.RiverSystem.RiverParts import RiverPart, Boat
from morgan_jonah.RiverSystem.RiverParts.Lock import Lock
from morgan_jonah.RiverSystem.RiverParts.Section import Section
from morgan_jonah.Iterators.RiverPartIterator import RiverPartIterator
from morgan_jonah.Iterators.SectionIterator import SectionIterator


class RiverSystem():

    def __init__(self, create_default=True):
        self.__river_parts: List[RiverPart] = []

        if create_default:
            self.add_river_part(Section(6, 0, 1))
            self.add_river_part(Lock())
            self.add_river_part(Section(3, 1, 2))

    def add_river_part(self, part: RiverPart):
        self.__river_parts.append(part)

        if len(self.__river_parts) > 1 and self.__river_parts[-2].next is None:
            self.__river_parts[-2].next = part

    def add_boat(self, boat: Boat) -> bool:
        if len(self.__river_parts) == 0:
            return False

        first_part = self.__river_parts[0]

        if first_part.is_open():
            first_part.receive_boat(boat)
            return True

        return False

    def update(self):
        # GRADING: LOOP_ALL
        river_part_itr = ReverseRiverPartIterator(self.__river_parts)
        for part in river_part_itr:
            part.update()

    def show_section_details(self):
        iter = SectionIterator(self.__river_parts)
        for section in iter:
            print(section.details())
            print()

    def clear(self):
        self.__river_parts = []

    def make_tester_river(self):
        self.__river_parts = []
        self.add_river_part(Section(5, 0, 1))
        self.add_river_part(Lock())  # none/pass-through behavior
        self.add_river_part(Section(6, 2, 2))
        self.add_river_part(Lock(2, BasicLockBehavior()))
        self.add_river_part(Section(3, 3, 3))
        self.add_river_part(Lock(5, FastLockBehavior()))

    def __str__(self):
        river_str = ''

        river_itr = RiverPartIterator(self.__river_parts)
        for part in river_itr:
            river_str += str(part)

        river_str += '\n'

        river_itr = RiverPartIterator(self.__river_parts)
        for part in river_itr:
            river_str += part.alt_str()

        return river_str