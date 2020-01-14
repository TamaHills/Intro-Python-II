# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.n_to = self
        self.e_to = self
        self.s_to = self
        self.w_to = self
    def move(self, direction):
        new_room = self.__getattribute__(direction)
        if new_room == self:
            print("you can't move that direction")
            
        return new_room