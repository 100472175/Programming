#Metemos un parametro que sea un indicador de que sprite queremos utilizar
import pyxel
from position import Position
import random
class Enemy(Position):
    def __init__(self, x, y, alive): #The type will be goompa or koopa troopa
        super().__init__(x, y)
        self.x = x
        self.y = y
        alive = True
        num = random.randint(0,4)
        if num == 0:
            self.type = "Koopa Troopa"
        else:
            self.type = "Goompa"
    '''def die: #si los pies de mario tocan la cabeza del enemigo, el enemigo desaparece
        if '''
    def draw(self):
        if type == "Koopa Troopa":
            # pyxel.blt( where it is being drawn x coordinate and y coordinate, the image bank, the position of the
            # sprite in the image, x and y, the width, the height, and the colour of the background to be removed and
            # turned into png format
            pyxel.blt(self.x, self.y, 0, 48, 32, 16, 24, 12)
        else:
            pyxel.blt(self.x, self.y, 0, 32, 48, 16, 16, 12)

