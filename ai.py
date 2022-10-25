from player import *
import random


class AI(Player):
    def ask(self):
        x = random.randint(0, self.board.size)
        y = random.randint(0, self.board.size)
        return Dot(x, y)
