import random


class dice_roll:
    def __init__(self):
        # roll
        pass

    def d20(self):
        # rolls a d20 'x' times
        x = 0
        while x < (self):
            number = random.randint(1, 20)
            x += 1
            print(number)

    def d100(self):
        # rolls a percentile 'x' times
        x = 0
        while x < (self):
            number = random.randint(1, 100)
            x += 1
            print(number)

    def d10(self):
        # rolls a d10 'x' times
        x = 0
        while x < (self):
            number = random.randint(1, 10)
            x += 1
            print(number)

    def d8(self):
        # rolls a d8 'x' times
        x = 0
        while x < (self):
            number = random.randint(1, 8)
            x += 1
            print(number)

    def d6(self):
        # rolls a d6 'x' times
        x = 0
        while x < (self):
            number = random.randint(1, 6)
            x += 1
            print(number)

    def d4(self):
        # rolls a d4 'x' times
        x = 0
        while x < (self):
            number = random.randint(1, 4)
            x += 1
            print(number)

    def d12(self):
        # rolls a 12 'x' times
        x = 0
        while x < (self):
            number = random.randint(1, 12)
            x += 1
            print(number)


# dice_roll.d10(2)


"""def roll():
    number = 0
    count = 0
    while count < 4:
        print(count)
        number += random.randint(1, 6)
        count += 1
    return number


test = {
    "a": roll(),
    "b": 2
}

print(test["a"])"""
