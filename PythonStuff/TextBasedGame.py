import time

rooms = {
    'Silicon Valley': {'North': 'Amazon', 'South': 'Apple', 'West': 'Github', 'East': 'Google'},
    'Apple': {'North': 'Silicon Valley', 'East': 'Facebook', 'item': 'Root extractor'},
    'Facebook': {'West': 'Apple', 'boss': 'lizard king'},
    'Github': {'East': 'Silicon Valley', 'item': 'repository'},
    'Google': {'West': 'Silicon Valley', 'North': 'NetFlix', 'item': 'Drill'},
    'NetFlix': {'South': 'Google', 'item': 'ad blocker'},
    'Amazon': {'South': 'Silicon Valley', 'East': 'StackOverFlow', 'item': 'Mallet'},
    'StackOverFlow': {'West': 'Amazon', 'item': 'algorithm'}
}
current_room = 'Silicon Valley'
Playing = True
inventory = []


def location(next_room, direction):
    new_room = current_room
    for enter in rooms:
        if enter == new_room and direction in rooms[next_room]:
            new_room = rooms[next_room][direction]
    return new_room


def player_location():
    print(f'# You are entering {current_room} now... '
          f'\n# Your current inventory is {inventory}'
          f'\n##################################################################################')


def player_intructions():
    print(f"##################################################################################\n"
          f"# Welcome to the path to becoming a successful startup.                          #"
          f"\n# In this Game you will need to navigate through 8 rooms.                        #\n"
          f"# Using directions 'North,South,East,West' will control the direction to rooms.  #\n"
          f"# Using the 'Yes/No' command will retrieve the item in the room you are in.      #\n"
          f"# You must collect all items before reaching the lizard king or lose the game.   #\n"
          f"# Defeat the lizard king and make your startup thrive.                           #\n"
          f"# Do you have what it takes to become a successful startup?                      #\n"
          f"##################################################################################")


def items(rooms):
    if 'item' in rooms[current_room] and rooms[current_room]['item'] not in inventory:
        print('There is a', rooms[current_room]['item'])
        decision = input(f"Would you like to take {rooms[current_room]['item']}... ")
        if decision == 'yes':
            inventory.append(rooms[current_room]['item'])
            if rooms[current_room]['item'] == 'algorithm':
                print("Using the I'm not sure where he is algorithm; west, south, south, east,\nyou find that the Lizard king is in FaceBook. ")
            print(rooms[current_room]['item'], 'has been added to your inventory')
            print(inventory)


def game_logic():
    global current_room, Playing
    player_location()
    items(rooms)
    direction = input("Enter a direction you would like to go. --> ").capitalize()
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':
        new_room = location(current_room, direction)
        if new_room == current_room:
            print(f"Error does not compute @.@ Stop banging your head against the wall!!!\n"
                  f"                        ~")
        else:
            current_room = new_room
    else:
        if direction == 'Quit':
            Playing = False
    if 'boss' in rooms[current_room]:
        print("You have entered the lizard king's liar")
        decision = input(f"Would you like to fight the {rooms[current_room]['boss']}... ").capitalize()
        if decision == 'Yes':
            if len(inventory) != 6 and rooms[current_room]['boss'] == 'lizard king':
                print('FAANG has defeated you and stole your source code, better luck next time...')
                print("Game will shut down in 3 seconds...")
                time.sleep(3)
                Playing = False
            else:
                if len(inventory) == 6 and rooms[current_room]['boss'] == 'lizard king':
                    print("You have defeated the lizard king and can now grow your business")
                    print("Game will shut down in 3 seconds...")
                    time.sleep(3)
                    Playing = False

player_intructions()
while Playing:
    game_logic()
