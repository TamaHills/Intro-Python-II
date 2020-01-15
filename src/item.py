from colors import BLUE, GREEN, RED, YELLOW, BOLD, UNDERLINE, END


class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    def ontake(self):
        print(f'{BOLD}{UNDERLINE}{GREEN}PICKED UP {self.name.upper()}{END}\n')
    def ondrop(self):
        print(f'{BOLD}{UNDERLINE}{YELLOW}DROPPED {self.name.upper()}{END}\n')

class Win_Item(Item):
    def __init__(self, name, desc)
        super().__init__(name, desc)
        