from blocks import Block


class BreakableBlock(Block):
    def __init__(self):

        super().__init__("coins", 0, 0)
        self.platform_list_of_isa = [(29 * 8, 23 * 8), (30 * 8, 23 * 8), (44 * 8, 15 * 8), (45 * 8, 15 * 8),
                                (202 * 8, 23 * 8),
                                (202 * 8, 23 * 8), (221 * 8, 15 * 8), (222 * 8, 15 * 8), (221 * 8, 23 * 8),
                                (222 * 8, 23 * 8),
                                (227 * 8, 23 * 8), (228 * 8, 23 * 8), (236 * 8, 29 * 8), (237 * 8, 29 * 8),
                                (238 * 8, 27 * 8),
                                (239 * 8, 27 * 8), (240 * 8, 25 * 8), (241 * 8, 25 * 8), (90 * 8, 23 * 8),
                                (91 * 8, 23 * 8)]

    # def broke_when_hit(self):  # funcion cuando mario toque los pixeles de abajo del bloque, el bloque desaparece
