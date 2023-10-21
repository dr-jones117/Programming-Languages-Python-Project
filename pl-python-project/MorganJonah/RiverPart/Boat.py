from MorganJonah.BoatBehavior.BoatBehavior import BoatBehavior, SteadyBoatBehavior


class Boat:
    def __init__(self, id: int, power: int = 1, boat_behavior: BoatBehavior = SteadyBoatBehavior()):
        self.boat_behavior = boat_behavior
        self.__id: int = id
        self.power: int = power
        self.__symbol: str = '⛴'

    def __str__(self):
        return self.__symbol

    def get_id(self):
        return str(self.__id)
