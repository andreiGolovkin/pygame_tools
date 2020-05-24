import random as rand
from math import cos, sin, sqrt, atan2, pi


class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def equals(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def add(self, x_offset, y_offset):
        self.x += x_offset
        self.y += y_offset

    def add_point(self, offset):
        self.x += offset.x
        self.y += offset.y

    def with_offset(self, x_offset, y_offset):
        point = self.__class__(self.x + x_offset, self.y + y_offset)
        return point

    def copy(self):
        point = Point(self.x, self.y)
        return point

    def get_dir(self):
        angle = self.angle_to_base()
        return Point(cos(angle), sin(angle))

    def dist(self, other) -> float:
        x = other.x - self.x
        y = other.y - self.y

        point = Point(x, y)

        return point.mag()

    def mag(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def angle_to_base(self):
        angle = atan2(self.y, self.x)
        return angle

    def angle_to(self, other):
        x = other.x - self.x
        y = other.y - self.y

        point = self.__class__(x, y)

        return point.angle_to_base()

    def scale(self, scale_):
        return Point(self.x * scale_, self.y * scale_)

    def __eq__(self, other):
        if isinstance(other, Point):
            ans = self.equals(other)
        else:
            ans = NotImplemented
        return ans

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return Point(abs(self.x), abs(self.y))

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.scale(other)
        else:
            return NotImplemented

    @classmethod
    def random(cls, x_range, y_range):
        point = cls(rand.randint(0, x_range - 1), rand.randint(0, y_range - 1))
        return point

    @classmethod
    def zero(cls):
        point = cls(0, 0)
        return point

    @classmethod
    def from_angle(cls, angle: float, r: float):
        point = cls(cos(angle) * r, sin(angle) * r)
        return point

    def as_tuple(self) -> tuple:
        return self.x, self.y


def find_circuit(points: list) -> list:
    prepared_points = prepare_points(points)

    circuit = convex_hull(prepared_points)

    return circuit


def convex_hull(points: list) -> list:
    ans = [points[0]]
    angles = [0]
    for n in range(1, len(points)):
        current = points[n]

        last_angle = angles[len(angles) - 1]
        new_angle = ans[len(ans) - 1].angle_to(current)
        between_angle = get_angle_between(new_angle, last_angle)

        while between_angle >= pi:
            ans.pop()
            angles.pop()

            last_angle = angles[len(angles)-1]
            new_angle = ans[len(ans)-1].angle_to(current)
            between_angle = get_angle_between(new_angle, last_angle)

        ans.append(current)
        angles.append(new_angle)

    return ans


def get_angle_between(new_angle: float, last_angle: float):
    between_angle = new_angle - last_angle
    if between_angle < 0:
        between_angle = 2 * pi + between_angle

    return between_angle


def validate_angle(angle: float) -> float:
    if angle > pi or angle < -pi:
        angle = -(angle % pi)

    return angle


def prepare_points(points: list) -> list:
    base = get_base(points)

    def key(point: Point):
        if point == base:
            return -100000
        else:
            return base.angle_to(point)

    sorted_points = sorted(points, key=key)
    return sorted_points


def get_base(points: list) -> Point:
    index = find_lowest(points)
    base = points[index]
    return base


def find_lowest(points: list) -> int:
    index = -1
    lowest_y = 1000000

    for n in range(len(points)):
        if points[n].y < lowest_y:
            lowest_y = points[n].y
            index = n

    return index
