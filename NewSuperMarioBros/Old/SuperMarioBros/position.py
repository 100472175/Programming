import pyxel


class Position:
    def __init__(self, x: int, y: int):
        pyxel.load("assets/marioassets.pyxress")
        self.x = x
        self.y = y
        

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        if type(x) == int:
            self.__x = x
        else:
            raise TypeError("X has an incorrect type, must be an integer")

    @property
    def y(self):
        return self.__x

    @y.setter
    def y(self, y: int):
        if type(y) == int:
            self.__y = y
        else:
            raise TypeError("Y has an incorrect type, must be an integer")

    def check_tilemap_collision(x, y, deltax, deltay, collisionable: list):
        x1 = x // 8
        y1 = y // 8
        x2 = (x + 12 - 1) // 8
        y2 = (y + 16 - 1) // 8

        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                for k in range(len(collisionable)):
                    if pyxel.tilemap(0).pget(j, i) == collisionable[k]:
                        return True
        return False

    def react_on_collision(self, x, y, deltax, deltay):
        abs_deltax = abs(deltax)
        abs_deltay = abs(deltay)

        if abs_deltax > abs_deltay:
            sign = 1 if deltax > 0 else -1
            for i in range(abs_deltax):
                if not self.check_tilemap_collision(x + sign, y, deltax, deltay):
                    x += sign

            sign = 1 if deltay > 0 else -1
            for i in range(abs_deltay):
                if not self.check_tilemap_collision(x, y + sign, deltax, deltay):
                    y += sign

        else:
            sign = 1 if deltay > 0 else -1
            for i in range(abs_deltay):
                if not self.check_tilemap_collision(x, y + sign, deltax, deltay):
                    y += sign

            sign = 1 if deltax > 0 else -1
            for i in range(abs_deltax):
                if not self.check_tilemap_collision(x + sign, y, deltax, deltay):
                    x += sign

        return x, y, deltax, deltay
