from pygame_tools.Geometry.Point import Point


def get_intersection(p11: Point, p12: Point, p21: Point, p22: Point):
    intersection = {"is_intersects": False, "would_intersects": False, "intersection_point": None}

    x1 = p11.x
    y1 = p11.y
    x2 = p12.x
    y2 = p12.y

    x3 = p21.x
    y3 = p21.y
    x4 = p22.x
    y4 = p22.y

    div = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if div != 0:
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / div
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / div

        if 0 <= t and 0 <= u <= 1:
            px = x1 + t * (x2 - x1)
            py = y1 + t * (y2 - y1)

            intersection["is_intersects"] = 0 <= t <= 1 and 0 <= u <= 1
            intersection["would_intersects"] = True
            intersection["intersection_point"] = Point(px, py)

    return intersection
