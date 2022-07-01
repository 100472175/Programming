floor_list_of_isa = []
for i in range(143 + 1):
    floor_list_of_isa.append((i * 8, 31 * 8))
    # We have to multiply everything by 8 because the data provided by Isa is from the tile map,
    # which is made up of 8x8 squares
for i in range(148, 225 + 1):
    floor_list_of_isa.append(((i + 148) * 8, 31 * 8))
print(floor_list_of_isa)