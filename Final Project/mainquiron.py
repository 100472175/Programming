import pyxel

position = [10, 10]


def move(x, y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if x < 144:
            x += 1
    elif pyxel.btn(pyxel.KEY_LEFT):
        if x > 0:
            x -= 1
    elif pyxel.btn(pyxel.KEY_UP):
        if y > 0:
            y -= 1
    elif pyxel.btn(pyxel.KEY_DOWN):
        if y < 104:
            y += 1
    return x, y


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    else:
        position[0], position[1] = move(position[0], position[1])


def draw():
    global x, y
    """ This function draws graphics from the image bank"""
    # Clears the screen and assigns a color
    pyxel.cls(11)
    # Loading images from the image bank 0
    # A cat in the middle
    pyxel.blt(position[0] + 32, position[1] + 32, 0, 0, 48, 16, 16, colkey=12)
    pyxel.blt(position[0], position[1], 0, 32, 48, 16, 16, colkey=12)
    # To draw an asset, pyxel.blt(xcord, y coord, x_cord_editor, y_cord_editor, x_size_image, y_size_image, chromekey)


################## main program ##################


WIDTH = 160
HEIGHT = 120
CAPTION = "Boomba Looompa?"

pyxel.init(WIDTH, HEIGHT, caption=CAPTION, scale=6, fps=60)

pyxel.load("assets/marioassets.pyxres")
pyxel.run(update, draw)
