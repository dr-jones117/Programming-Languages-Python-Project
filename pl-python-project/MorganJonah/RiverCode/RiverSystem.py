from .Section import Section
from .Lock import Lock
from .Iterators.SectionIterator import SectionIterator
from .Boat import Boat
class RiverSystem:
    def __init__(self):
        self.river_parts = []
        self.__init_default_system()

    def __init_default_system(self):
        parts = []
        parts.append(Section())
        parts.append(Lock())
        parts.append(Section(3, 1))
        self.river_parts = parts

    def update(self):
        return

    def add_boat(self, boat: Boat):
        self.river_parts[0].boats.append(boat)


    def __str__(self):
        riverStr = ''
        iterator = SectionIterator(self.river_parts)
        for a in iterator:
            riverStr += str(a)

        return riverStr
