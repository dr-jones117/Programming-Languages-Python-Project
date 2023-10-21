class Section:
    def __init__(self, length: int = 6, flow: int = 0):
        self.symbol = '~'
        self.length: int = length
        self.flow: int = flow
        self.boats = []

    def __str__(self):
        sect_str = self.symbol * 3 * self.length

        for boat in self.boats:
            sect_str = sect_str[:boat.location * 3] + boat.id) + sect_str[boat.location * 3 + 1:]

        return sect_str

    def details(self):
        return