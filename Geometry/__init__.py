from pygame_tools.Geometry.Transform import *
from pygame_tools.Geometry.Point import *
from pygame_tools.Geometry.Orientation import *


def to_transform(point) -> Transform:
    transform = point

    if isinstance(point, Orientation):
        transform = o2t(point)
    elif isinstance(point, Point):
        transform = p2t(point)

    return transform


def to_orientation(point) -> Orientation:
    orient = point

    if isinstance(point, Transform):
        orient = t2o(point)
    elif isinstance(point, Point):
        orient = p2o(point)

    return orient


def to_point(point) -> Point:
    if isinstance(point, Orientation):
        point = o2p(point)
    elif isinstance(point, Transform):
        point = t2p(point)

    return point


def t2o(point: Transform) -> Orientation:
    coord = get_coord_from_transform(point)
    return Orientation(*coord)


def t2p(point: Transform) -> Point:
    coord = get_coord_from_transform(point)
    return Point(*coord[0:2])


def o2p(point: Orientation) -> Point:
    coord = get_coord_from_orientation(point)
    return Point(*coord[0:2])


def o2t(point: Orientation) -> Transform:
    coord = get_coord_from_orientation(point)
    return Transform(*coord)


def p2o(point: Point) -> Orientation:
    coord = get_coord_from_point(point)
    return Orientation(*coord)


def p2t(point: Point) -> Transform:
    coord = get_coord_from_point(point)
    return Transform(*coord)


def get_coord_from_transform(point: Transform) -> tuple:
    x = point.get_x()
    y = point.get_y()
    angle = point.get_angle()

    return x, y, angle


def get_coord_from_point(point: Point) -> tuple:
    x = point.x
    y = point.y
    angle = 0

    return x, y, angle


def get_coord_from_orientation(point: Orientation) -> tuple:
    x = point.x
    y = point.y
    angle = point.angle

    return x, y, angle

