import dndChar


class Classes():
    def __init__(self) -> None:
        # pass
        pass

    def health(self):
        if self == 'Barbarian':
            dndChar.stats["HP"] += 12
        elif self == 'Bard':
            dndChar.stats["HP"] += 8
        elif self == 'Cleric':
            dndChar.stats["HP"] += 8
        elif self == 'Druid':
            dndChar.stats["HP"] += 8
        elif self == 'Fighter':
            dndChar.stats["HP"] += 10
        elif self == 'Monk':
            dndChar.stats["HP"] += 8
        elif self == 'Paladin':
            dndChar.stats["HP"] += 10
        elif self == 'Ranger':
            dndChar.stats["HP"] += 10
        elif self == 'Rogue':
            dndChar.stats["HP"] += 8
        elif self == 'Sorcerer':
            dndChar.stats["HP"] += 6
        elif self == 'Warlock':
            dndChar.stats["HP"] += 8
        elif self == 'Wizard':
            dndChar.stats["HP"] += 6
