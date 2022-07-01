from breakableblocks import BreakableBlock
from questionblocks import QuestionBlock
from floor import Floor


class AllBlocks(BreakableBlock, QuestionBlock, Floor):
    def __init__(self):
        super().__init__()
        self.platforms = [(232, 184), (240, 184), (352, 120), (360, 120), (1616, 184), (1616, 184), (1768, 120),
                          (1776, 120), (1768, 184), (1776, 184), (1816, 184), (1824, 184), (1888, 232), (1896, 232),
                          (1904, 216), (1912, 216), (1920, 200), (1928, 200), (720, 184), (728, 184), (320, 184),
                          (328, 184), (336, 184), (344, 184), (352, 184), (360, 184), (368, 184), (376, 184),
                          (384, 184), (1280, 184), (1288, 184), (1296, 184), (1304, 184), (1312, 184), (1320, 184),
                          (1344, 120), (1352, 120), (1360, 120), (1368, 120), (1376, 120), (1384, 120), (1392, 120),
                          (1400, 120), (1408, 120), (1416, 120), (1424, 120), (1432, 120), (1440, 120), (1448, 120),
                          (1456, 120), (1464, 120), (1472, 120), (1480, 120), (1488, 120), (1496, 120), (1568, 120),
                          (1576, 120), (1584, 120), (1592, 120), (1600, 120), (1608, 120), (1616, 120), (1624, 120),
                          (1680, 184), (1688, 184), (1696, 184), (1704, 184)]

        # self.floor = self.floor.floor_list_of_isa
        self.floor = [(0, 248), (8, 248), (16, 248), (24, 248), (32, 248), (40, 248), (48, 248), (56, 248), (64, 248),
                      (72, 248), (80, 248), (88, 248), (96, 248), (104, 248), (112, 248), (120, 248), (128, 248),
                      (136, 248), (144, 248), (152, 248), (160, 248), (168, 248), (176, 248), (184, 248), (192, 248),
                      (200, 248), (208, 248), (216, 248), (224, 248), (232, 248), (240, 248), (248, 248), (256, 248),
                      (264, 248), (272, 248), (280, 248), (288, 248), (296, 248), (304, 248), (312, 248), (320, 248),
                      (328, 248), (336, 248), (344, 248), (352, 248), (360, 248), (368, 248), (376, 248), (384, 248),
                      (392, 248), (400, 248), (408, 248), (416, 248), (424, 248), (432, 248), (440, 248), (448, 248),
                      (456, 248), (464, 248), (472, 248), (480, 248), (488, 248), (496, 248), (504, 248), (512, 248),
                      (520, 248), (528, 248), (536, 248), (544, 248), (552, 248), (560, 248), (568, 248), (576, 248),
                      (584, 248), (592, 248), (600, 248), (608, 248), (616, 248), (624, 248), (632, 248), (640, 248),
                      (648, 248), (656, 248), (664, 248), (672, 248), (680, 248), (688, 248), (696, 248), (704, 248),
                      (712, 248), (720, 248), (728, 248), (736, 248), (744, 248), (752, 248), (760, 248), (768, 248),
                      (776, 248), (784, 248), (792, 248), (800, 248), (808, 248), (816, 248), (824, 248), (832, 248),
                      (840, 248), (848, 248), (856, 248), (864, 248), (872, 248), (880, 248), (888, 248), (896, 248),
                      (904, 248), (912, 248), (920, 248), (928, 248), (936, 248), (944, 248), (952, 248), (960, 248),
                      (968, 248), (976, 248), (984, 248), (992, 248), (1000, 248), (1008, 248), (1016, 248),
                      (1024, 248), (1032, 248), (1040, 248), (1048, 248), (1056, 248), (1064, 248), (1072, 248),
                      (1080, 248), (1088, 248), (1096, 248), (1104, 248), (1112, 248), (1120, 248), (1128, 248),
                      (1136, 248), (1144, 248), (2368, 248), (2376, 248), (2384, 248), (2392, 248), (2400, 248),
                      (2408, 248), (2416, 248), (2424, 248), (2432, 248), (2440, 248), (2448, 248), (2456, 248),
                      (2464, 248), (2472, 248), (2480, 248), (2488, 248), (2496, 248), (2504, 248), (2512, 248),
                      (2520, 248), (2528, 248), (2536, 248), (2544, 248), (2552, 248), (2560, 248), (2568, 248),
                      (2576, 248), (2584, 248), (2592, 248), (2600, 248), (2608, 248), (2616, 248), (2624, 248),
                      (2632, 248), (2640, 248), (2648, 248), (2656, 248), (2664, 248), (2672, 248), (2680, 248),
                      (2688, 248), (2696, 248), (2704, 248), (2712, 248), (2720, 248), (2728, 248), (2736, 248),
                      (2744, 248), (2752, 248), (2760, 248), (2768, 248), (2776, 248), (2784, 248), (2792, 248),
                      (2800, 248), (2808, 248), (2816, 248), (2824, 248), (2832, 248), (2840, 248), (2848, 248),
                      (2856, 248), (2864, 248), (2872, 248), (2880, 248), (2888, 248), (2896, 248), (2904, 248),
                      (2912, 248), (2920, 248), (2928, 248), (2936, 248), (2944, 248), (2952, 248), (2960, 248),
                      (2968, 248), (2976, 248), (2984, 248)]

        self.pipes = [(448, 216), (456, 216), (464, 216), (472, 216), (576, 184), (584, 184), (592, 184), (600, 184),
                      (768, 160), (776, 160), (784, 160), (792, 160), (960, 160), (968, 160), (976, 160), (984, 160)]

        self.combined_list = []
        self.combined_list.append(self.platforms)
        self.combined_list.append(self.floor)
        self.combined_list.append(self.pipes)

        # self.floor_list.append(self.floor_list_of)