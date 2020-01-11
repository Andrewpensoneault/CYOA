from rpg import Item, Character, Enemy, Room
from os import system, name


def clear(): 
    """ method for clearing line """
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# Defines Rooms

entry_way = Room('Entry Way')
entry_way.set_description('An eerie and spooky hallway')

kitchen = Room('Kitchen')
kitchen.set_description('A long abandoned kitchen')

bathroom = Room('Bathroom')
bathroom.set_description('A musty dark bathroom')

pantry = Room('Pantry')
pantry.set_description('Full of old expired canned goods')

parlor = Room('Parlor')
parlor.set_description('A once mighty parlor, now covered in dust and cobwebs')

living_room = Room('Living Room')
living_room.set_description('A scary looking living room')

# Adds connections

entry_way.link_room(kitchen,'north')
kitchen.link_room(entry_way,'south')

kitchen.link_room(pantry,'north')
pantry.link_room(kitchen,'south')

entry_way.link_room(living_room,'east')
living_room.link_room(entry_way,'west')

entry_way.link_room(bathroom,'west')
bathroom.link_room(entry_way,'east')

living_room.link_room(parlor,'north')
parlor.link_room(living_room,'south')

parlor.link_room(kitchen,'west')
kitchen.link_room(parlor,'east')


#Defines Characters

tom = Character('Tom')
tom.set_description('A boring guy')
tom.set_dialog('Hello')
tom.set_item('sword')

thief = Enemy('Thief')
thief.set_description('A dangerous thief')
thief.set_weakness('sword')

#Defines Item

sword = Item('sword')
sword.set_description('A shiny and powerful sword')
bathroom.set_item(sword)


entry_way.set_character(tom)
parlor.set_character(thief)

#Runs Game
cardinal_directions  = ('north','south','east','west')
current_room = entry_way
alive = True
backpack = []
clear()

while True:
    print('\n')
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    clear()
    if command.lower() in cardinal_directions:
        #Move in a direction
        current_room = current_room.move(command)

    elif command.lower() == 'talk':
        #Talk to character
        if current_room.get_character() is None:
            print('No one is here to talk to')
        else:
            current_room.get_character().talk()

    elif command.lower() == 'steal':
        #Talk to character
        if current_room.get_character() is None:
            print('No one is here to steal from')
        else:
            current_room.get_character().steal()
            if current_room.get_character().get_item() is None:
                pass
            else:
                backpack.append(current_room.get_character().get_item())
                current_room.get_character().set_item(None)

    elif command.lower() == 'backpack':
        #check your inventory
        print('You have the following items in your backpack:')
        for item in backpack:
            print(item)

    elif command.lower() == 'fight':
        #Fight character
        if current_room.get_character() is None:
            print('There is no one to fight')
        else:
            fight_item = input('Choose your weapon> ')
            if fight_item not in backpack:
                print('You do not have a ' + fight_item + ' in your backpack')
                print('You have the following items in your backpack:')
                for item in backpack:
                    print(item)
            else:
                alive = current_room.get_character().fight(fight_item)
                if alive == True and isinstance(current_room.get_character(),Enemy):
                    current_room.set_character(None)
                    if Enemy.number_dead_enemy >= 1:
                        print('You won the game')
                        break
    
    elif command.lower() == 'take':
        #Fight character
        if current_room.get_item() is None:
            print('There is no item to take')
        else:
            print('You took the ' + current_room.get_item().get_name())
            backpack.append(current_room.get_item().get_name())
            current_room.set_item(None)

    elif command.lower() == 'help':
        valid_commands = ('north','south','east','west','fight','steal','talk','take','backpack','help','exit','quit')
        print('You can type any of the following commands')
        for text in valid_commands:
            print(text)


    elif command.lower() in ('exit','quit'):
        #End the game
        break

    else:
        print('Command not recognized')
    
    if alive == False:
        break
print('The End')