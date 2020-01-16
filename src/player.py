# Write a class to hold player information, e.g. what room they are in
# currently.
from colors import BLUE, GREEN, RED, BOLD, UNDERLINE, YELLOW, END

class Player:
    def __init__(self, name, room):
        self.room = room
        self.name = name
        self.inventory = []

    def __repr__(self):
        name = f'Name: {BOLD}{self.name}{END}\n'
        
        inventory_header = f'{BOLD}{UNDERLINE}Inventory:{END}\n'
        inventory_string = str().join([ f'{item}' for item in self.inventory])

        return f'{name}{inventory_header}{inventory_string}'

    def take(self, item):
        if item in self.room.items:
            self.room.items.remove(item)
            self.inventory.append(item)
            item.ontake()
        else:
            print(f'{RED}{BOLD}\n{item.name.upper()} CAN\'T BE FOUND IN THIS ROOM\n{END}')
            
    def drop(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.room.items.append(item)
            item.ondrop()
        else:
            print(f'{RED}{BOLD}\n{item.name.upper()} ISN\'T IN YOUR INVENTORY\n{END}')