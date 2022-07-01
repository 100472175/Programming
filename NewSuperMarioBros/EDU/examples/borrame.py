def kikblock(self):
    for i in self.question_block_list:
        if self.big:
            if (self.x - i.x) < 10 and self.y - 16 == \
                    i.x and i.container == "nothing":
                self.question_block_list.remove(i)

        if (self.x - i.x) < 10 and self.y - 16 == i.x:
            if i.container == "coin":
                i.sprite = (16, 16)
                coin1 = Coin(i.x, i.y - 16)
                self.coin_list.append(coin1)

        if (self.x - i.x) < 10 and self.y - 16 == i.x:
            if i.container == "mushroom":
                i = (16, 16)
                mushroom1 = Mushroom(i.x, i.y - 16)
                self.mushroom_list.append(mushroom1)