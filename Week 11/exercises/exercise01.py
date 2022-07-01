"""Create the Student class, which represents a first year student. Its fields will be: name, surname, programming
 mark, algebra mark, calculus mark, physics mark, skills mark and humanities mark. Create an init method that receives
 values for all the fields and checks that the values for the marks are in the right range (if not, a zero will be
 assigned to the mark). Write a program that creates an object of this type, fills the fields asking the user by
 keyboard and prints them."""


class Student:
    def __init__(self, name: str, surname: str, programming: float, algebra: float, calculus: float, physics: float,
                 skills: float, humanities: float):
        self.name = name
        self.surname = surname
        self.programming = programming
        self.algebra = algebra
        self.calculus = calculus
        self.physics = physics
        self.skills = skills
        self.humanities = humanities

        @property
        def programming(self):
            return self.__programming

        @programming.setter
        def programming(self, programming: float):
            if type(programming) == float:
                self.__programming = programming
                if programming <= 0 or programming > 10:
                    self.__programming = 0
            else:
                raise TypeError("Programming has an incorrect type")

        @property
        def algebra(self):
            return self.__algebra

        @algebra.setter
        def algebra(self, algebra: float):
            if type(algebra) == float:
                self.__algebra = algebra
                if algebra <= 0 or algebra > 10:
                    self.__algebra = 0
            else:
                raise TypeError("Algebra has an incorrect type")

        @property
        def calculus(self):
            return self.__calculus

        @calculus.setter
        def calculus(self, calculus: float):
            if type(calculus) == float:
                self.__calculus = calculus
                if calculus <= 0 or calculus > 10:
                    self.__calculus = 0
            else:
                raise TypeError("Calculus has an incorrect type")

        @property
        def physics(self):
            return self.__physics

        @physics.setter
        def physics(self, physics: float):
            if type(physics) == float:
                self.__physics = physics
                if physics <= 0 or physics > 10:
                    self.__physics = 0
            else:
                raise TypeError("Physics has an incorrect type")

        @property
        def skills(self):
            return self.__skills

        @skills.setter
        def skills(self, skills: float):
            if type(skills) == float:
                self.__skills = skills
                if skills <= 0 or skills > 10:
                    self.__skills = 0
            else:
                raise TypeError("Skills has an incorrect type")

        @property
        def humanities(self):
            return self.__humanities

        @humanities.setter
        def humanities(self, humanities: float):
            if type(humanities) == float:
                self.__humanities = humanities
                if humanities <= 0 or humanities > 10:
                    self.__humanities = 0
            else:
                raise TypeError("Humanities has an incorrect type")

        def __repr__(self):
            return self.name + ', ' + self.surname + ', ' + str(self.programming) + ', ' + str(self.algebra) + ', ' + \
                   str(self.calculus) + ', ' + str(self.physics) + ', ' + str(self.skills) + ', ' + str(self.humanities)

        def __str__(self):
            return self.name + ', ' + self.surname + ', ' + str(self.programming) + ', ' + str(self.algebra) + ', ' + \
                   str(self.calculus) + ', ' + str(self.physics) + ', ' + str(self.skills) + ', ' + str(self.humanities)

        def fprint(self):
            print(self.name + ', ' + self.surname + ', ' + str(self.programming) + ', ' + str(self.algebra) + ', ' + \
                  str(self.calculus) + ', ' + str(self.physics) + ', ' + str(self.skills) + ', ' + str(self.humanities))

        def print(self) -> str:
            return self.name + ', ' + self.surname + ', ' + str(self.programming) + ', ' + str(self.algebra) + ', ' + \
                   str(self.calculus) + ', ' + str(self.physics) + ', ' + str(self.skills) + ', ' + str(self.humanities)


n = input('What is your name? ')
s = input('What is your surname? ')
pr = float(input('What was your grade in programming? '))
al = float(input('What was your grade in algebra? '))
ca = float(input('What was your grade in calculus? '))
ph = float(input('What was your grade in physics? '))
sk = float(input('What was your grade in skills? '))
hu = float(input('What was your grade in humanities? '))

result = Student(n, s, pr, al, ca, ph, sk, hu)
print(result)
result.print()
