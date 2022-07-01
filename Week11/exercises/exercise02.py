import math

class RightTriangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

        @property
        def base(self):
            return self.__base
        @base.setter
        def base(self, base: float):
            if type(base) == float:
                self.__base = base
                if base <= 0:
                    self.__base = 1
            else:
                raise TypeError('The base is not accepted as the type is not correct, needed float')

        @property
        def height(self):
            return self.__base

        @base.setter
        def base(self, base: int):
            if type(base) == float:
                self.height = height
                if height <= 0:
                    self.height = 1
            else:
                raise TypeError('The height is not accepted as the type is not correct, needed float')

        def perimeter(self):
            h = (base**2 + height**2)**(1/2)
            return str(base+height+h)

        def area(self):
            return str(base*height/2)

b = float(input('Base: '))
h = float(input('Height: '))
a = input("What do you want to calculate: the perimeter(1) or the area(2)?")
patata = RightTriangle(b, h)
patata.height = h
patata.base = b

print(patata)
patata.perimeter()

if a == 1:
    patata.perimeter()
    print(patata)
elif a == 2:
    patata.area()
