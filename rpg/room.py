class Room():
    #Class for creating rooms in a Chose Your Own Adventure
    def __init__(self,room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.cardinal_directions =  ('north','south','east','west')
        self.character = None
        self.item = None

    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character
    
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description)
    
    def link_room(self,room_to_link,direction):
        # links one way the provided room to self
        is_cardinal_direction = direction.lower() in self.cardinal_directions
        assert is_cardinal_direction, direction +' is not a cardinal direction'
        direction = direction.lower()
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        # gets surrounding rooms and description
        print(self.name)
        print('--------------------------')
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)
        if self.character is not None:
            print(self.character.name + ' is here' )

    def move(self, direction):
        # Method for moving between rooms
        is_cardinal_direction = direction.lower() in self.cardinal_directions
        assert is_cardinal_direction, direction +' is not a cardinal direction'
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
