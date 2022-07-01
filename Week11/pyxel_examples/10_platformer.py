import math

import pyxel

CHARA_WIDTH = 8
CHARA_HEIGHT = 8
SCROLL_BORDER_X = 80

TILE_SPACE = (0, 0)
TILE_BLOCK = (1, 0)
TILE_FLOOR = (2, 0)
TILE_SPAWN = (0, 1)
TILE_ENEMY1 = (0, 1)
TILE_ENEMY2 = (1, 1)
TILE_ENEMY3 = (2, 1)

enemy_list = []
scroll_x = 0
player = None


def get_tilemap(x, y):
    return pyxel.tilemap(0).pget(x, y)


def check_tilemap_collision(x, y, dx, dy):
    x1 = x // 8
    y1 = y // 8
    x2 = (x + CHARA_WIDTH - 1) // 8
    y2 = (y + CHARA_HEIGHT - 1) // 8

    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            if get_tilemap(j, i) == TILE_BLOCK:
                return True

    if dy > 0 and y % 8 == 1:
        for i in range(x1, x2 + 1):
            if get_tilemap(i, y1 + 1) == TILE_FLOOR:
                return True

    return False


def react_on_collision(x, y, dx, dy):
    abs_dx = abs(dx)
    abs_dy = abs(dy)

    if abs_dx > abs_dy:
        sign = 1 if dx > 0 else -1
        for i in range(abs_dx):
            if check_tilemap_collision(x + sign, y, dx, dy):
                break
            x += sign

        sign = 1 if dy > 0 else -1
        for i in range(abs_dy):
            if check_tilemap_collision(x, y + sign, dx, dy):
                break
            y += sign
    else:
        sign = 1 if dy > 0 else -1
        for i in range(abs_dy):
            if check_tilemap_collision(x, y + sign, dx, dy):
                break
            y += sign

        sign = 1 if dx > 0 else -1
        for i in range(abs_dx):
            if check_tilemap_collision(x + sign, y, dx, dy):
                break
            x += sign

    return x, y, dx, dy


def check_floor(x, y):
    tile = get_tilemap(x // 8, y // 8)
    return tile == TILE_BLOCK or tile == TILE_FLOOR


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def update(self):
        global scroll_x

        if pyxel.btn(pyxel.KEY_LEFT):
            self.dx = -2

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.dx = 2

        self.dy = min(self.dy + 1, 3)

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.dy = -6

        self.x, self.y, self.dx, self.dy = react_on_collision(
            self.x, self.y, self.dx, self.dy
        )

        if self.x < scroll_x:
            self.x = scroll_x

        if self.y < 0:
            self.y = 0

        self.dx = int(self.dx * 0.8)

        if self.x > scroll_x + SCROLL_BORDER_X:
            last_scroll_x = scroll_x
            scroll_x = min(self.x - SCROLL_BORDER_X, 240 * 8)

    def draw(self):
        pyxel.rectb(self.x - scroll_x, self.y, 8, 8, 9)



class App:
    def __init__(self):
        pyxel.init(128, 128, title="Pyxel Mario")

        pyxel.load("assets/marioassets.pyxres")

        # make enemy spawn images invisible
        pyxel.image(0).rect(0, 8, 24, 8, 0)

        global player
        player = Player(0, 0)


        pyxel.run(self.update, self.draw)

    def update(self):
        player.update()

        for enemy in enemy_list:
            if abs(player.x - enemy.x) < 6 and abs(player.y - enemy.y) < 6:
                game_over()
                return

            enemy.update()

            if enemy.x < scroll_x - 8 or enemy.x > scroll_x + 160 or enemy.y > 160:
                enemy.alive = False


    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(-(scroll_x % 8), 0, 0, scroll_x // 8, 0, 17, 16)
        player.draw()

        for enemy in enemy_list:
            enemy.draw()


def game_over():
    global scroll_x, enemy_list

    scroll_x = 0
    player.x = 0
    player.y = 0
    player.dx = 0
    player.dy = 0

    enemy_list = []
    spawn_enemy(0, 127)


App()
