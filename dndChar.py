import random

races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-elf', 'Half-orc', 'Tiefling']
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
alignment = ['Lawful Good', 'Neutral Good', 'Chaotic Good', 'Lawful Neutral', 'Neutral', 'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil', 'Chaotic Evil']
backgrounds = ['Acolyte', 'Charlatan', 'Criminal/Spy', 'Entertainer', 'Folk Hero', 'Gladiator', 'Hermit', 'Knight', 'Noble', 'Outlander', 'Pirate', 'Sage', 'Sailor', 'Soldier', 'Urchin']
stats = [0, 0, 0, 0, 0, 0]
stat_mods = [0, 0, 0, 0, 0, 0]
stat_mod_sign = [ ]
walking_speed = 1
hp = 0
user_race = races[random.randint(0,8)]
user_class = classes[random.randint(0,11)]
user_align = alignment[random.randint(0,9)]
user_back = backgrounds[random.randint(0,14)]

def roll_dice():
    for i in range(0,6):
        dice = 0
        stat_add = 0
        while dice <= 4:
            stat_add += random.randint(1,6)
            dice += 1
        stats[i] = stat_add

def create_character():
    if user_race == 'Dwarf':
        stats[2] += 2
        walking_speed = 25
    elif user_race == 'Elf':
        stats[1] += 2
        walking_speed = 30
    elif user_race == 'Halfling':
        stats[1] += 2
        walking_speed = 25
    elif user_race == 'Human':
        for i in [stats]:
            stats[i] += 1
        walking_speed = 30
    elif user_race == 'Dragonborn':
        stats[0] += 2
        stats[5] += 1
        walking_speed = 30
    elif user_race == 'Gnome':
        stats[3] += 2
        walking_speed = 25
    elif user_race == 'Half-elf':
        stats[5] += 2
        while i <= 2:
            he_score = random.randint(0,7)
            stats[he_score] += 1
            i += 1
        walking_speed = 30
    elif user_race == 'Half-orc':
        stats[0] += 2
        stats[2] += 1
        walking_speed = 30
    elif user_race == 'Tiefling':
        stats[3] += 1
        stats[5] += 2
        walking_speed = 30

    for y in range(0,6):
        mod = stats[y] - 10
        if mod % 2 != 0:
            mod -= 1
        stat_mods[y] = mod / 2
    for x in range(0,6):
        if stat_mods[x] > 0:
            stat_mod_sign.append('+')
        else:
            stat_mod_sign.append('')

    if user_class == 'Barbarian':
        hp = 12 + stat_mods[3]
    elif user_class == 'Bard':
        hp = 8 + stat_mods[3]
    elif user_class == 'Cleric':
        hp = 8 + stat_mods[3]
    elif user_class == 'Druid':
        hp = 8 + stat_mods[3]
    elif user_class == 'Fighter':
        hp = 10 + stat_mods[3]
    elif user_class == 'Monk':
        hp = 8 + stat_mods[3]
    elif user_class == 'Paladin':
        hp = 10 + stat_mods[3]
    elif user_class == 'Ranger':
        hp = 10 + stat_mods[3]
    elif user_class == 'Rogue':
        hp = 8 + stat_mods[3]
    elif user_class == 'Sorcerer':
        hp = 6 + stat_mods[3]
    elif user_class == 'Warlock':
        hp = 8 + stat_mods[3]
    elif user_class == 'Wizard':
        hp = 6 + stat_mods[3]

    #return walking_speed

def printer():
    print("Race = " + user_race + " Class = " + user_class)
    print("Walking Speed = " + str(walking_speed) + " feet" + " HP = " + str(hp))
    print("Alignment = " + user_align + " Background = " + user_back)
    print("----------------------------")
    print("Str = " + str(stats[0]) + ' Mod = ' + stat_mod_sign[0] + str(stat_mods[0]))
    print('Dex = ' + str(stats[1]) + ' Mod = ' + stat_mod_sign[1] + str(stat_mods[1]))
    print('Const = ' + str(stats[2]) + ' Mod = ' + stat_mod_sign[2] + str(stat_mods[2]))
    print('Int = ' + str(stats[3]) + ' Mod = ' + stat_mod_sign[3] + str(stat_mods[3]))
    print('Wis = ' + str(stats[4]) + ' Mod = ' + stat_mod_sign[4] + str(stat_mods[4]))
    print('Char = ' + str(stats[5]) + ' Mod = ' + stat_mod_sign[5] + str(stat_mods[5]))


roll_dice()
create_character()
printer()
