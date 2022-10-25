class Dot:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def neighbors(self):
        dot_list = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not (x == 0 and y == 0):
                    dot_list.append(Dot(self.x + x, self.y + y))
        return dot_list

    def __str__(self):
        return f"({self.x}, {self.y})"

