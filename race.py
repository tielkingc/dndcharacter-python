from dndChar import setup
import random


class Races():
    def __init__(self, race):
        # pass
        self.con = setup.play("Constitution")
        self.str = setup.play("Strength")
        self.dex = setup.play("Dexterity")
        self.int = setup.play("Intelligence")
        self.wis = setup.play("Wisdom")
        self.cha = setup.play("Charisma")
        self.walking = "Walking Speed"
        if race == 'Dwarf':
            self.con += 2
            self.walking = 25
        elif race == 'Elf':
            self.dex += 2
            self.walking = 30
        elif race == 'Halfling':
            self.dex += 2
            self.walking = 25
        elif race == 'Human':
            self.str += 1
            self.dex += 1
            self.con += 1
            self.int += 1
            self.wis += 1
            self.cha += 1
            self.walking = 30
        elif race == 'Dragonborn':
            self.str += 2
            self.cha += 1
            self.walking = 30
        elif race == 'Gnome':
            self.int += 2
            self.walking = 25
        elif race == 'Half-elf':
            self.cha += 2
            i = 0
            while i <= 2:
                he_score = random.randint(0, 5)
                sta = [self.str, self.dex, self.con,
                       self.int, self.wis, self.cha]
                sta[he_score] += 1
                i += 1
            self.walking = 30
        elif race == 'Half-orc':
            self.str += 2
            self.con += 1
            self.walking = 30
        elif race == 'Tiefling':
            self.int += 1
            self.cha += 2
            self.walking = 30
