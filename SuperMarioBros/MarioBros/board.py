from mario import Mario
import pyxel


class Board:
    """ This class contains all the information needed to represent the
    board"""

    def __init__(self, w: int, h: int):
        """ The parameters are the width and height of the board"""
        self.width = w
        self.height = h
        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(self.width // 2, 200, True)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.move('left', self.width)
        elif pyxel.btn(pyxel.KEY_UP):
            self.mario.move('up', self.height)
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.mario.move('down', self.height)

    def draw(self):
        pyxel.cls(0)
        # We draw Mario taking the values from the mario object
        # Parameters are x, y, image bank, the starting x and y and the size

        # The second to last is how much x of the tile-map draws
        # The last one is how much of the y of the tile-map draws
        pyxel.bltm(0, 0, 0, 0, 16, 32, 32)

        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4], colkey=self.mario.sprite[5])
