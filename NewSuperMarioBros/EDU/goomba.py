class Goomba:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.direction = 1
        self.is_falling = True
        self.alive = True
        self.sprite = (0, 32, 48, 16, 16, 12)

    def update(self):
        self.dx = self.direction
        self.dy = min(self.dy + 1, 3)

