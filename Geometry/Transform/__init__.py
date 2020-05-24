import numpy as np
from math import degrees, cos, sin, atan2, sqrt


class Transform:
    def __init__(self, x=0., y=0., theta=0.):
        self.mat = np.array([])
        self.init_mat(x, y, theta)

    def init_mat(self, x=0., y=0., theta=0.):
        self.mat = np.array([[cos(theta), -sin(theta), x],
                             [sin(theta), cos(theta), y],
                             [0, 0, 1]])

    def get_x(self):
        return self.mat[0][2]

    def get_y(self):
        return self.mat[1][2]

    def get_angle(self):
        return atan2(self.mat[1, 0], self.mat[0, 0])

    def get_mag(self):
        mag = sqrt(self.get_x()**2 + self.get_y()**2)

        return mag

    def add_t(self, offset):
        self.mat = np.matmul(self.mat, offset.mat)

    def add(self, x_offset=0, y_offset=0, theta_offset=0):
        offset = __class__(x_offset, y_offset, theta_offset)
        self.add_t(offset)

    def get_offset(self, other):
        inv_origin = self.inverse()
        offset = inv_origin.with_offset_t(other)
        return offset

    def with_offset(self, x_offset=0, y_offset=0, theta_offset=0):
        offset = self.__class__(x=x_offset, y=y_offset, theta=theta_offset)
        transform = self.with_offset_t(offset)
        return transform

    def with_offset_t(self, offset):
        mat = np.matmul(self.mat, offset.mat)
        transform = self.from_mat(mat)
        return transform

    def to_xy(self):
        x = self.get_x()
        y = self.get_y()

        return x, y

    def dist_to(self, other):
        x1, y1 = self.to_xy()
        x2, y2 = other.to_xy()

        x = x2 - x1
        y = y2 - y1

        dist = sqrt(x**2 + y**2)
        return dist

    def to_xya(self):
        x, y = self.to_xy()
        theta = self.get_angle()

        return x, y, theta

    def __str__(self):
        return 'x: ' + str(self.get_x()) + ' y: ' + str(self.get_y()) + ' theta: ' + str(degrees(self.get_angle()))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            ans = self.mat == other.mat
        else:
            ans = NotImplemented
        return ans

    def inverse_self(self):
        self.mat = np.linalg.inv(self.mat)

    def inverse(self):
        mat = np.linalg.inv(self.mat)
        return self.from_mat(mat)

    def copy(self):
        return Transform.from_mat(self.mat)

    @classmethod
    def from_mat(cls, mat: np.array):
        transform = cls()
        transform.mat = mat
        return transform
