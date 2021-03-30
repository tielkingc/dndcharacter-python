from race import Races
import dndChar
import random

#dice_roll.roll(20, 2)

print(Races.mod_bonus("Dwarf") + 2)

dndChar.stats["Walking Speed"] += 2
print(dndChar.stats["Walking Speed"])
