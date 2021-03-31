import dndChar


class Classes():
    def __init__(self, classes):
        self.hp = 0
        if classes == 'Barbarian':
            self.hp = 12
        elif classes == 'Bard':
            self.hp = 8
        elif classes == 'Cleric':
            self.hp = 8
        elif classes == 'Druid':
            self.hp = 8
        elif classes == 'Fighter':
            self.hp = 10
        elif classes == 'Monk':
            self.hp = 8
        elif classes == 'Paladin':
            self.hp = 10
        elif classes == 'Ranger':
            self.hp = 10
        elif classes == 'Rogue':
            self.hp = 8
        elif classes == 'Sorcerer':
            self.hp = 6
        elif classes == 'Warlock':
            self.hp = 8
        elif classes == 'Wizard':
            self.hp = 6
