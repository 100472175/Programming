class Mario:
    """This class stores all the information needed for Mario"""
    # I need to store the position, as y,x
    # Facing right or left
    def __init__(self, x: int, y: int, direc: str):
        # This is the list of attributes
        """
        This method created the Mario object
        :param x: Starting position of x of Mario
        :param y: Starting y coordinate of Mario
        :param direc: a boolean to indicate where Mario is looking at.
                    True=Right, False=Left
        """
        self.x = x
        self.y = y
        self.direction = direc
        # Here, we assume Mario wil be always placed at the first
        # bank at first position and it will be 16x16 pixels
        self.sprite = (0, 0, 48, 16, 16)
        # We also assume Mario always starts with 3 lives
        self.lives = 3

    # After creating the parameters, we see what does mario need to be able to do.

    def move(self, direction: str, size: int):
        mario_x_size = self.sprite[3]
        if direction.lower() == 'right' and self.x < size - mario_x_size:
            self.x = self.x + 1
        elif direction.lower() == 'left' and self.x > 0:
            self.x -= 1

