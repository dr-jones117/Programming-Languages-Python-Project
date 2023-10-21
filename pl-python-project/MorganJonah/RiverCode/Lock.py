from .Boat import Boat

class Lock:
    def __init__(self, depth: int = 0):
        self.depth: int = depth
        self.lock_behavior = None
        self.boat: Boat = None

    def __str__(self):
        if self.boat is None:
            return f'......'
        else:
            return f'{str(self.boat.id)}.....'

