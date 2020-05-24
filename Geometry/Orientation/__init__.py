from pygame_tools.Geometry.Point import Point
from pygame_tools.Geometry.Transform import Transform
from pygame_tools import Drawing_tools as draw
from math import sin, cos


class Orientation(Point):
    def __init__(self, x: float = 0, y: float = 0, angle: float = 0):
        super(Orientation, self).__init__(x, y)

        self.angle = angle

    def equals(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.angle == other.angle

    def copy(self):
        return Orientation(self.x, self.y, self.angle)

    def draw_dir(self):
        draw.ellipse(self.x + cos(self.angle)*10, self.y + sin(self.angle)*10, 5, 5)

    def draw_pos(self):
        draw.ellipse(self.x, self.y, 10, 10)
