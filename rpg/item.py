class Item():
    def __init__(self,item_name):
        """Initializes the Item class with a name"""
        self.name = item_name
        self.description = None
    
    def set_description(self, item_description):
        """Sets the Item description"""
        self.description = item_description

    def get_description(self):
        """Return the Item description"""
        return self.description

    def get_name(self):
        """Return the Item's name"""
        return self.name

    def describe(self):
        """Prints the Item description"""
        print(self.description)
