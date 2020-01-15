import os
import sys
from room import Room
from player import Player
from textwrap import fill

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
def location(player):
    print(f"location: {BOLD}{player.room.name}{END}\n")
    print(f"{GREEN}{fill(player.room.desc, 50)}{END}\n")


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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




#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('adventurer', room['outside'])

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

location(player)

while True:
    cmd = input(f'{BOLD}Enter a direction (n/e/s/w) or \'q\' to quit.\n--> {END}')
    direction = directions.get(cmd.lower())

    if direction:
        clear()
        prev_room = player.room
        player.room = prev_room.next_room(direction)
        location(player)
    elif cmd == 'q':
        clear()
        print(f'\n{BLUE}{UNDERLINE}{BOLD}THANKS FOR PLAYING!{END}\n')
        break
    else:
        clear()
        print(f'\n{RED}{BOLD}INVALID COMMAND\n{END}')
        location(player)