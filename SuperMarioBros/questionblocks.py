from blocks import Block


class QuestionBlock(Block):

    def __init__(self, container: str, x, y):
        super().__init__(x, y)
        self.platform_list = ((29, 23), (44, 15))
        self.contain = container

#    def itemwhenhitted(self):  # funcion para que aparezca moneda/seta/estrella cuando mario lo pulsa


#    def changeappereance(self): #funcion para que el bloque se vuelva marron cuando mario lo pulsa
