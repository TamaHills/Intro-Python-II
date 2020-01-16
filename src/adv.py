import os
import sys
from textwrap import fill
from game_map import starting_room, lettuce
from player import Player
from colors import BLUE, GREEN, RED, BOLD, UNDERLINE, BRIGHT, END, YELLOW

#helper dictionary
directions = {
    'n': 'n_to',
    'e': 'e_to',
    's': 's_to',
    'w': 'w_to',
}

# clear console output
def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    
def print_help():
    print(f"""\{BRIGHT}
Press 'q' to quit
Pickup items in room with 'take <item>'
Drop items in room with 'drop <item>'{END}

{YELLOW}yellow items are treasure and add to users treasure value{END}
{BLUE}blue items are usable, with 'use <item>'{END}
""")

def parse_cmd(verb, object=None, *args):
    direction = directions.get(verb.lower())
    room = player.room
    if direction:
        
        player.travel(room.next_room(direction))
    elif verb == 'help':
        print_help()
    elif verb == 'take' and room.hasitem(object):
        player.take(object)

    elif verb == 'drop' and player.hasitem(object):
        player.drop(object)

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
print(f'\n{BLUE}{UNDERLINE}{BOLD}Wash Your Lettuce{END}\n')

print(fill(f"""{BLUE}\
You're a weary traveler whos seeks a magic cave where you can wash your lettuce.
You have been traveling for many days, and have reached the cave. 
What trials will await you inside?
{END}"""))
player = Player(input(f'\n{BOLD}enter a name: {END}'), starting_room, [lettuce])

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



clear()


print(player)
print(player.room)


while not player.win:
    # read
    cmd = input(f'{BOLD}Enter a direction (n/e/s/w) or \'help\' for all commands\n--> {END}')
    words = cmd.split(' ')
    clear()
    # eval
    parse_cmd(*words)
    # print
    print(player)
    print(player.room)
    # loop

clear()

print(f'{GREEN}CONGRATS YOU\'VE WON!{END}')
print(f'{BOLD}{YELLOW}YOU FOUND ${player.value} WORTH OF TREASURE{END}')