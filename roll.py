import random


class dice_roll:
    def __init__(self):
        # roll
        pass

    def roll(self, num_of_dice):
        # rolls a 'self' sided di 'num_of_dice' times
        x = 0
        total = 0
        while x < (num_of_dice):
            number = random.randint(1, self)
            total += number
            x += 1
        print(total)
