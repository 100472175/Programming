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
        # direction of mario in the x-axis and how much pyxels the player wants to move in that direction
        self.deltax = 0
        # direction of mario in the y-axis and how much pyxels the player wants to move in that direction
        self.deltay = 0
        # image bank, position x in image bank, position y in image bank, width, height, color of the background
        self.sprite = (0, 0, 48, 13, 16, 12)
        self.coins = 0
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

    # We have to update the size of Mario, the presence of mushrooms and coins and check if Mario is colliding
    # with blocks:
    def update(self):
        if self.big:
            self.width = 16
            self.height = 32
        if not self.big:
            self.width = 13
            self.height = 16

        self.grow_with_mushroom()

        self.pick_coin()
        self.kikblock(self.x, self.y)

    # We have to draw Mario with its different directions and sizes:
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

    # With this function we check Mario is colliding with any block and what item that block contains so that
    # the program knows what to do depending on the type of the block:
    def kikblock(self, x: int, y: int):
        for i in self.question_block_list:
            # If Mario is big the breakable blocks are removed from the block list when kicked:
            if self.big:
                if abs(x - i.x) < 10 and y - 16 == i.x and i.container == "nothing":
                    self.question_block_list.remove(i)

            # When Mario kicks a question block a new object (coin or mushroom) is created and the sprite of the block
            # changes as well as its content:
            if abs(self.x - i.x) < 10 and self.y - 16 == i.x:
                if i.container == "coin":
                    i.container = "nothing"
                    coin1 = Coin(i.x, i.y - 16)
                    self.coin_list.append(coin1)
                if i.container == "mushroom":
                    i.container = "nothing"
                    mushroom1 = Mushroom(i.x, i.y - 16)
                    self.mushroom_list.append(mushroom1)

    # Mario will grow when touching a mushroom, the score will increase and the mushroom will be removed:
    def grow_with_mushroom(self):
        for i in self.mushroom_list:
            if (self.x - i.x) < 10 and self.y == i.y:
                self.big = True
                self.sprite = (0, 72, 48, 13, 16, 12)
                self.y -= 16
                self.score += 200
                self.mushroom_list.remove(i)

    # When Mario touches a coin, the score and the coin counter will increase and the coin will be removed:
    def pick_coin(self):
        for i in self.coin_list:
            if abs(self.x - i.x) < 10 and self.y == i.y:
                self.coins += 1
                self.coin_list.remove(i)
                self.score += 200

    # If Mario is touching a block from bellow he will collides with it:
    def collisions_with_blocks(self):
        for i in self.question_block_list:
            if abs(self.x - i.x) < 10 and self.y == i.y + 16:
                self.deltay = 0
            elif abs(self.x - i.x) < 10 and self.y == i.y - 1:
                self.deltay = 0
