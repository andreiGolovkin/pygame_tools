#!/usr/bin/env python3

import numpy as np
from math import degrees, cos, sin, atan2, sqrt
from pygame_tools.Geometry.Transform import Transform


def create(start: Transform, finish: Transform, slope):
    param = np.zeros([2, 4])

    for axis in range(2):
        param[axis, 0] = 2*start.mat[axis, 2] - 2*finish.mat[axis, 2] + slope*start.mat[axis, 0] + slope*finish.mat[axis, 0]
        param[axis, 1] = -3*start.mat[axis, 2] + 3*finish.mat[axis, 2] - 2*start.mat[axis, 0]*slope - finish.mat[axis, 0]*slope
        param[axis, 2] = start.mat[axis, 0]*slope
        param[axis, 3] = start.mat[axis, 2]

    return param


def evaluate(params: np.ndarray, t):
    pos = np.zeros([2, len(t)])
    for n in range(len(t)):

        tt = t[n] * t[n]
        ttt = tt * t[n]

        pos[0, n] = params[0, 0]*ttt + params[0, 1]*tt + params[0, 2]*t[n] + params[0, 3]
        pos[1, n] = params[1, 0]*ttt + params[1, 1]*tt + params[1, 2]*t[n] + params[1, 3]
    return pos


def get(start: Transform, finish: Transform, tc=100, slope_coef=2.0):
    t = []
    a = 0
    while a <= tc:
        t.append(a / tc)
        a += 1

    geom_slope = slope_coef * start.dist_to(finish)

    param = create(start, finish, geom_slope)

    np_spline = evaluate(param, t)

    spline = []
    for n in range(np_spline.shape[1]-1):
        x = np_spline[0, n]
        y = np_spline[1, n]
        
        if n == 0:
            a = start.get_angle()
        elif n == np_spline.shape[1]-2:
            a = finish.get_angle()
        else:
            ox, oy = spline[-1].to_xy()
            a = atan2(y-oy, x-ox)
        point = Transform(x, y, a)
        spline.append(point)

    return spline
