import pyxel
from position import Position
from all_blocks import AllBlocks
import position

all_blocks = AllBlocks()


class Mario(Position):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.blocks_list = all_blocks.combined_list
        self.x = x
        self.y = y
        self.deltax = 0
        self.deltay = 0
        self.sprite = (0, 0, 48, 13, 16, 12)
        self.coins = 69
        self.score = 0
        self.lives = 3
        self.scroll_x = 0
        self.scroll_border = 0
        self.last_scroll_x = 0

    def update(self):

        if pyxel.btn(pyxel.KEY_LEFT):
            self.deltax = -2

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.deltax = 2

        self.deltay = min(self.deltay + 1, 3)

        if pyxel.btnp(pyxel.KEY_UP):
            for k in range(len(self.blocks_list)):
                if self.y + 16 == self.blocks_list[k][1]:
                    self.deltay = -12
            for b in range(len(self.blocks_list)):
                if self.y + 16 == self.blocks_list[b][1] or self.x + 16 == self.blocks_list[b][0]:
                    self.deltay = -12
            for c in self.blocks_list:
                if self.x + 16 == c[0] or self.y + 16 == c[1]:
                    self.deltay = -12

        if self.x < self.scroll_x:
            self.x = self.scroll_x

        if self.y < 0:
            self.y = 0

        self.deltax = int(self.deltax * 0.8)

        if self.x > self.scroll_x + self.scroll_border:
            self.last_scroll_x = self.scroll_x
            self.scroll_x = min(self.x - self.scroll_border, 248 * 8)

        if self.y > 300:
            self.game_ends()

        if self.lives == 0:
            pyxel.cls(0)
            pyxel.text(255 // 2, 255 // 2, "Game over :(", 7)

    def draw(self):
        pyxel.blt(self.x - self.scroll_x, self.y, *self.sprite)

    def game_ends(self):
        self.scroll_x = 0
        self.x = 20
        self.y = 10
        self.deltax = 0
        self.deltay = 0
        self.lives -= 1
