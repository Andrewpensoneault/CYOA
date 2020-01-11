class Character():
    def __init__(self,character_name):
        """Initializes the Character class with a name"""
        self.name = character_name
        self.description = None
        self.dialog = None
        self.item = None
    
    def set_description(self, character_description):
        """Sets the Character description"""
        self.description = character_description

    def get_description(self):
        """Returns the Character description"""
        return self.description
    
    def describe(self):
        """Prints the character description"""
        print(self.description)

    def set_item(self, new_item):
        """Sets the Character's held item"""
        self.item = new_item

    def get_item(self):
        """Returns the Character's held item"""
        return self.item

    def steal(self):
        """Returns the Character's item if an item is held"""
        if self.item is not None:
            print('You steal ' + self.item + ' from ' + self.name)
        else:
            print(self.name + ' has no item')

    def get_name(self):
        """Returns the Character's name"""
        return self.name

    def set_dialog(self, character_dialog):
        """Sets the Character's dialog""" 
        self.dialog = character_dialog

    def talk(self):
        """Prints the Character's dialog"""
        print('[' + self.name + ' says' + ']: ' + self.dialog)

    def fight(self, combat_item):
        """Prints the Character's fighting rejection line"""
        print(self.name + ' does not want to fight you')
        return True

class Enemy(Character):
    number_dead_enemy = 0
    def __init__(self,character_name):
        """Initializes the Enemy subclass with a name"""
        super().__init__(character_name)
        self.weakness = None

    def set_weakness(self, weakness_name):
        """Sets the Enemy's weakness"""
        self.weakness = weakness_name

    def get_weakness(self):
        """Returns the Enemy's weakness"""
        return self.weakness

    def talk(self):
        """Prints the Enemy's rejection line"""
        print(self.name + ' does not want to talk')

    def fight(self, combat_item):
        """Fights the enemy, returns if the weakness is chosen and false otherwise"""
        if combat_item == self.weakness:
            print('You fought off ' + self.name + ' with the ' + combat_item)
            Enemy.number_dead_enemy +=1
            return True
        else:
            print('You lost the fight and were killed by ' + self.name)
            return False