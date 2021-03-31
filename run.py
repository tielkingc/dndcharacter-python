from dndChar import setup
from race import Races
from dndclass import Classes


def printer():
    race = Races(setup.play("Race"))
    health = Classes(setup.play("Class"))
    strength = setup.play("Strength") + race.str
    if (strength - 10) % 2 != 0:
        strength_mod = (strength - 1) / 2
    else:
        strength_mod = strength / 2
    dexterity = setup.play("Dexterity") + race.dex
    constitution = setup.play("Constitution") + race.con
    intelligence = setup.play("Intelligence") + race.int
    wisdom = setup.play("Wisdom") + race.wis
    charisma = setup.play("Charisma") + race.cha
    print("Race = " + setup.play("Race") +
          " Class = " + setup.play("Class"))
    print("Walking Speed = " +
          str(race.walking) + " feet" + " Health = " + str(health.hp))
    print("Alignment = " + setup.play("Alignment") +
          " Background = " + setup.play("Background"))
    print("----------------------------")
    print("Str = " + str(strength))
    print('Dex = ' + str(dexterity))
    print('Const = ' + str(constitution))
    print('Int = ' + str(intelligence))
    print('Wis = ' + str(wisdom))
    print('Char = ' + str(charisma))


# create_character()
printer()
