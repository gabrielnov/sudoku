class Play:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

class Game:
    def __init__(self, player, tries, level):
        self.player = player
        self.tries = tries
        self.level = level
