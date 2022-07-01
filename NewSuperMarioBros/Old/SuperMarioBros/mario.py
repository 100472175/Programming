import pyxel
from position import Position
from all_blocks import AllBlocks


class Mario(Position):
    def __init__(self, x, y):
        super().__init__(x, y)
        super().check_tilemap_collision()
        super().react_on_collision()
        from all_blocks import floor
        self.x = x
        self.y = y
        self.deltax = 0
        self.deltay = 0
        self.sprite = (0, 0, 48, 13, 16, 12)
        self.coins = 69
        self.score = 0
        self.lives = 3
        self.scroll_x = 0

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
            for b in range(len(platform_list_of_isa)):
                if player.y + 16 == platform_list_of_isa[b][1] or player.x + 16 == platform_list_of_isa[b][0]:
                    self.deltay = -12
            for c in pipes_list_of_isa:
                if player.x + 16 == c[0] or player.y + 16 == c[1]:
                    self.deltay = -12

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

    def game_ends(self):
        self.scroll_x = 0
        self.x = 20
        self.y = 10
        self.deltax = 0
        self.deltay = 0
        self.lives -= 1
