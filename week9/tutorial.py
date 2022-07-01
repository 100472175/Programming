import pyxel
import enum
import time
import random


class Direction(enum.Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


# Apple class handles drawing and moving the apple and checking if sth is on the apple (snake ate it)
class Apple:
    def __init__(self, x, y):
        self.x = x  # Variable inside the class
        self.y = y
        self.w = 8  # Width
        self.h = 8  # Height

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, self.w, self.h, colkey=0)

    def intersects(self, u, v, w, h):  # U and v are the coordinates to check with
        is_intersected = False
        if (
                u + w > self.x
                and self.x + self.w > u
                and v + h > self.y
                and self.y + self.h > v
        ):
            is_intersected = True
        return is_intersected

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class SnakeSection:
    def __init__(self, x, y, is_head=False):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.is_head = is_head

    def draw(self, direction):
        width = self.w
        height = self.h
        sprite_x = 0  # Variables to manipulate where the sprite lives on the x map
        sprite_y = 0
        # If this is the head section, we need to change and flip the sprite on the direction
        if self.is_head:
            if direction == Direction.RIGHT:
                sprite_x = 8
                sprite_y = 0
            if direction == Direction.LEFT:
                sprite_x = 8
                sprite_y = 0
                width *= -1  # This flips horizontally the sprite
            if direction == Direction.DOWN:
                sprite_x = 0
                sprite_y = 8
            if direction == Direction.UP:
                sprite_x = 0
                sprite_y = 8
                height *= -1  # Flips the sprite vertically
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, width, height, colkey=0)


class App:
    def __init__(self):
        pyxel.init(192, 128, scale=4, caption="NIBBLES", fps=60)
        pyxel.load("assets/resources.pyxres")
        self.apple = Apple(64, 32)
        self.snake = []  # Store the snake section
        self.snake.append(SnakeSection(32, 32, is_head=True))
        self.snake.append(SnakeSection(24, 32))
        self.snake.append(SnakeSection(16, 32))
        self.snake_direction = Direction.RIGHT
        self.sections_to_add = 0
        self.speed = 1.5  # Moving 1.5 times per second
        self.time_last_frame = time.time()
        self.dt = 0
        self.time_since_last_move = 0
        pyxel.run(self.update, self.draw)

    def update(self):  # Happens for every frame
        time_this_frame = time.time()
        self.dt = time_this_frame - self.time_last_frame
        self.time_last_frame = time_this_frame
        self.time_since_last_move += self.dt
        if self.time_since_last_move >= 1 / self.speed:
            self.time_since_last_move = 0
            self.move_snake()
            self.check_collisions()

    def draw(self):
        pyxel.cls(1)
        self.apple.draw()
        for s in self.snake:
            s.draw(self.snake_direction)

    def check_collisions(self):
        # Apple
        if self.apple.intersects(self.snake[0].x, self.snake[0].y, self.snake[0].w, self.snake[0].h):
            self.speed += (self.speed * 0.1)
            self.sections_to_add += 4
            self.move_apple()

    def move_apple(self):
        # Select a new random location for the apple
        # Make sure it is not in a wall or in the snake
        good_position = False
        while not good_position:
            new_x = random.randrange(8, 184, 8)  # From where, to where (192-8), jumps
            new_y = random.randrange(8, 120, 8)
            good_position = True
            # Check snake
            for s in self.snake:
                if (
                        new_x + 8 > s.x
                        and s.x + s.w > new_x
                        and new_y + 8 > s.y
                        and s.y + s.h > new_y
                ):
                    good_position = False
                    break
            # Check Wall

            # If the position is good, move the apple
            if good_position:
                self.apple.move(new_x, new_y)

    def move_snake(self):
        # Do we need to grow the snake=?
        if self.sections_to_add > 0:
            self.snake.append(SnakeSection(self.snake[-1].x, self.snake[-1].y))
            self.sections_to_add -= 1
        # Move the head
        previous_location_x = self.snake[0].x
        previous_location_y = self.snake[0].y
        if self.snake_direction == Direction.RIGHT:
            self.snake[0].x += self.snake[0].w
        if self.snake_direction == Direction.LEFT:
            self.snake[0].x -= self.snake[0].w
        if self.snake_direction == Direction.DOWN:
            self.snake[0].y += self.snake[0].w
        if self.snake_direction == Direction.UP:
            self.snake[0].y -= self.snake[0].w
        # Moving the tail
        for s in self.snake:
            if s == self.snake[0]:
                continue
            current_location_x = s.x
            current_location_y = s.y
            s.x = previous_location_x
            s.y = previous_location_y
            previous_location_x = current_location_x
            previous_location_y = current_location_y


# Kickstart our program
App()
