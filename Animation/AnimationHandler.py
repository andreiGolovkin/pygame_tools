from pygame_tools.Animation import Animation
from pygame_tools.Geometry import Point
from pygame_tools.Timer import Timer


class AnimationHandler:
    def __init__(self):
        self.animations = []
        self.current = 0

        self.timer = Timer(0.13)

    def add_animation(self, animation: Animation) -> int:
        self.animations.append(animation)

        index = len(self.animations) - 1
        return index

    def play(self, offset: Point):
        if len(self.animations) > 0:
            self.update()
            self.draw(offset)

    def update(self):
        if self.timer.is_finished():
            self.animations[self.current].next_frame()

    def draw(self, offset: Point, scale=1):
        self.animations[self.current].draw(offset, scale=scale)

    def switch_to(self, index: int):
        self.current = index
        self.timer.restart()
