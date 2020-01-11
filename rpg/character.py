class Character():
    #a class for characters
    def __init__(self,character_name):
        self.name = character_name
        self.description = None
        self.dialog = None
        self.item = None
    
    def set_description(self, character_description):
        self.description = character_description

    def get_description(self):
        return self.description

    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item

    def get_name(self):
        return self.name

    def describe(self):
        #prints the description of a character
        print(self.description)

    def set_dialog(self, character_dialog):
        self.dialog = character_dialog

    def talk(self):
        #prints the dialog
        print('[' + self.name + ' says' + ']: ' + self.dialog)

    def fight(self, combat_item):
        #attempts to fight a character
        print(self.name + ' does not want to fight you')
        return True
    
    def steal(self):
        if self.item is not None:
            print('You steal ' + self.item + ' from ' + self.name)
        else:
            print(self.name + ' has no item')

class Enemy(Character):
    number_dead_enemy = 0
    def __init__(self,character_name):
        super().__init__(character_name)
        self.weakness = None

    def set_weakness(self, weakness_name):
        self.weakness = weakness_name

    def get_weakness(self):
        return self.weakness

    def talk(self):
       #attempts to talk
        print(self.name + ' does not want to talk')

    def fight(self, combat_item):
        #attempts to fight
        if combat_item == self.weakness:
            print('You fought off ' + self.name + ' with the ' + combat_item)
            Enemy.number_dead_enemy +=1
            return True
        else:
            print('You lost the fight and were killed by ' + self.name)
            return False