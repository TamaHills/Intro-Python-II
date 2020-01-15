import os
import sys
from room import Room
from item import Item
from player import Player
from colors import BLUE, GREEN, RED, BOLD, UNDERLINE, END

items = {
    'torch': Item('torch', 'a lit torch'),
    'coins': Item('coins', 'a small bag o\'coins'),
    'pickles': Item('pickles', 'a jar of fancy pickles')
}

# Declare all the rooms
rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons", [items['torch']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. To the west there is a large kitchen"""),

    'kitchen':    Room("Kitchen", """A huge fancy man kitchen. 
The nothern side contains a masive pantry. Heading east returns to the foyer.""", [items['pickles']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['coins']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['foyer'].w_to = rooms['kitchen']
rooms['kitchen'].e_to = rooms['foyer']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']


# clear console output
def clear():
    platform = sys.platform
    if platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    

def parse_cmd(verb, object=None, *args):
    direction = directions.get(verb.lower())
    item = items.get(object)

    if direction:
        prev_room = player.room
        player.room = prev_room.next_room(direction)

    elif verb == 'take' and item:
        player.take(item)

    elif verb == 'drop' and item:
        player.drop(item)

    elif verb == 'q':
        print(f'\n{BLUE}{UNDERLINE}{BOLD}THANKS FOR PLAYING!{END}\n')
        exit()

    else:
        print(f'\n{RED}{UNDERLINE}{BOLD}INVALID COMMAND\n{END}')



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
clear()
player = Player(input(f'{BOLD}enter a name: {END}'), rooms['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = {
    'n': 'n_to',
    'e': 'e_to',
    's': 's_to',
    'w': 'w_to',
    }

clear()
print(f'\n{BLUE}{UNDERLINE}{BOLD}Welcome to the Adventure{END}\n')

print(player)
print(player.room)


while True:
    # read
    cmd = input(f'{BOLD}Enter a direction (n/e/s/w) or \'q\' to quit.\n--> {END}')
    words = cmd.split(' ')
    clear()
    # eval
    parse_cmd(*words)
    # print
    print(player)
    print(player.room)
    # loop