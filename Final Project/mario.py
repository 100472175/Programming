import pyxel


class Mario:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.w = 16  # Width
        self.h = 16  # Height

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 48, self.w, self.h, colkey=6)

