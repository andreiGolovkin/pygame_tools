from pygame_tools.Drawing_tools import *
from pygame_tools.Geometry.Point import Point


class Button(pg.Surface):
    def __init__(self, x, y, w, h):
        super(Button, self).__init__([w, h])

        self.pos = Point(x, y)
        self.mouse = get_mouse()

        self.function = self.default_function

        self.fill(WHITE)

    def draw(self):
        draw_surface(self, self.pos)

    def check_event(self):
        if self.function and self.is_pressed():
            self.function()

    def default_function(self):
        print("Button is pressed")

    def is_pressed(self) -> bool:
        return self.get_rect().collidepoint(*(self.mouse - self.pos).as_tuple()) and self.mouse.left_pressed
