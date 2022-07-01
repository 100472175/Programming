
class Floor():
    def __init__(self):
        # This is the list of the floor of each block, we use it so mario does not fall off the screen, this allows
        # mario to jump when only on this blocks,
        self.floor_list_of_isa = []
        for i in range(143 + 1):
            self.floor_list_of_isa.append((i * 8, 31 * 8))
            # We have to multiply everything by 8 because the data provided by Isa is from the tile map,
            # which is made up of 8x8 squares
        for i in range(148, 225 + 1):
            self.floor_list_of_isa.append(((i + 148) * 8, 31 * 8))

