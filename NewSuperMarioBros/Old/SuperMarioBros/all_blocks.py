from breakableblocks import BreakableBlock
from questionblocks import QuestionBlock
from floor import Floor


class AllBlocks(BreakableBlock, QuestionBlock, Floor):
    def __init__(self):
        super().__init__(x, y)
        self.floor_list = self.floor_list_of_isa
        self.floor_list.append(self.floor_list_of)

