# Implement a class to hold room information. This should have name and
# description attributes.
from textwrap import fill

from colors import GREEN, RED, BOLD, UNDERLINE, END

class Room:
    def __init__(self, name, desc, items = []):
        self.name = name
        self.desc = desc
        self.n_to = self
        self.e_to = self
        self.s_to = self
        self.w_to = self

        self.items = items

    def __repr__(self):
        location = f'location: {BOLD}{self.name}{END}'
        desc = f'{GREEN}{fill(self.desc)}{END}\n'
        info_string = f'{location}\n{desc}\n'

        item_header = f'{BOLD}{UNDERLINE}Items:{END}\n'
        items_string = str().join([ f'{item}' for item in self.items])
        
        return f'{info_string}{item_header}{items_string}'

    def next_room(self, direction):
        new_room = self.__getattribute__(direction)

        if new_room == self:
            print(f"{RED}{BOLD}\nYOU CAN'T GO THAT DIRECTION\n{END}")
        
        return new_room 