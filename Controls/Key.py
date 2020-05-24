registered_keys = []


class Key:
    def __init__(self, code: int):
        self.code = code

        self.pressed = False
        self.name = ""

        self.function = self.default_function

    def press(self):
        self.pressed = True

    def release(self):
        self.pressed = False

    def equals(self, code: int):
        return self.code == code

    def __eq__(self, other) -> bool:
        if isinstance(other, Key):
            ans = self.equals(other.code)
        else:
            ans = NotImplemented
        return ans

    def default_function(self):
        print("Key", self.name, "with code", self.code, "is pressed")

    def __getstate__(self):
        return self.code

    def __int__(self):
        return self.code

    def __float__(self):
        return self.code

    def __getitem__(self, index):
        return self.registered_keys[index]

    def __contains__(self, item):
        return item in self.registered_keys

    @classmethod
    def a(cls):
        global registered_keys

        key = Key(97)
        key.name = "a"
        registered_keys.append(key)
        return key

    @classmethod
    def d(cls):
        global registered_keys

        key = Key(100)
        key.name = "d"
        registered_keys.append(key)
        return key

    @classmethod
    def s(cls):
        global registered_keys

        key = Key(115)
        key.name = "s"
        registered_keys.append(key)
        return key

    @classmethod
    def w(cls):
        global registered_keys

        key = Key(119)
        key.name = "w"
        registered_keys.append(key)
        return key

    @classmethod
    def left_arrow(cls):
        global registered_keys

        key = Key(276)
        key.name = "left arrow"
        registered_keys.append(key)
        return key

    @classmethod
    def right_arrow(cls):
        global registered_keys

        key = Key(275)
        key.name = "right arrow"
        registered_keys.append(key)
        return key

    @classmethod
    def up_arrow(cls):
        global registered_keys

        key = Key(273)
        key.name = "up arrow"
        registered_keys.append(key)
        return key

    @classmethod
    def down_arrow(cls):
        global registered_keys

        key = Key(274)
        key.name = "down arrow"
        registered_keys.append(key)
        return key

    @classmethod
    def space(cls):
        global registered_keys

        key = Key(32)
        key.name = "space"
        registered_keys.append(key)
        return key

    @classmethod
    def r(cls):
        global registered_keys

        key = Key(114)
        key.name = "r"
        registered_keys.append(key)
        return key

    @classmethod
    def j(cls):
        global registered_keys

        key = Key(106)
        key.name = "j"
        registered_keys.append(key)
        return key

    @classmethod
    def u(cls):
        global registered_keys

        key = Key(117)
        key.name = "u"
        registered_keys.append(key)
        return key

    @classmethod
    def k(cls):
        global registered_keys

        key = Key(107)
        key.name = "k"
        registered_keys.append(key)
        return key

    @classmethod
    def i(cls):
        global registered_keys

        key = Key(105)
        key.name = "i"
        registered_keys.append(key)
        return key

    @classmethod
    def get_default_press_control_function(cls, keys: list):
        def on_press(code: int):
            pressed_key = Key(code)
            for key in keys:
                if pressed_key == key:
                    key.press()
                    break

        return on_press

    @classmethod
    def get_default_release_control_function(cls, keys: list):
        def on_release(code: int):
            released_key = Key(code)
            for key in keys:
                if released_key == key:
                    key.release()
                    break

        return on_release


A = Key.a()
S = Key.s()
D = Key.d()
W = Key.w()

R = Key.r()

J = Key.j()
U = Key.u()
K = Key.k()
I = Key.i()

RIGHT_ARROW = Key.right_arrow()
LEFT_ARROW = Key.left_arrow()
UP_ARROW = Key.up_arrow()
DOWN_ARROW = Key.down_arrow()

SPACE = Key.space()
