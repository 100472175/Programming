import pyxel
from mario import Mario
import random


class Mario:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.w = 16  # Width
        self.h = 16  # Height

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 48, self.w, self.h, colkey=6)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class App:
    def __init__(self):
        pyxel.init(192, 128, scale=4, caption="NIBBLES", fps=60)
        pyxel.load("assets/marioassets.pyxres")
        self.mario = Mario(16, 16)
        pyxel.run(self.draw)

    def draw(self):
        pyxel.cls(1)
        self.mario.draw()

    def move_mario(self):
        new_x = random.randrange(8, 184, 8)  # From where, to where (192-8), jumps
        new_y = random.randrange(8, 120, 8)
        good_position = True
