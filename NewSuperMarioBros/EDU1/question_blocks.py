
class QuestionBlocks:
    def __init__(self, x: int, y: int, container="nothing"):
        self.x = x
        self.y = y
        self.container = container
        if container == "nothing":
            self.sprite = (0, 0, 16, 16, 16)
        elif container == "coin" or container == "mushroom":
            self.sprite = (0, 16, 0, 16, 16)
        else:
            self.sprite = (0, 16, 16, 16, 16)
