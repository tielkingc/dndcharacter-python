from dndChar import setup
from race import Races
from dndclass import Classes


def printer():
    # setup.play("run")
    # mod = ' Mod = '
    print("Race = " + setup.play("Race") +
          " Class = " + setup.play("Class"))
    print("Walking Speed = " +
          str(Races(setup.play("Race"))) + " feet" + " Health = " + str(setup.play("HP")))
    print("Alignment = " + setup.play("Alignment") +
          " Background = " + setup.play("Background"))
    print("----------------------------")
    print("Str = " + str(setup.play("Strength")) +
          str(Races(setup.play("Race"))))
    print('Dex = ' + str(setup.play("Dexterity")))
    print('Const = ' + str(setup.play("Constitution")))
    print('Int = ' + str(setup.play("Intelligence")))
    print('Wis = ' + str(setup.play("Wisdom")))
    print('Char = ' + str(setup.play("Charisma")))


# create_character()
printer()
