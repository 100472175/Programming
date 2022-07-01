class Student:
    def __init__(self, name: str, surname: str, age: int):
        """

        :param name:
        :param surname:
        :param age:
        """
        self.name = name
        self.surname = surname
        self.age = age

    def print_student(self):
        if self.age >= 18:
            return self.name + ', ' + self.surname + ', ' + str(self.age) + ', Can drink'
        else:
            return self.name + ', ' + self.surname + ', ' + str(self.age) + ", Can't drink"
