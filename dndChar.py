from roll import dice_roll
import random

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


def create_character():
    if stats["Race"] == 'Dwarf':
        stats["Constitution"] += 2
        stats["Walking Speed"] = 25
    elif stats["Race"] == 'Elf':
        stats["Dexterity"] += 2
        stats["Walking Speed"] = 30
    elif stats["Race"] == 'Halfling':
        stats["Dexterity"] += 2
        stats["Walking Speed"] = 25
    elif stats["Race"] == 'Human':
        for i in [stats]:
            stats[i] += 1
        stats["Walking Speed"] = 30
    elif stats["Race"] == 'Dragonborn':
        stats["Strength"] += 2
        stats["Charisma"] += 1
        stats["Walking Speed"] = 30
    elif stats["Race"] == 'Gnome':
        stats["Intelligence"] += 2
        stats["Walking Speed"] = 25
    elif stats["Race"] == 'Half-elf':
        stats["Charisma"] += 2
        while i <= 2:
            he_score = random.randint(0, 7)
            stats[he_score] += 1
            i += 1
        stats["Walking Speed"] = 30
    elif stats["Race"] == 'Half-orc':
        stats["Strength"] += 2
        stats["Constitution"] += 1
        stats["Walking Speed"] = 30
    elif stats["Race"] == 'Tiefling':
        stats["Intelligence"] += 1
        stats["Charisma"] += 2
        stats["Walking Speed"] = 30

    """for y in range(0, 6):
        mod = stats[y] - 10
        if mod % 2 != 0:
            mod -= 1
        stat_mods[y] = mod / 2
    for x in range(0, 6):
        if stat_mods[x] > 0:
            stat_mod_sign.append('+')
        else:
            stat_mod_sign.append('')"""

    if stats["Class"] == 'Barbarian':
        stats["HP"] += 12
    elif stats["Class"] == 'Bard':
        stats["HP"] += 8
    elif stats["Class"] == 'Cleric':
        stats["HP"] += 8
    elif stats["Class"] == 'Druid':
        stats["HP"] += 8
    elif stats["Class"] == 'Fighter':
        stats["HP"] += 10
    elif stats["Class"] == 'Monk':
        stats["HP"] += 8
    elif stats["Class"] == 'Paladin':
        stats["HP"] += 10
    elif stats["Class"] == 'Ranger':
        stats["HP"] += 10
    elif stats["Class"] == 'Rogue':
        stats["HP"] += 8
    elif stats["Class"] == 'Sorcerer':
        stats["HP"] += 6
    elif stats["Class"] == 'Warlock':
        stats["HP"] += 8
    elif stats["Class"] == 'Wizard':
        stats["HP"] += 6

    # return walking_speed


def printer():
    #mod = ' Mod = '
    print("Race = " + stats["Race"] + " Class = " + stats["Class"])
    print("Walking Speed = " +
          str(stats["Walking Speed"]) + " feet" + " Health = " + str(stats["HP"]))
    print("Alignment = " + stats["Alignment"] +
          " Background = " + stats["Background"])
    print("----------------------------")
    print("Str = " + str(stats["Strength"]))
    print('Dex = ' + str(stats["Dexterity"]))
    print('Const = ' + str(stats["Constitution"]))
    print('Int = ' + str(stats["Intelligence"]))
    print('Wis = ' + str(stats["Wisdom"]))
    print('Char = ' + str(stats["Charisma"]))


create_character()
printer()
