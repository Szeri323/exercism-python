class Colors:
    def __init__(self):
        self.colors = {
                "black": 0,
                "brown": 1,
                "red": 2,
                "orange": 3,
                "yellow": 4,
                "green": 5,
                "blue": 6,
                "violet": 7,
                "grey": 8,
                "white": 9
            }
    def get_key(self, color):
        return self.colors[color]
    def get_all_keys(self):
        return[key for key in self.colors.keys()]

def color_code(color):
    colors = Colors()
    return colors.get_key(color)


def colors():
    colors = Colors()
    return colors.get_all_keys()
