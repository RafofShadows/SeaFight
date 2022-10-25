import enum

from ship import *
from exceptions import *


class Board:
    def __init__(self, size, is_hidden):
        self.size = size
        self.hid = is_hidden
        self.dot_list = [[DotState.empty for i in range(size)] for j in range(size)]
        self.ship_list = []

    def out(self, dot):
        return not (0 <= dot.x < self.size and 0 <= dot.y < self.size)

    def state(self, dot):
        return self.dot_list[dot.y][dot.x]

    def set_state(self, dot, state):
        self.dot_list[dot.y][dot.x] = state

    def contour(self, ship, hide):
        for dot in ship.dots():
            for n_dot in dot.neighbors():
                if not self.out(n_dot) and self.state(n_dot) != DotState.hit and self.state(n_dot) != DotState.occupied:
                    if hide:
                        self.set_state(n_dot, DotState.miss)
                    else:
                        self.set_state(n_dot, DotState.unavailable)

    def add_ship(self, ship):
        for dot in ship.dots():
            if self.out(dot):
                raise OutOfBoundsError("Точка корабля находится за пределами доски.")
            elif self.state(dot) != DotState.empty:
                raise IntersectionError("Одна из точек корабля имеет уже занята.")
        for dot in ship.dots():
            self.set_state(dot, DotState.occupied)
        self.ship_list.append(ship)
        self.contour(ship, False)

    def ships_left(self):
        return sum(map(lambda x: x.health > 0, self.ship_list))

    def shot(self, dot):
        if self.out(dot):
            raise OutOfBoundsError("Точка находится за пределами доски.")
        elif self.state(dot) == DotState.miss or self.state(dot) == DotState.hit:
            raise IntersectionError("Невозможно выстрелить: выстрел уже был произведен.")
        if self.state(dot) == DotState.occupied:
            self.set_state(dot, DotState.hit)
            for ship in self.ship_list:
                if dot in ship.dots():
                    ship.hit()
                    if ship.health < 1:
                        self.contour(ship, True)
                        return ShotResult.kill
                    else:
                        return ShotResult.wound
        elif self.state(dot) == DotState.empty or self.state(dot) == DotState.unavailable:
            self.set_state(dot, DotState.miss)
            return ShotResult.miss

    def __str__(self):
        result = "  |"
        for i in range(self.size):
            result += f"{i}|"
        result += "\n"
        for i, line in enumerate(self.dot_list):
            result += f"{i} |" + "|".join([self.state_str(s) for s in line]) + "|\n"
        return result

    def state_str(self, state):
        if state == DotState.empty:
            return "O"
        if state == DotState.miss:
            return "T"
        if state == DotState.hit:
            return "X"
        if self.hid:
            return "O"
        if state == DotState.unavailable:
            return "*"
        return "N"


class DotState(enum.Enum):
    empty = 0
    unavailable = 1
    occupied = 2
    miss = 3
    hit = 4


class ShotResult(enum.Enum):
    miss = 0
    wound = 1
    kill = 2
