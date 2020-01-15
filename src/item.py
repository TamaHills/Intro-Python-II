from colors import BLUE, GREEN, RED, BOLD, UNDERLINE, END


class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    def ontake(self):
        print(f'{BOLD}{UNDERLINE}{GREEN}PICKED UP {self.name.upper()}{END}\n')
    def ondrop(self):
        print(f'{BOLD}{UNDERLINE}{RED}DROPPED {self.name.upper()}{END}\n')