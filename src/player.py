# Write a class to hold player information, e.g. what room they are in
# currently.


deadend = "Nowhere to go in that direction. Try a different direction."


class Player:
    def __init__(self, name, location, items=[]):
        self.name = name
        self.location = location
        self.items = items
        self.path = []

    def move(self, direction):
        if direction == ('north' or 'n'):
            if hasattr(self.location, 'n_to'):
                self.location = self.location.n_to
                self.path.append('south')
            else:
                print(deadend)
        elif direction == ('south' or 's'):
            if hasattr(self.location, 's_to'):
                self.location = self.location.s_to
                self.path.append('north')
            else:
                print(deadend)
        elif direction == ('west' or 'w'):
            if hasattr(self.location, 'w_to'):
                self.location = self.location.w_to
                self.path.append('east')
            else:
                print(deadend)
        elif direction == ('east' or 'e'):
            if hasattr(self.location, 'e_to'):
                self.location = self.location.e_to
                self.path.append('west')
            else:
                print(deadend)
        elif direction == ('back'):
            if len(self.path) > 0:
                if self.path[-1] == 'north':
                    self.location = self.location.n_to
                    self.path.pop()
                elif self.path[-1] == 'south':
                    self.location = self.location.s_to
                    self.path.pop()
                elif self.path[-1] == 'west':
                    self.location = self.location.w_to
                    self.path.pop()
                elif self.path[-1] == 'east':
                    self.location = self.location.e_to
                    self.path.pop()
            else:
                print("***You've only just started, there is nowhere to go back to.***")

    def inventory(self):
        if len(self.items) > 0:
            print("***You look over your inventory:***")
            for item in self.items:
                print(item.name)
        else:
            print("***You don't have anything with you.***")

    def recieveitem(self, item):
        self.items.append(item)
        print(f"***You put {item.name.upper()} in your inventory.***")

    def dropitem(self, itemname):
        if next(item for item in self.items if item.name.lower() == itemname):
            item = next(
                item for item in self.items if item.name.lower() == itemname)
            self.items.remove(item)
            return item
        else:
            return False
