class Boat:
    def __init__(self, id: int, power: int = 1):
        self.id: int = id
        self.power: int = power
        self.symbol: str = '⛴'

    def __str__(self):
        return self.symbol
