
class QuestionBlocks:
    def __init__(self, x: int, y: int, container="nothing", kicked=False):
        self.x = x
        self.y = y
        self.container = container
        self.kicked = kicked

        if container == "nothing":
            self.sprite = (0, 16, 0, 16, 16)
        elif container == "coin" or container == "mushroom":
            self.sprite = (0, 16, 16, 16, 16)
        else:
            self.sprite = (0, 0, 16, 16, 16)


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        if type(x) == int:
            self.__x = x
        else:
            raise TypeError("X's type is not valid, must be int")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        if type(y) == int:
            self.__y = y
        else:
            raise TypeError("Y's type is not valid, must be int")

    @property
    def container(self):
        return self.__x

    @container.setter
    def container(self, container: str):
        if type(container) == str:
            self.__container = container
        else:
            raise TypeError("Container's type is not valid, must be a string")


