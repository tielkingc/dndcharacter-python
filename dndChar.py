import random
from roll import dice_roll


class setup():
    def __init__(self) -> None:
        # pass
        pass

    def play(self):
        races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn',
                 'Gnome', 'Half-elf', 'Half-orc', 'Tiefling']
        classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
                   'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
        alignment = ['Lawful Good', 'Neutral Good', 'Chaotic Good', 'Lawful Neutral',
                     'Neutral', 'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil', 'Chaotic Evil']
        backgrounds = ['Acolyte', 'Charlatan', 'Criminal/Spy', 'Entertainer', 'Folk Hero', 'Gladiator',
                       'Hermit', 'Knight', 'Noble', 'Outlander', 'Pirate', 'Sage', 'Sailor', 'Soldier', 'Urchin']
        stat_mod_sign = []

        stats = {
            "Race": races[random.randint(0, 8)],
            "Class": classes[random.randint(0, 11)],
            "Walking Speed": 0,
            "HP": 0,
            "Alignment": alignment[random.randint(0, 8)],
            "Background": backgrounds[random.randint(0, 14)],
            "Strength": dice_roll.roll(6, 4),
            "Dexterity": dice_roll.roll(6, 4),
            "Constitution": dice_roll.roll(6, 4),
            "Intelligence": dice_roll.roll(6, 4),
            "Wisdom": dice_roll.roll(6, 4),
            "Charisma": dice_roll.roll(6, 4)
        }
        return stats[self]


"""def create_character():
    for y in range(0, 6):
        mod = stats[y] - 10
        if mod % 2 != 0:
            mod -= 1
        stat_mods[y] = mod / 2
    for x in range(0, 6):
        if stat_mods[x] > 0:
            stat_mod_sign.append('+')
        else:
            stat_mod_sign.append('')"""

# return walking_speed
