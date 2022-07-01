import pyxel
from blocks import Blocks
from coins import Coin
from mushrooms import Mushroom


class Mario:
    def __init__(self, x, y):
        blocks = Blocks()
        self.pfp_list = blocks.pfp_list
        self.col_tiles = blocks.col_tiles
        self.x = x
        self.y = y
        self.deltax = 0
        self.deltay = 0
        self.sprite = (0, 0, 48, 13, 16, 12)
        self.coins = 69
        self.score = 0
        self.lives = 3
        self.scroll_x = 0
        self.width = 13
        self.height = 16
        self.big = False
        self.blocks = Blocks
        self.coin_list = []
        self.mushroom_list = []
        self.question_block_list = blocks.question_block_list

    def update(self):
        if self.big:
            self.width = 16
            self.height = 32
        if not self.big:
            self.width = 13
            self.height = 16

        self.grow_with_mushroom()

        self.pick_coin()
        self.kikblock()

    def draw(self):
        if not self.big:
            if self.deltax < 0:
                # Small mario facing left
                pyxel.blt(self.x - self.scroll_x, self.y, 0, 0, 48, -13, 16, 12)
            else:
                # Small mario facing right
                pyxel.blt(self.x - self.scroll_x, self.y, 0, 0, 48, 13, 16, 12)
        else:
            if self.deltax < 0:
                # Big mario facing left
                pyxel.blt(self.x - self.scroll_x, self.y, 0, 0, 72, -16, 32, 12)
            else:
                # Big mario facing right
                pyxel.blt(self.x - self.scroll_x, self.y, 0, 0, 72, 16, 32, 12)

    def grow_with_mushroom(self, x, y):
        pass

    def draw_mushroom(self):
        self.drawmushroom = True
        return self.drawmushroom

    def draw_coin(self):
        self.drawcoin = True
        return self.drawcoin

    def kikblock(self):
        for i in self.question_block_list:
            if self.big:
                if abs(self.x - i.x) < 10 and self.y - 16 == i.x and i.container == "nothing":
                    self.question_block_list.remove(i)

            if abs(self.x - i.x) < 10 and self.y - 16 == i.x:
                if i.container == "coin":
                    i.sprite = (0, 16, 16, 16, 16, 12)
                    coin1 = Coin(i.x, i.y - 16)
                    self.coin_list.append(coin1)

            if abs(self.x - i.x) < 10 and self.y - 16 == i.x:
                if i.container == "mushroom":
                    i.sprite = (0, 16, 16, 16, 16, 12)
                    mushroom1 = Mushroom(i.x, i.y - 16)
                    self.mushroom_list.append(mushroom1)

    def grow_with_mushroom(self):
        for i in self.mushroom_list:
            if (self.x - i.x) < 10 and self.y == i.y:
                self.big = True
                self.sprite = (0, 72, 48, 13, 16, 12)
                self.y -= 16
                self.score += 200
                return True

    def pick_coin(self):
        for i in self.coin_list:
            if abs(self.x - i.x) < 10 and self.y == i.y:
                self.coins += 1
                self.coin_list.remove(i)
                self.score += 200

