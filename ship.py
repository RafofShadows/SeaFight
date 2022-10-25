import enum

from dot import Dot


class Ship:
    def __init__(self, start, direction, size):
        self.start = start
        self.direction = direction
        self.size = size
        self._health = size

    def dots(self):
        dot_list = []
        for i in range(self.size):
            if self.direction:
                dot_list.append(Dot(self.start.x + i, self.start.y))
            else:
                dot_list.append(Dot(self.start.x, self.start.y + 1))
        return dot_list

    def hit(self):
        self._health -= 1

    @property
    def health(self):
        return self._health


class ShipDirection(enum.Enum):
    horizontal = 0  # слева направо
    vertical = 1    # сверху вниз
