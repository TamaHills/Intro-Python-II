from colors import BLUE, GREEN, RED, YELLOW, BOLD, BRIGHT, UNDERLINE, END

class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return f'{BOLD}{BRIGHT}{self.name}{END} - {BRIGHT}{self.desc}{END}\n'

    def ontake(self, player):
        print(f'{BOLD}{UNDERLINE}{GREEN}{player.name.upper()} PICKED UP {self.name.upper()}{END}\n')

    def ondrop(self, player):
        print(f'{BOLD}{UNDERLINE}{YELLOW}{player.name.upper()} DROPPED {self.name.upper()}{END}\n')


class Treasure(Item):
    def __init__(self, name, desc, value=0):
        super().__init__(name, desc)
        self.value = value

    def __repr__(self):
        return f'{BOLD}{YELLOW}{self.name}{END} - {self.desc}{YELLOW} ${self.value}{END}\n'

    def ontake(self, player):
        super().ontake(player)
        player.value += self.value

    def ondrop(self, player):
        super().ondrop(player)
        player.value -= self.value

class Usable

class WinItem(Item):
    def __init__(self, name, desc):
        super().__init__(name, desc)
    def ontake(self, player):
        player.win = True


