from typing import List

from MorganJonah.RiverPart import RiverPart, Boat
from MorganJonah.RiverPart.Lock import Lock
from MorganJonah.RiverPart.Section import Section


class RiverSystem():
    DEBUG_PRINT = False

    def __init__(self, create_default=True):
        self.river_parts: List[RiverPart] = []

        if create_default:
            self.add_river_part(Section(6, 0))
            self.add_river_part(Lock())
            self.add_river_part(Section(3, 1))

        if self.DEBUG_PRINT:
            for part in self.river_parts:
                print(f'{part} {part.next}')

    def add_river_part(self, part: RiverPart):
        self.river_parts.append(part)

        if len(self.river_parts) > 1 and self.river_parts[-2].next is None:
            self.river_parts[-2].next = part

    def add_boat(self, boat: Boat) -> bool:
        first_part = self.river_parts[0]

        if first_part.is_open():
            first_part.receive_boat(boat)
            return True

        return False

    def update(self):
        for part in reversed(self.river_parts):
            part.update()

    def __str__(self):
        river_str = ''

        for part in self.river_parts:
            river_str += str(part)

        river_str += '\n'

        for part in self.river_parts:
            river_str += part.alt_str()

        return river_str
