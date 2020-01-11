class Room():
    """Class for creating rooms in a Chose Your Own Adventure"""
    def __init__(self,room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.cardinal_directions =  ('north','south','east','west')
        self.character = None
        self.item = None

    def set_item(self, new_item):
        """Sets the Room's item"""
        self.item = new_item

    def get_item(self):
        """Returns the Room's item """
        return self.item

    def set_character(self, new_character):
        """Sets the Room's Character"""
        self.character = new_character

    def get_character(self):
        """Returns the Room's Character"""
        return self.character
    
    def set_description(self, room_description):
        """Sets the Room's description"""
        self.description = room_description

    def get_description(self):
        """Returns the Room's description"""
        return self.description

    def describe(self):
        """Prints the Room's description"""
        print(self.description)

    def get_name(self):
        """Returns the Room's name"""
        return self.name
    
    def link_room(self,room_to_link,direction):
        """Adds a room to the linked_room dictionary associated with a room if cardinal direction is given"""
        is_cardinal_direction = direction.lower() in self.cardinal_directions
        assert is_cardinal_direction, direction +' is not a cardinal direction'
        direction = direction.lower()
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """Prints the Room's name, description, surrounding rooms, item, and character"""
        print(self.name)
        print('--------------------------')
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)
        if self.item is not None:
            print('A ' + self.item.get_name() + ' is here' )
        if self.character is not None:
            print(self.character.get_name() + ' is here' )

    def move(self, direction):
        # Method for moving between rooms
        is_cardinal_direction = direction.lower() in self.cardinal_directions
        assert is_cardinal_direction, direction +' is not a cardinal direction'
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
