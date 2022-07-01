from typing import Tuple

import pyxel
import random

player_width = 13  # en mario
player_height = 16  # en mario
scroll_border = 80  # en board

# They have to be multiplied by 16 to get the correct coordinates on the editor
tile_space = (0, 0)  # en board
# The tile has to be divided into 4 different 8x8 tiles, with s-> superior, i -> inferior, l -> left and r -> right
tile_cobble_sl = (4, 14)
tile_cobble_sr = (5, 14)
tile_cobble_il = (4, 15)
tile_cobble_ir = (5, 15)
tile_cobble_list = ((4, 14), (5, 14), (4, 15), (5, 15))  # en unbreakable_blocks

tile_jukebox_sl = (2, 2)
tile_jukebox_sr = (3, 2)
tile_jukebox_il = (2, 3)
tile_jukebox_ir = (3, 3)
tile_jukebox_list = ((2, 2), (3, 2), (2, 3), (3, 3))  # en unbreakable_blocks

tile_question_sl = (2, 0)
tile_question_sr = (3, 0)
tile_question_il = (2, 1)
tile_question_ir = (3, 1)
tile_question_list = ((2, 0), (3, 0), (2, 1), (3, 1))  # en question_blocks

tile_lists_of_lists = [(4, 14), (5, 14), (4, 15), (5, 15), (2, 2), (3, 2), (2, 3), (3, 3), (2, 0), (3, 0), (2, 1),
                       (3, 1), (0, 2), (1, 2), (0, 3), (1, 3), (4, 0), (5, 0), (6, 0), (7, 0), (4, 1), (9, 1), (4, 2),
                       (7, 2)]

# Head -> upper part of pipe, s -> superior, l-> left, i -> inferior, r -> right,
# c -> center in x axis, m-> center in y axis
tile_pipe_head_sl = (4, 0)
tile_pipe_head_scl = (5, 0)
tile_pipe_head_scr = (6, 0)
tile_pipe_head_sr = (7, 0)
tile_pipe_head_il = (4, 1)
tile_pipe_head_ir = (9, 1)
tile_pipe_body_left = (4, 2)
tile_pipe_body_right = (7, 2)
tile_pipe_list = ((4, 0), (5, 0), (6, 0), (7, 0), (4, 1), (9, 1), (4, 2), (7, 2))  # en pipes

tile_bricks_sl = (0, 2)
tile_bricks_sr = (1, 2)
tile_bricks_il = (0, 3)
tile_bricks_ir = (1, 3)
tile_bricks_list = [(0, 2), (1, 2), (0, 3), (1, 3)]  # en bricks

tile_goomba = (2, 3)  # en goomba
tile_goomba_generate = (6, 14)

# This is the list of the floor of each block, we use it so mario does not fall off the screen, this allows mario to
# jump when only on this blocks,
floor_list_of_isa = []
for i in range(144):
    floor_list_of_isa.append((i * 8, 31 * 8))
    # We have to multiply everything by 8 because the data provided by Isa is from the tile map, which is made up of
    # 8x8 squares
for i in range(107):
    floor_list_of_isa.append(((i + 148) * 8, 31 * 8))

platform_list_of_isa = [(29*8, 23*8), (30*8, 23*8),(44*8,15*8),(45*8,15*8)]
for i in range(40,48):
    platform_list_of_isa.append((i*8, 23*8))
for i in range(160,165):
    platform_list_of_isa.append(i*8,23)


pipes_list_of_isa = []

platforms_list_of_isa = []



enemy_list = []
scroll_x = 0
player = None


def get_tilemap(x, y):
    return pyxel.tilemap(0).pget(x, y)


def check_tilemap_collision(x, y, deltax, deltay):
    x1 = x // 8
    y1 = y // 8
    x2 = (x + player_width - 1) // 8
    y2 = (y + player_height - 1) // 8

    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            for k in range(len(tile_lists_of_lists)):
                if get_tilemap(j, i) == tile_lists_of_lists[k]:
                    return True
    return False


def react_on_collision(x, y, deltax, deltay):
    abs_deltax = abs(deltax)
    abs_deltay = abs(deltay)

    if abs_deltax > abs_deltay:
        sign = 1 if deltax > 0 else -1
        for i in range(abs_deltax):
            if not check_tilemap_collision(x + sign, y, deltax, deltay):
                x += sign

        sign = 1 if deltay > 0 else -1
        for i in range(abs_deltay):
            if not check_tilemap_collision(x, y + sign, deltax, deltay):
                y += sign

    else:
        sign = 1 if deltay > 0 else -1
        for i in range(abs_deltay):
            if not check_tilemap_collision(x, y + sign, deltax, deltay):
                y += sign

        sign = 1 if deltax > 0 else -1
        for i in range(abs_deltax):
            if not check_tilemap_collision(x + sign, y, deltax, deltay):
                x += sign

    return x, y, deltax, deltay


def check_floor(x, y):
    tile = get_tilemap(x // 8, y // 8)
    for k in range(len(tile_lists_of_lists)):
        if tile == tile_lists_of_lists[k]:
            return True
        else:
            return False


class Mario:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.deltax = 0
        self.deltay = 0
        self.sprite = (0, 0, 48, 13, 16, 12)
        self.coins = 69
        self.score = 0

    def update(self):
        global scroll_x  # ------------------------------------------------------------------------------------------

        if pyxel.btn(pyxel.KEY_LEFT):
            self.deltax = -2

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.deltax = 2

        self.deltay = min(self.deltay + 1, 3)

        if pyxel.btnp(pyxel.KEY_UP):
            for k in range(len(floor_list_of_isa)):
                if player.y + 16 == floor_list_of_isa[k][1]:
                    self.deltay = -12
                    
           """ for b in range(len(platform_list_of_isa)): 
                if player.y + 16 == [b][1]:"""
                    


        self.x, self.y, self.deltax, self.deltay = react_on_collision(self.x, self.y, self.deltax, self.deltay)

        if self.x < scroll_x:
            self.x = scroll_x

        if self.y < 0:
            self.y = 0

        self.deltax = int(self.deltax * 0.8)

        if self.x > scroll_x + scroll_border:
            last_scroll_x = scroll_x
            scroll_x = min(self.x - scroll_border, 248 * 8)

        if self.y > 300:
            game_ends()

    def draw(self):
        pyxel.blt(self.x - scroll_x, self.y, *self.sprite)


class Goomba:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.deltax = 0
        self.deltay = 0
        self.direction = 1
        self.alive = True
        self.sprite = (0, 32, 48, 16, 16, 12)
        self.is_falling = True

    def update(self):
        self.deltax = self.direction
        self.deltay = min(self.deltay + 1, 3)

        self.x, self.y, self.deltax, self.deltay = \
            react_on_collision(self.x, self.y, self.deltax, self.deltay)

    def draw(self):
        pyxel.blt(self.x - scroll_x, self.y, *self.sprite)


class KoopaTroopa:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def enemy_update(x, y, kind, is_alive):
    if is_alive and abs(x - player.x) < 10 and abs(y - player.y) < 12:
        is_alive = False
        player.score += 200
    return x, y, kind, is_alive


class App:
    def __init__(self):
        pyxel.init(255, 255, title='Mario Bosh', fps=60)
        pyxel.load("assets/marioassets.pyxres")
        pyxel.image(0).rect(48, 112, 16, 16, 12)
        self.enemy = [(random.randint(8, 250), 200, random.randint(0, 2), True)]

        # This will resolve when importing classes
        global player
        player = Mario(20, 10)
        pyxel.run(self.update, self.draw)

    def update_enemy(x, y, kind, is_alive):
        if is_alive and abs(x - player.x) < 12 and abs(y - player.y) < 12:
            is_alive = False

    def update(self):
        player.update()

        if pyxel.btnp(pyxel.KEY_SHIFT):
            pyxel.quit()
        self.remaining_time = 300 - pyxel.frame_count // 60

        #        for i, v in enumerate(self.enemy):
        #            self.enemy[i] = self.update_enemy(*v)

        if self.remaining_time == 0:
            game_ends()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(-(scroll_x % 8), 0, 0, scroll_x // 8, 0, 40, 40)
        player.draw()

        for enemy in enemy_list:
            enemy.draw()

        pyxel.text(230, 4, str(self.remaining_time), 0)
        pyxel.text(100, 4, str(player.coins) + " coins", 0)
        pyxel.text(150, 4, 'Score: ' + str(player.score), 0)
        pyxel.text(1, 1, 'X cooridnate: ' + str(player.x), 0)
        pyxel.text(1, 11, 'Y coordinate: ' + str(player.y), 0)
        pyxel.blt(95, 4, 0, 11, 232, 4, 6, 12)

        for x, y, kind, is_alive in self.enemy:
            if is_alive:
                pyxel.blt(x, y, 0, 48, 32, 16, 24, 12)


def game_ends():
    global scroll_x, enemy_list

    scroll_x = 0
    player.x = 20
    player.y = 10
    player.deltax = 0
    player.deltay = 0

    enemy_list = []


App()
