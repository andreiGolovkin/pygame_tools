import pygame as pg
from pygame_tools.Geometry.Point import Point


class Mouse(Point):
    def __init__(self):
        super(Mouse, self).__init__()

        self.prev = None

        self.right = False
        self.left = False
        self.wheel = False

        self.right_pressed = False
        self.left_pressed = False
        self.wheel_pressed = False

        self.right_released = False
        self.left_released = False
        self.wheel_released = False

    def update(self):
        self.prev = self.copy()

        self.update_mouse_pos()
        self.check_pressed()

    def update_mouse_pos(self):
        self.x, self.y = pg.mouse.get_pos()

    def check_pressed(self):
        self.right_pressed = False
        self.left_pressed = False
        self.wheel_pressed = False

        self.right_released = False
        self.left_released = False
        self.wheel_released = False

        new_left, new_wheel, new_right = pg.mouse.get_pressed()

        if new_right and not self.right:
            self.right_pressed = True
        elif not new_right and self.right:
            self.right_released = True

        if new_wheel and not self.wheel:
            self.wheel_pressed = True
        elif not new_wheel and self.wheel:
            self.wheel_released = True

        if new_left and not self.left:
            self.left_pressed = True
        elif not new_left and self.left:
            self.left_released = True

        self.right, self.wheel, self.left = new_right, new_wheel, new_left

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " right: " + str(self.right) + " wheel: " + str(self.wheel)\
               + " left: " + str(self.left)

    def copy(self):
        mouse_copy = Mouse()
        mouse_copy.x = self.x
        mouse_copy.y = self.y
        mouse_copy.right = self.right
        mouse_copy.left = self.left
        mouse_copy.wheel = self.wheel
        mouse_copy.right_pressed = self.right_pressed
        mouse_copy.left_pressed = self.left_pressed
        mouse_copy.wheel_pressed = self.wheel_pressed
        mouse_copy.right_released = self.right_released
        mouse_copy.left_released = self.left_released
        mouse_copy.wheel_released = self.wheel_released

        return mouse_copy
