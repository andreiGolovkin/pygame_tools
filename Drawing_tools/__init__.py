import pygame as pg
from pygame_tools.Geometry.Point import Point
from pygame_tools.Geometry.Transform import Transform
from pygame_tools.Controls.Mouse import Mouse

size = width, height = 600, 600
screen = None

mouse = None

fs = 25

c = (255, 255, 255)
a = 255

WHITE = (255, 255, 255)
GREY = (180, 180, 180)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x_is_flipped = False
y_is_flipped = False


def set_win_size(w, h):
    global size
    global width
    global height
    global screen
    global mouse

    pg.init()

    width = w
    height = h
    size = width, height
    screen = pg.display.set_mode(size)
    mouse = Mouse()


def get_mouse() -> Mouse:
    global mouse
    return mouse


def save_screen_shot(file_path: str):
    global screen
    pg.image.save(screen, file_path)


def flip_along_x(flag: bool):
    global x_is_flipped
    
    x_is_flipped = flag


def flip_along_y(flag: bool):
    global y_is_flipped
    
    y_is_flipped = flag


def color(*rgb, alpha=255):
    global c
    global a

    if type(rgb[0]) == tuple:
        rgb = rgb[0]

    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    if r > 255:
        r = 255
    elif r < 0:
        r = 0

    if g > 255:
        g = 255
    elif g < 0:
        g = 0

    if b > 255:
        b = 255
    elif b < 0:
        b = 0

    c = (r, g, b)
    a = alpha


def font_size(new_font_size: int):
    global fs

    fs = new_font_size


def circuit(*points: Point, line_width: int = 1, close: bool = True):
    # if isinstance(points, tuple):
    #     points = points[0]

    if close:
        prev = points[-1]
    else:
        prev = points[0]

    for point in points:
        line(prev.x, prev.y, point.x, point.y, line_width)
        prev = point


def text(msg: str, x: int, y: int):
    global c
    global screen
    global fs

    font = pg.font.SysFont(None, fs)
    msg = font.render(msg, True, c)
    screen.blit(msg, (x, y))


def line(x1: int, y1: int, x2: int, y2: int, line_width: int = 1):
    global c
    global screen

    norm_x1, norm_y1 = normalize_axis(x1, y1)
    norm_x2, norm_y2 = normalize_axis(x2, y2)

    # print(norm_x1, norm_y1, norm_x2, norm_y2)

    w = abs(norm_x1 - norm_x2)+line_width
    h = abs(norm_y1 - norm_y2)+line_width

    if norm_x1 > norm_x2:
        inner_x1 = w-line_width
        inner_x2 = 0
    else:
        inner_x1 = 0
        inner_x2 = w-line_width

    if norm_y1 > norm_y2:
        inner_y1 = h-line_width
        inner_y2 = 0
    else:
        inner_y1 = 0
        inner_y2 = h-line_width

    shape = create_rect(w, h, apply_color=False)
    pg.draw.line(shape, c, (inner_x1, inner_y1), (inner_x2, inner_y2), line_width)
    screen.blit(shape, (min(norm_x1, norm_x2), min(norm_y1, norm_y2)))


def polygon(*points_):
    global c
    global screen

    lx = 10000000
    rx = -10000000
    uy = 10000000
    dy = -10000000

    points = []
    for point in points_:
        if isinstance(point, Point):
            x, y = point.as_tuple()
        elif isinstance(point, tuple):
            x, y = point
        else:
            return NotImplemented

        x, y = normalize_axis(x, y)

        lx = min(lx, x)
        rx = max(rx, x)

        uy = min(uy, y)
        dy = max(dy, y)

        points.append((x, y))

    for n in range(len(points)):
        x, y = points[n]
        points[n] = (x - lx + 1, y - uy + 1)

    w = rx - lx + 4
    h = dy - uy + 4

    shape = create_rect(w, h, apply_color=False)
    pg.draw.polygon(shape, c, points)
    screen.blit(shape, (lx, uy))


def ellipse(x, y, w, h, fill=True):
    global c
    global screen

    x, y = normalize_axis(x, y)

    shape = create_rect(w, h, apply_color=False)
    pg.draw.ellipse(shape, c, shape.get_rect(), not fill)
    draw_surface(shape, (x - w/2, y - h/2))


def rect(x: int, y: int, w: int, h: int):
    rectangle = create_rect(w, h)
    draw_image(rectangle, x, y, rectangle.get_width(), rectangle.get_height())


def draw_surface(surface: pg.Surface, pos):
    global screen

    if isinstance(pos, Point):
        pos = pos.as_tuple()
    elif not isinstance(pos, tuple):
        return NotImplemented

    screen.blit(surface, pos)


def rect_with_rot(center: Point, w: int, h: int, angle: float):
    global screen
    #print(center)

    pos = normalize_axis(center.x, center.y)
    #print(center)

    rectangle = create_rect(w, h)

    rotated_rectangle = rotate(rectangle, angle)

    drawing_box = rotated_rectangle.get_rect()
    drawing_box.center = pos

    screen.blit(rotated_rectangle, drawing_box)


def rotate(image: pg.Surface, angle: float) -> pg.Surface:
    rotated_image = pg.transform.rotate(image, angle)

    return rotated_image


def create_rect(w: int, h: int, apply_color=True) -> pg.Surface:
    global c
    global a

    rectangle = pg.Surface([w, h])
    rectangle.set_colorkey(BLACK)
    rectangle.set_alpha(a)
    if apply_color:
        rectangle.fill(c)

    return rectangle


def load_image(file_name: str) -> pg.Surface:
    image = pg.image.load(file_name)
    return image


def get_sprite(sheet: pg.Surface, x: int, y: int, sprite_width: int, sprite_height: int) -> pg.Surface:
    area = pg.Rect(x, y, sprite_width, sprite_height)
    sprite = sheet.subsurface(area)
    return sprite


def draw_image(image: pg.Surface, x: int, y: int, w: int, h: int):
    global screen

    x, y = normalize_axis(x, y)

    w = int(w)
    h = int(h)
    screen.blit(pg.transform.scale(image, (w, h)), (x, y))


def background(*rgb: int):
    global screen

    screen.fill(rgb)


def normalize_axis(x: float, y: float) -> tuple:
    global x_is_flipped
    global y_is_flipped

    new_x = x
    new_y = y

    if x_is_flipped:
        new_x = flip_x(x)
    if y_is_flipped:
        new_y = flip_y(y)

    return new_x, new_y


def flip_x(x: float) -> float:
    new_x = screen_width() - x
    return new_x


def flip_y(y: float) -> float:
    new_y = screen_height() - y
    return new_y


def update_display():
    global mouse

    mouse.update()
    pg.display.update()


def screen_width():
    global width
    return width


def screen_height():
    global height
    return height
