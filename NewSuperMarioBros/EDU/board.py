import random
import pyxel

from mario import Mario
from blocks import Blocks
from mushrooms import Mushroom
from question_blocks import QuestionBlocks


class Board:
    def __init__(self, x: int, y: int, fps: int):
        self.remaining_time = 0
        pyxel.init(x, y, title='EDU New Super Mario Bros', fps=fps)
        pyxel.load("assets/marioassets.pyxres")
        pyxel.image(0).rect(48, 112, 16, 16, 12)
        self.scroll_border = 80
        self.player = Mario(20, 10)
        self.blocks = Blocks()
        pyxel.run(self.update, self.draw)
        self.x = x
        self.y = y

    def get_tilemap(self, x, y):
        return pyxel.tilemap(0).pget(x, y)

    def check_tilemap_collision(self, x, y):
        x1 = x // 8
        y1 = y // 8
        x2 = (x + self.player.width - 1) // 8
        y2 = (y + self.player.height - 1) // 8
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                for k in range(len(self.player.col_tiles)):
                    if self.get_tilemap(j, i) == self.player.col_tiles[k]:
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

    # def react_on_collision_ojects:


    def game_ends(self):
        self.player.scroll_x = 0
        self.player.x = 20
        self.player.y = 10
        self.player.deltax = 0
        self.player.deltay = 0
        self.player.lives -= 1

    def draw(self):
        if self.player.lives > 0 and self.player.x < 2000:
            pyxel.cls(12)
            pyxel.bltm(-(self.player.scroll_x % 8), 0, 0, self.player.scroll_x // 8, 0, 40, 40)
            self.player.draw()

            pyxel.text(230, 4, str(self.remaining_time), 0)
            pyxel.text(100, 4, str(self.player.coins) + " coins", 0)
            pyxel.blt(95, 4, 0, 11, 232, 4, 6, 12)
            pyxel.text(140, 4, 'Score: ' + str(self.player.score), 0)
            pyxel.text(1, 1, 'X coordinate: ' + str(self.player.x), 0)
            pyxel.text(1, 11, 'Y coordinate: ' + str(self.player.y), 0)
            pyxel.text(190, 4, 'Lives: ' + str(self.player.lives), 0)
            pyxel.blt(180, 4, 0, 17, 232, 7, 8, 12)

            for i in self.player.question_block_list:
                pyxel.blt(i.x - self.player.scroll_x, i.y, *i.sprite)

            for i in self.player.coin_list:
                pyxel.blt(i.x - self.player.scroll_x, i.y, *i.sprite)

            for i in self.player.mushroom_list:
                pyxel.blt(i.x, i.y, *i.sprite)



        elif self.player.x > 2000:
            pyxel.cls(0)
            pyxel.text(255 // 3, 255 // 2, "You win, congratulations <3 \n :D ", 7)
        else:
            pyxel.cls(0)
            pyxel.text(255 // 2.5, 255 // 2, "Game over :(", 7)

    def mario_grows(self):
        if self.player.x > 400:
            self.player.big = True

    def update(self):
        if pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_SHIFT):
            pyxel.quit()

        # Mario's update
        if pyxel.btn(pyxel.KEY_A):
            self.player.deltax = -2

        if pyxel.btn(pyxel.KEY_D):
            self.player.deltax = 2

        self.player.deltay = min(self.player.deltay + 1, 3)

        if self.player.x > 400:
            self.player.big = True

        # Detect if mario hits a block
        self.player.kikblock()

        self.player.grow_with_mushroom()

        self.player.update()

        # Used to debug and be a ble to jump freely on the map to test the different collisions and speeds
        if pyxel.btnp(pyxel.KEY_UP):
                self.player.deltay = -12

        if pyxel.btnp(pyxel.KEY_W):
            for k in self.blocks.floor_list:
                if self.player.y + 16 == k.x:
                    self.player.deltay = -12
            for b in self.blocks.platform_list:
                if self.player.x + 16 == b.x and self.player.y + 16 == b.y:
                    self.player.deltay = -12
            for c in self.blocks.pipes_list:
                if self.player.x + 16 == c.x and self.player.y + 16 == c.x:
                    self.player.deltay = -12

        self.player.x, self.player.y, self.player.deltax, self.player.deltay = \
            self.react_on_collision(self.player.x, self.player.y, self.player.deltax, self.player.deltay)

        if self.player.x < self.player.scroll_x:
            self.player.x = self.player.scroll_x

        if self.player.y < 0:
            self.player.y = 0

        self.player.deltax = int(self.player.deltax * 0.8)

        if self.player.x > self.player.scroll_x + self.scroll_border:
            self.player.scroll_x = min(self.player.x - self.scroll_border, 248 * 8)

        # Deaths and time

        self.remaining_time = 300 - pyxel.frame_count // 60

        if self.player.y > 300:
            self.game_ends()

