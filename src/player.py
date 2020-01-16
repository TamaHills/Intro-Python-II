# Write a class to hold player information, e.g. what room they are in
# currently.
from colors import BLUE, GREEN, RED, BOLD, UNDERLINE, YELLOW, END

class Player:
    def __init__(self, name, room, inv=[]):
        self.room = room
        self.name = name
        self.inventory = inv
        self.win = False
        self.value=0

    def __repr__(self):
        name = f'Name: {BOLD}{self.name}{END}\n'
        treasure = f'Treasure Value: {BOLD}{YELLOW}${self.value}{END}\n'
        inventory_header = f'{BOLD}{UNDERLINE}Inventory:{END}\n'
        inventory_string = str().join([ f'  *{item}' for item in self.inventory])

        return f'{name}{treasure}{inventory_header}{inventory_string}'

    def hasitem(self, item_name):
        return item_name in self.item_names()

    def item_names(self):
        return [item.name for item in self.inventory]

    def travel(self, room):
        self.room = room

    def take(self, item_name):
        item_index = self.room.item_names().index(item_name)
        item = self.room.items[item_index]
        self.room.items.remove(item)
        self.inventory.append(item)
        item.ontake(self)
            
    def drop(self, item_name):
        item_index = self.item_names().index(item_name)
        item = self.inventory[item_index]
        self.inventory.remove(item)
        self.room.items.append(item)
        item.ondrop(self)