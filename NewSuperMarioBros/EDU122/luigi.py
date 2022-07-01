import pyxel
from blocks import Blocks
from coins import Coin
from mushrooms import Mushroom


class Luigi:
    def __init__(self, x, y):
        blocks = Blocks()
        self.pfp_list = blocks.pfp_list
        self.col_tiles = blocks.col_tiles
        self.x = x
        self.y = y
        # direction of Liugi in the x-axis and how much pyxels the player wants to move in that direction
        self.deltax = 0
        # direction of Liugi in the y-axis and how much pyxels the player wants to move in that direction
        self.deltay = 0
        # image bank, position x in image bank, position y in image bank, width, height, color of the background
        self.sprite = (0, 64, 80, 16, 16, 12)
        self.coins = 0
        self.score = 0
        self.lives = 3
        self.scroll_x = 0
        self.width = 13
        self.height = 16
        self.big = False
        self.blocks = Blocks
        self.coins_list = []
        self.mushroom_list = []
        self.question_block_list = blocks.question_block_list

    # We have to update the size of Liugi, the presence of mushrooms and coins and check if Liugi is colliding
    # with blocks:
    def update(self):
        if self.big:
            self.width = 16
            self.height = 32
        if not self.big:
            self.width = 16
            self.height = 16

        self.grow_with_mushroom_l()

        # self.pick_coin(self.x, self.y)
        self.kikblock_l(self.x, self.y)

    # We have to draw Liugi with its different directions and sizes:
    def draw(self):
        if not self.big:
            if self.deltax < 0:
                # Small Liugi facing left
                pyxel.blt(self.x - self.scroll_x, self.y, 0, 64, 80, -16, 16, 12)
            else:
                # Small Liugi facing right
                pyxel.blt(self.x - self.scroll_x, self.y, 0, 64, 80, 16, 16, 12)
        else:
            if self.deltax < 0:
                # Big Liugi facing left
                pyxel.blt(self.x - self.scroll_x, self.y, 0, 64, 80, -16, 32, 12)
            else:
                # Big Liugi facing right
                pyxel.blt(self.x - self.scroll_x, self.y, 0, 64, 80, 16, 32, 12)

    # With this function we check Liugi is colliding with any block and what item that block contains so that
    # the program knows what to do depending on the type of the block:
    def kikblock_l(self, x: int, y: int):
        for i in self.question_block_list:
            # If Liugi is big the breakable blocks are removed from the block list when kicked:
            if self.big:
                if abs(x - i.x) < 16 and abs(y - i.y) < 10 and i.container == "nothing":
                    self.question_block_list.remove(i)
                    self.coins_list.append(Coin(i.x, i.y + 16))
                    self.y += 8

            # When Liugi kicks a question block a new object (coin or mushroom) is created and the sprite of the block
            # changes as well as its content:
            if abs(self.x - i.x) < 10 and abs(self.y - 16 - i.y) < 10:
                if i.container == "coin":
                    i.container = "empty"
                    coin1 = Coin(i.x, i.y - 16)
                    self.coins_list.append(Coin(x, y + 16))
                elif i.container == "mushroom":
                    i.container = 'empty'
                    i.sprite = (0, 16, 16, 16, 16)
                    mushroom1 = Mushroom(i.x, i.y - 16)
                    self.mushroom_list.append(mushroom1)

    # Liugi will grow when touching a mushroom, the score will increase and the mushroom will be removed:
    def grow_with_mushroom_l(self):
        for i in self.mushroom_list:
            if (self.x - i.x) < 10 and (self.y - i.y) < 10:
                self.big = True
                self.sprite = (0, 72, 48, 13, 16, 12)
                self.y -= 16
                self.score += 200
                self.mushroom_list.remove(i)

    def decrease_with_enemy_l(self):
        if self.big:
            self.big = False
            self.sprite = (0, 0, 48, 13, 16, 12)
        else:
            return False

    # When Liugi touches a coin, the score and the coin counter will increase and the coin will be removed:
    def pick_coin_l(self, x: int, y: int):
        for i in self.coins_list:
            if abs(x - i.x) < 10 and abs(y - i.y) < 10:
                self.coins += 1
                self.coins_list.remove(i)
                self.score += 200

    # If Liugi is touching a block from bellow he will collides with it:
    def collisions_with_blocks_l(self):
        for i in self.question_block_list:
            if abs(self.x - i.x) < 8 and (i.y - self.y) < 6 and self.big:
                self.deltay = 0
            elif abs(self.x - i.x) < 8 and (i.y - self.y) < 24:
                self.deltay = 0
