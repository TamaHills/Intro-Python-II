import os
import sys
from room import Room
from item import Item
from player import Player
from textwrap import fill

items = {
    'torch': Item('torch', 'a lit torch'),
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons", [items['torch']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# helpers to control console output
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

# clear console output
def clear():
    platform = sys.platform
    if platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

# print player location
def player_info(player):
    print(f'Name: {BOLD}{player.name}{END}')
    print(f'{BOLD}{UNDERLINE}Inventory:{END}')
    for item in player.inventory:
        print(f'    *{BOLD}{item.name}{END} - {item.desc}')

    print(f'\nlocation: {BOLD}{player.room.name}{END}\n')
    print(f'{GREEN}{fill(player.room.desc)}{END}\n')

    print(f'{BOLD}{UNDERLINE}Items:{END}')
    for item in player.room.items:
        print(f'    *{BOLD}{item.name}{END} - {item.desc}')
    
def parse_verb(cmd, object_name=None):
    direction = directions.get(cmd.lower())
    object = items.get(object_name)
    if direction:
        clear()
        prev_room = player.room
        player.room = prev_room.next_room(direction)

    elif cmd == 'get' and object:
        player.room.items.remove(object)
        player.inventory.append(object)
        clear()

    elif cmd == 'drop' and object:
        player.inventory.remove(object)
        player.room.items.append(object)
        clear()

    elif cmd == 'q':
        clear()
        print(f'\n{BLUE}{UNDERLINE}{BOLD}THANKS FOR PLAYING!{END}\n')
        exit()
    else:
        clear()
        print(f'\n{RED}{BOLD}INVALID COMMAND\n{END}')





#
# Main
#

# Make a new player object that is currently in the 'outside' room.
clear()
player = Player(input(f'{BOLD}enter a name: {END}'), room['outside'])

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

player_info(player)

while True:
    cmd = input(f'{BOLD}Enter a direction (n/e/s/w) or \'q\' to quit.\n--> {END}')
    words = cmd.split(' ')
    print(words)
    parse_verb(*words)
    player_info(player)
        
    