import pyxel

import mario
from random import random
from enemies import Enemy
from mario import Mario
from all_blocks import AllBlocks

all_blocks = AllBlocks()


class Board:

    def __init__(self, x: int, y: int, fps: int):
        self.remaining_time = 0
        pyxel.init(x, y, title='Mario Brosh', fps=fps)
        pyxel.load("assets/marioassets.pyxres")
        pyxel.image(0).rect(48, 112, 16, 16, 12)
        # self.enemy = [(random.randint(8, 250), 200, random.randint(0, 2), True)]
        self.player = Mario(20, 10)
        self.blocks_list = all_blocks.combined_list

        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(-(self.player.scroll_x % 8), 0, 0, self.player.scroll_x // 8, 0, 40, 40)
        self.player.draw()

        pyxel.text(230, 4, str(self.remaining_time), 0)
        pyxel.text(100, 4, str(self.player.coins) + " coins", 0)
        pyxel.text(150, 4, 'Score: ' + str(self.player.score), 0)
        pyxel.text(1, 1, 'X coordinate: ' + str(self.player.x), 0)
        pyxel.text(1, 11, 'Y coordinate: ' + str(self.player.y), 0)
        pyxel.blt(95, 4, 0, 11, 232, 4, 6, 12)

    def get_tilemap(self, x, y):
        return pyxel.tilemap(0).pget(x, y)

    def check_tilemap_collision(self, x, y):
        x1 = x // 8
        y1 = y // 8

        x2 = (x + self.player.sprite[3] - 1) // 8
        y2 = (y + self.player.sprite[4] - 1) // 8

        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                for k in range(len(self.blocks_list)):
                    if self.get_tilemap(j, i) == self.blocks_list[k]:
                        return True
        return False

    def react_on_collision(self, x, y, deltax, deltay):
        abs_deltax = abs(deltax)
        abs_deltay = abs(deltay)

        if abs_deltax > abs_deltay:
            sign = 1 if deltax > 0 else -1
            for i in range(abs_deltax):
                if not self.check_tilemap_collision(x + sign, y):
                    x += sign

            sign = 1 if deltay > 0 else -1
            for i in range(abs_deltay):
                if not self.check_tilemap_collision(x, y + sign):
                    y += sign

        else:
            sign = 1 if deltay > 0 else -1
            for i in range(abs_deltay):
                if not self.check_tilemap_collision(x, y + sign):
                    y += sign

            sign = 1 if deltax > 0 else -1
            for i in range(abs_deltax):
                if not self.check_tilemap_collision(x + sign, y):
                    x += sign

        return x, y, deltax, deltay

    def update(self):
        self.player.update()

        if pyxel.btnp(pyxel.KEY_SHIFT):
            pyxel.quit()
        self.remaining_time = 300 - pyxel.frame_count // 60

        if self.remaining_time == 0:
            self.player.game_ends()

        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.deltax = -2

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.deltax = 2

        self.player.deltay = min(self.player.deltay + 1, 3)

        if pyxel.btnp(pyxel.KEY_UP):
            for k in range(len(self.blocks_list)):
                if self.player.y + 16 == self.blocks_list[k][1]:
                    self.player.deltay = -12
            for b in range(len(self.blocks_list)):
                if self.player.y + 16 == self.blocks_list[b][1] and \
                        self.player.x + 16 == self.blocks_list[b][0]:
                    self.player.deltay = -12

        self.player.x, self.player.y, self.player.deltax, self.player.deltay = \
            self.react_on_collision(self.player.x, self.player.y, self.player.deltax, self.player.deltay)

        if self.player.x < self.player.scroll_x:
            self.player.x = self.player.scroll_x

        if self.player.y < 0:
            self.player.y = 0

        self.player.deltax = int(self.player.deltax * 0.8)

        if self.player.x > self.player.scroll_x + self.player.scroll_border:
            self.player.last_scroll_x = self.player.scroll_x
            self.player.scroll_x = min(self.player.x - self.player.scroll_border, 248 * 8)

        if self.player.y > 300:
            self.player.game_ends()
