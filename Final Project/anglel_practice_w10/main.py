import pyxel
from board import Board


board = Board(165, 120)
pyxel.init(board.width, board.height, caption='Is this you Mario???', fps=60)
pyxel.load("assets/marioassets.pyxres")
pyxel.run(board.update(), board.draw())
