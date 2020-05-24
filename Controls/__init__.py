from pygame_tools.Controls.Key import *


def bind(key: Key, func):
    key.function = func
