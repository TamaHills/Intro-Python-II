# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc, items = []):
        self.name = name
        self.desc = desc
        self.n_to = self
        self.e_to = self
        self.s_to = self
        self.w_to = self
        
        self.items = items
    def next_room(self, direction):
        new_room = self.__getattribute__(direction)

        if new_room == self:
            print("\033[91m\033[1m\nYOU CAN'T GO THAT DIRECTION\n\033[0m")
        
        return new_room 