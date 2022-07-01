from mario import Mario
import pyxel


class Board:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h
        # This creates a Mario in the middle of the screen and at y = 200, facing right
        self.mario = Mario(self.width // 2, 100, 'left')

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.move('left', self.width)

    def draw(self):
        pyxel.cls(12)
        # Parameters are x, y,  image bank, staring x and y and the size and the colkey (chromakey)
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2],
                  self.mario.sprite[3], self.mario.sprite[4])
        pyxel.bltm(0, 0, 0, 0, 80, 23, 95, colkey=12)

