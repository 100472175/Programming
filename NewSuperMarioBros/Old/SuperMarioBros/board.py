import pyxel
from position import Position
from enemies import Enemy



class Board:
    player = Position(0, 0)
    def __init__(self):
        pyxel.load("assets/marioassets.pyxres")


    def update(self):
        e = Enemy()
        enemies_list = []
        enemies_list.append(e)
        while len(enemies_list) > 4:
            enemies_list.pop()
        for i in enemies_list:
            enemies_list[i].update

