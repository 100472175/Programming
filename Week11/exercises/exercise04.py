import pyxel


class Position:
    def __init__(self, x: int, y: int, dirx: int, diry: int):
        self.x = x
        self.y = y
        self.dirx = dirx
        self.diry = diry

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        if type(x) == int:
            self.__x = x
        else:
            raise TypeError("X has an incorrect type")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        if type(y) == int:
            self.__y = y
        else:
            raise TypeError("Y has an incorrect type")

    @property
    def dirx(self):
        return self.__dirx

    @dirx.setter
    def dirx(self, dirx: int):
        if type(dirx) == int:
            self.__dirx = dirx
        else:
            raise TypeError("dirX has an incorrect type")

    @property
    def diry(self):
        return self.__diry

    @diry.setter
    def diry(self, diry: int):
        if type(diry) == int:
            self.__diry = diry
        else:
            raise TypeError("dirY has an incorrect type")


class Block:
    def __init__(self, x: int, y: int):
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
            raise TypeError("X type is not valid, must be int")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        if type(y) == int:
            self.__y = y
        else:
            raise TypeError("Y type is not valid, must be int")


class Mario(Position):
    def __init__(self, x: int, y: int, dirx: int, diry: int, size: str):
        super().__init__(x, y, dirx, diry)

        self.x = x
        self.y = y
        self.dirx = dirx
        self.diry = diry
        self.size = size
        self.__sprite = (0, 0, 48, 13, 16, 12)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        if type(x) == int:
            self.__x = x
        else:
            raise TypeError("Mario’s x coordinate was given in an incorrect value")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        if type(y) == int:
            self.__y = y
        else:
            raise TypeError("Mario's y coordinate was given in an incorrect value")

    @property
    def dirx(self):
        return self.__dirx

    @dirx.setter
    def dirx(self, dirx: str):
        if type(dirx) == str:
            self.__dirx = dirx
        else:
            raise TypeError("The value entered for the x direction is not an integer")

    @property
    def diry(self):
        return self.__diry

    @dirx.setter
    def diry(self, diry: str):
        if type(diry) == str:
            self.__dirx = diry
        else:
            raise TypeError("The value entered for the y direction is not an integer")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        if type(size) == str:
            self.__size = size
        else:
            raise TypeError("The value entered for the size is incorrect")

    @diry.setter
    def diry(self, value):
        self._diry = value

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def sprite(self):
        return self.__sprite


class Goomba(Position):
    def __init__(self, x: int, y: int, dirx: int, diry: int):
        super().__init__(x, y, dirx, diry)
        self.sprite = (0, 32, 48, 16, 16, 12)


class Mushroom(Position):
    def __init__(self, x: int, y: int, dirx: int, diry: int):
        super().__init__(x, y, dirx, diry)
        self.sprite = (0, 0, 32, 16, 16, 12)


class BreakableBlocks(Position):
    def __init__(self, x: int, y: int, broken: bool):
        super().__init__(x, y, )
        self.sprite = (0, 0, 16, 16, 16)


class UnbreakableBlocks(Position):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.sprite = (0, 32, 104, 16, 16)


class QuestionBlocks(Position):
    def __init__(self, x: int, y: int, contain: str):
        super().__init__(x, y)
        self.sprite = (0, 16, 0, 16, 16)
        self.contain = contain


class ClearBlocks(Position):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.sprite = (0, 0, 0, 16, 16)


class Floor(Position):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.sprite = (0, 32, 104, 16, 16)


class Pipes(Position):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.sprite = (0, 32, 0, 31, 31)


class FireFlower(Position):
    def __init__(self, x: int, y: int, dirx: int, diry: int):
        super().__init__(x, y, dirx, diry)
        self.sprite = (0, 16, 32, 16, 16, 12)


class Star(Position):
    def __init__(self, x: int, y: int, dirx: int, diry: int):
        super().__init__(x, y, dirx, diry)
        self.sprite = (0, 32, 32, 16, 16, 12)


class KoopaTroopa(Position):
    def __init__(self, x: int, y: int, dirx: int, diry: int, size: str):
        super().__init__(x, y, dirx, diry)
        self.sprite = (0, 48, 32, 24, 16, 12)
        self.size = size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, size: str):
            if type(size) == str:
                self.__size = size
            else:
                raise TypeError("The type for the size of the KoopaTroopa is not correct. Must be a string")


