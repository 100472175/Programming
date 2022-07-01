import random
import pyxel

from mario import Mario
from blocks import Blocks
from coins import Coin
from enemies import Enemies
from mushrooms import Mushroom
from luigi import Luigi


class Board:
    # Gets the tile from a specific coordinate from the tile map
    def get_tilemap_L(self, x, y):
        return pyxel.tilemap(0).pget(x, y)

    # This function gets the coordinates of mario, and adds them to the width and height of the player, which then
    # checks, in the range, if mario is between two tile, which he always is, as the tiles are 8 by 8 and mario is
    # 13 pixels wide and 16 pixels tall when they are small and 16 by 32 when they are big and divides them by 8.
    # This then checks the tile where mario wants to go and if it is in the list of tiles mario has to collide with,
    # in this case self.player2.col_tiles, (collidable tiles)
    def check_tilemap_collision_l(self, x, y):
        x1 = x // 8
        y1 = y // 8
        x2 = (x + self.player2.width - 1) // 8
        y2 = (y + self.player2.height - 1) // 8
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                for k in range(len(self.player2.col_tiles)):
                    if self.get_tilemap_l(j, i) == self.player2.col_tiles[k]:
                        return True
        return False

    # This is the method that takes the position if mario and the diration is facing, to tell us if the player can
    # move to tht position. It takes 4 arguments, marios x and y position and the direction where mario wants to move.

    def react_on_collision_l(self, x, y, deltax, deltay):
        abs_deltax = abs(deltax)
        abs_deltay = abs(deltay)

        if abs_deltax > abs_deltay:
            sign = 1 if deltax > 0 else -1  # This is a normal if, made into a single line to occupy less space
            for i in range(abs_deltax):  # This gets all the numbers from 0 to where mario wants to move in the x-axis
                if not self.check_tilemap_collision_l(x + sign, y):  # And lastly, it checks that it can move
                    x += sign

        sign = 1 if deltay > 0 else -1
        for i in range(abs_deltay):
            if not self.check_tilemap_collision_l(x, y + sign):
                y += sign

        else:
            sign = 1 if deltay > 0 else -1
            for i in range(abs_deltay):
                if not self.check_tilemap_collision_l(x, y + sign):
                    y += sign

            sign = 1 if deltax > 0 else -1
            for i in range(abs_deltax):
                if not self.check_tilemap_collision_l(x + sign, y):
                    x += sign

        # This function then returns the x and y position mario will be on the next frame
        return x, y, deltax, deltay

    def enemy_collision_l(self, x, y):
        x1 = x // 8
        y1 = y // 8
        x2 = (x + self.player2.width - 1) // 8
        y2 = (y + self.player2.height - 1) // 8
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                for k in self.enemy.all_enemy_tiles:
                    if self.get_tilemap_l(j, i) == k:
                        return True
        return False

    def react_on_collision_except_vertical_l(self, x, y, deltax):
        abs_deltax = abs(deltax)
        sign = 1 if deltax > 0 else -1
        for i in range(abs_deltax):
            if self.enemy_collision_l(x + sign, y):
                if self.player2.big:
                    self.player2.decrease_with_enemy_l()
                else:
                    self.game_ends()

    def mushroom_collision_l(self, x, y):
        x1 = x // 8
        y1 = y // 8
        x2 = (x + self.player2.width - 1) // 8
        y2 = (y + self.player2.height - 1) // 8
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                for k in self.mushroom.tiles:
                    if self.get_tilemap_l(j, i) == k:
                        return True
        return False

    def react_with_mushroom_collision_l(self, x, y, deltax):
        abs_deltax = abs(deltax)
        sign = 1 if deltax > 0 else -1
        for i in range(abs_deltax):
            if self.mushroom_collision_l(x + sign, y):
                if self.cooldown <= 0:
                    if not self.player2.big:
                        self.player2.grow_with_mushroom_l()
                        self.cooldown = 2
                    else:
                        self.player2.score += 200

    def game_ends(self):
        self.player2.scroll_x = 0
        self.player2.x = 20
        self.player2.y = 10
        self.player2.deltax = 0
        self.player2.deltay = 0
        self.player2.lives -= 1
        self.player2.big = False
        self.elapsed_time = 0

    # This is the method that prints the whole game
    def draw(self):
        # The first if condition makes it so the level is displayed if mario is playing, if he is alive and has
        # remaining lives, and it has not reached the castle
        if self.player2.lives > 0 and self.player2.x < 2000:
            # Clears the screen to a blue background
            pyxel.cls(12)
            # Print the map
            pyxel.bltm(-(self.player2.scroll_x % 8), 0, 0, self.player2.scroll_x // 8, 0, 40, 40)
            # This is the text that represents the remaining time
            pyxel.text(230, 4, str(self.remaining_time), 0)
            # This prints the number of coins in the game and the next blt draws the logo of a small coin
            pyxel.text(100, 20, str(self.player2.coins) + " coins", 0)
            pyxel.blt(95, 20, 0, 11, 232, 4, 6, 12)
            # This prints the score of mario
            pyxel.text(140, 20, 'Score2: ' + str(self.player2.score), 0)
            # These two print the x and y coordinates of mario, used in debug but ended being usefully
            pyxel.text(1, 1, 'X coordinate: ' + str(self.player2.x), 0)
            pyxel.text(1, 11, 'Y coordinate: ' + str(self.player2.y), 0)
            # These print the number of lives remaining and the small heart sprite
            pyxel.text(190, 20, 'Lives: ' + str(self.player2.lives), 0)
            pyxel.blt(180, 20, 0, 17, 232, 7, 8, 12)
            for i in self.coins_list:
                i.draw(i.x - self.player2.scroll_x, i.y)

            # Part of the debug of colision and acting on brick blocks
            """for j in self.bricks_list:
                j.draw(j.x - self.player2.scroll_x, j.y)"""

            # Prints the player
            self.player2.draw()

            # We have to draw each block, each coin and each mushroom:
            for i in self.player2.question_block_list:
                pyxel.blt(i.x - self.player2.scroll_x, i.y, *i.sprite)

            # This function print the coins on the screen
            for i in self.player2.coins_list:
                pyxel.blt(i.x - self.player2.scroll_x, i.y, *i.sprite)

            for k in self.enemies_list:
                pyxel.blt(k.x - self.player2.scroll_x, k.y, *k.sprite)

            # This prints all the mushrooms on the screen
            for j in self.player2.mushroom_list:
                pyxel.blt(j.x - self.player2.scroll_x, j.y, *j.sprite)

            # This calls the function kikblock, that makes the block break, disappear, removing the object from the list
            self.player2.kikblock_l(self.player2.x, self.player2.y)

            # This function would ake mario collide with the brick blocks, the question blocks and the already
            # hit question blocks
            self.player2.collisions_with_blocks_l()

            # This function checks the position of the mushrooms and if mario is not big, it will increase mario's size
            self.player2.grow_with_mushroom_l()

            # This function checks the position of mario and checks if it is the same as the coins and remove then
            # while adding them up to the counter of coins the player has.
            self.player2.pick_coin_l(self.player2.x, self.player2.y)

        # If mario is at the end of the map, a congratulations message is shown:    
        elif self.player2.x > 2000:
            pyxel.cls(0)
            pyxel.text(255 // 3, 255 // 2, "You win, congratulations <3 \n :D ", 7)
        # If nothing of the above is satisfied, it means that mario is dead and has no more lives
        else:
            pyxel.cls(0)
            pyxel.text(255 // 2.5, 255 // 2, "Game over :(", 7)

    # When mario hits the flag pole, he grows, acting as a checkpoint
    def mario_grows_l(self):
        if 380 < self.player2.x > 400 and 216 > self.player2.y < 150:
            self.player2.big = True

    # All of this medthod is executed every time a new frame is going to be displayed
    def update(self):
        # If the q key or the shift key are pressed, the program will exit
        if pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_SHIFT):
            pyxel.quit()

        # Luigi's update moving left
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player2.deltax = -2

        # Luigi's update moving right
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player2.deltax = 2

        # God mode
        if pyxel.btn(pyxel.KEY_G) and pyxel.btn(pyxel.KEY_M):
            self.player2.lives = 99999
            self.player2.big = True

        # Gravity, that moves mario down a maximum of 3 and a minimum of 1 pixel
        self.player2.deltay = min(self.player2.deltay + 1, 3)

        # This is the part that makes mario big if he encounters the flag
        """if self.player2.x > 100:
            self.player2.big = True"""

        # This function would ake mario collide with the brick blocks, the question blocks and the already
        # hit question blocks
        self.player2.collisions_with_blocks_l()

        # This function checks the position of the mushrooms and if mario is not big, it will increase mario's size
        self.player2.grow_with_mushroom_l()

        # When Mario touches a coin, the score and the coin counter will increase and the coin will be removed:

        # Collision of coins
        for i in self.coins_list:
            if abs(self.player2.x - i.x) < 15 and abs(self.player2.y - i.y) < 15:
                self.player2.coins += 1
                self.coins_list.remove(i)
                self.player2.score += 200

                # Collision of bricks and actuating on the different blocks:

                """if abs(self.player2.y - k.y) < 3:
                    self.coins_list.append(Coin(k.x, k.y+16))
                    self.player2.question_block_list.remove(k)"""

        # This is the update that is inside the player
        self.player2.update()

        # Used to debug and be a ble to jump freely on the map to test the different collisions and speeds, because
        # it is always executed, this code will be commented on the final program, as we only want it to jump when in
        # contact with the floor or a block
        """if pyxel.btnp(pyxel.KEY_W):
            self.player2.deltay = -12"""

        # This is the correct method that is used for the player to add to the que the jump when the W or the
        # upwards arrow is pressed
        if pyxel.btnp(pyxel.KEY_UP):
            for l in self.blocks.pfp_list:
                if self.player2.x + 16 == l.x and self.player2.y + 16 == l.x:
                    self.player2.deltay = -12
            """for k in self.blocks.floor_list:
                # If mario is on top of a block
                if self.player2.y + 16 == k.x:
                    self.player2.deltay = -12
            for c in self.blocks.pipes_list:
                # Checking that mario is on top of a pipe so the player can jump
                if self.player2.x + 16 == c.x and self.player2.y + 16 == c.x:
                    self.player2.deltay = -12"""

        # This is the part that affect marios movement, which checks for the collisions and if the path is free,
        # moves the player
        self.player2.x, self.player2.y, self.player2.deltax, self.player2.deltay = \
            self.react_on_collision_l(self.player2.x, self.player2.y, self.player2.deltax, self.player2.deltay)

        if self.player2.x < self.player2.scroll_x:
            self.player2.x = self.player2.scroll_x

        # This prevents mario from escaping the screen from the top
        if self.player2.y < 0:
            self.player2.y = 0

        self.player2.deltax = int(self.player2.deltax * 0.8)

        if self.player2.x > self.player2.scroll_x + self.scroll_border:
            self.player2.scroll_x = min(self.player2.x - self.scroll_border, 248 * 8)

            # Mario's collision with enemies:
            self.react_on_collision_except_vertical_l(self.player2.x, self.player2.y, self.player2.deltax)

        # Deaths and time:
        # self.remaining_time = 300 - pyxel.frame_count // 60
        self.remaining_time = self.time - self.elapsed_time
        if pyxel.frame_count % self.fps == 0:
            self.elapsed_time += 1

        # Adding a cooldown function
        if pyxel.frame_count % self.fps == 0:
            self.cooldown -= 1

        # If the player falls out of the map, though the floor gap, it will call the end function, that resets the game
        if self.remaining_time == 0 or self.player2.y > 300:
            self.game_ends()

        for i in self.player2.coins_list:
            pyxel.blt(i.x - self.player2.scroll_x, i.y, *i.sprite)

        for i in self.player2.mushroom_list:
            pyxel.blt(i.x, i.y, *i.sprite)

        # We have to check in each frame if Mario is colliding with any block, if he is kicking any block or if he
        # is picking any mushroom or coin:
        self.player2.kikblock_l(self.player2.x, self.player2.y)
        self.player2.grow_with_mushroom_l()
        self.player2.pick_coin_l(self.player2.x, self.player2.y)

        # Generating the enemies:
        # if (random.random() * self.elapsed_time % 15) == 1:

        # Update of enemies:
        for k in self.enemies_list:
            if k.x < 50 or k.x > 200:
                self.enemies_list.remove(k)
            k.move_left()

        if len(self.enemies_list) > 4:
            self.aux = 0
            self.aux = self.enemies_list[0]
            self.enemies_list.remove(self.aux)

        for g in self.enemies_list:
            if not self.player2.big:
                if g.x == self.player2.x and abs(g.y - self.y) < 3:
                    self.game_ends()
            else:
                if g.x == self.player2.x and abs(g.y - self.y + 16) < 3:
                    self.player2.decrease_with_enemy_l()
            self.enemies_list.remove(g)



