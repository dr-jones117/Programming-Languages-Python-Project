from typing import List

from MorganJonah.RiverPart.RiverPart import RiverPart
from MorganJonah.RiverPart.Section import Section


class SectionIterator:
    def __init__(self, sections: List[RiverPart]):
        self.sections: List[RiverPart] = sections
        self.idx = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.sections):
            if isinstance(self.sections[self.idx], Section):
                section = self.sections[self.idx]
                self.idx += 1
                return section
            else:
                while self.idx < len(self.sections):
                    if isinstance(self.sections[self.idx], Section):
                        section = self.sections[self.idx]
                        self.idx += 1
                        return section
                    self.idx += 1

        raise StopIteration

