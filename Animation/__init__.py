import pygame
from pygame_tools.Geometry.Point import Point
from pygame_tools.Drawing_tools import *


class Animation:
    def __init__(self, source: pygame.Surface):
        self.width = 0
        self.height = 0

        self.source = source

        self.frames = []
        self.current_frame = 0

    def set_size(self, w: int, h: int):
        self.width = w
        self.height = h

    def add_frame(self, coord: Point):
        self.frames.append(coord)

    def draw(self, offset: Point, scale=1):
        if len(self.frames) > 0:
            frame = self.frames[self.current_frame]
            sprite = get_sprite(self.source, frame.x, frame.y, self.width, self.height)
            draw_image(sprite, offset.x, offset.y, sprite.get_width() * scale, sprite.get_height() * scale)

    def next_frame(self):
        self.current_frame += 1

        if self.current_frame > len(self.frames) - 1:
            self.current_frame = 0

    def prev_frame(self):
        self.current_frame -= 1

        if self.current_frame < 0:
            self.current_frame = len(self.frames) - 1
