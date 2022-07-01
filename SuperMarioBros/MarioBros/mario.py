import pyxel


class Mario:
    """ This class stores all the information needed for Mario"""

    def __init__(self, x: int, y: int, dir: str):
        x = 24
        y = 96
        self.x = x
        self.y = y
        self.dx = 0  # Mario's x direction
        self.dy = 0  # Marios y direction
        self.direction = dir
        self.sprite = (0, 0, 48, 16, 16, 12)
        self.lives = 3
        self.small = True


    # Continuous movement
    """def move(self, direction: str, size: int):
        mario_x_size = self.sprite[3]
        mario_y_size = self.sprite[4]
        if direction.lower() == 'right' and self.x < size - mario_x_size:
            self.x += 1
        elif direction.lower() == 'left' and self.x > 0:
            self.x -= 1
        if direction.lower() == 'up' and self.y > 0:
            self.y -= 1
        elif direction.lower() == 'down' and size - mario_y_size > self.y <= 95:
            self.y += 1"""

    def check_tilemap_collision(x, y, dx, dy):

        # Spatial Data
        TILE_BRICKS = (0, 16)
        TILE_QUESTION = (16, 0)
        TILE_COBBLESTONE = (32, 104)

        x1 = x // 16
        y1 = y // 16
        x2 = (x + 16 - 1) // 8
        y2 = (y + 16 - 1) // 8

        if dy > 0 and y % 16 == 1:
            for i in range(x1, x2 + 1):
                if get_tilemap(i, y1 + 1) == TILE_COBBLESTONE:
                    return True
        if dy > 0 and y % 16 == 1:
            for i in range(x1, x2 + 1):
                if get_tilemap(i, y1 + 1) == TILE_QUESTION:
                    return True
        if dy > 0 and y % 16 == 1:
            for i in range(x1, x2 + 1):
                if get_tilemap(i, y1 + 1) == TILE_BRICKS:
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

    def update(self):
        global scroll_x
        if pyxel.btn(pyxel.KEY_LEFT):
            self.dx = -2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.dx = 2
        self.dy = min(self.dy + 1, 3)
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.dy = -6
        self.x, self.y, self.dx, self.dy = react_on_collision(self.x, self.y, self.dx, self.dy)

        SCROLL_BORDER_X = 80

        if self.x < scroll_x:
            self.x = scroll_x
        if self.y < 0:
            self.y = 0
        self.dx = int(self.dx * 0.8)
        if self.x > scroll_x + SCROLL_BORDER_X:
            last_scroll_x = scroll_x
            scroll_x = min(self.x - SCROLL_BORDER_X, 240 * 8)

    def get_tilemap(x, y):
        return pyxel.tilemap(0).get(x, y)


