# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.room = room
        self.name = name
        self.inventory = []
    def get(self, item):
        if item in self.room.items:
            self.room.items.remove(item)
            self.inventory.append(item)
        else:
            print(f'\033[91m\033[1m\n{item.name.upper()} CAN\'T BE FOUND IN THIS ROOM\n\033[0m')
            
    def drop(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.room.items.append(item)
        else:
            print(f'\033[91m\033[1m\n{item.name.upper()} ISN\'T IN YOUR INVENTORY\n\033[0m')