from room import Room
from item import Item, WinItem, Treasure
from colors import BLUE, GREEN, RED, BOLD, UNDERLINE, END

lettuce = Item('lettuce', 'a head of lettuce it needs to be washed.')

items = {
    'lantern': WinItem('lantern', 'a very bright lamp to guide my way'),
    'coins': Treasure('coins', 'a small bag o\'coins', 50),
    'pickles': Treasure('pickles', f'a jar of {BOLD}{UNDERLINE}very{END} fancy pickles', 150)
}

# Declare all the rooms
rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons", [items['lantern']], ),

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

starting_room = rooms['outside']