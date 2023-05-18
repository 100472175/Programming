class Alumno:
    def __init__(self, name: str, surname: str, nia: int, nota1: float, nota2: float):
        self.name = name
        self.surname = surname
        self.nia = nia
        if nota2 <= 10:
            self.nota2 = nota2
        else:
            raise ValueError("Máximo 10")
        self.nota1 = nota1
        media = (nota1+nota2)/2
        self.media = media

    def __str__(self):
        return str(self.nia)

    def altupeso(self):
        sum= self.nota1*self.nota2
        return sum


student = Alumno("Niki","Navarro",100492132,7.6,2)
enemigo = Alumno("Juan", "Garvía", 1034, 10, 10)

print(student)
print(student.altupeso())
print(enemigo.altupeso())