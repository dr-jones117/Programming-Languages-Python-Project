class Boat:
    def __init__(self, id: int, power: int = 1, location: int = 0):
        self.id: int = id
        self.power: int = power
        self.boat_behavior = None
        self.location = location
        self.symbol = '⛴'

    def __str__(self):
        return self.symbol
