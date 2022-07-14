


class Color():
    def __init__(self, r:int=0, g:int=0, b:int=0) -> None:
        self.r = r
        self.g = g
        self.b = b


    def toList(self):
        return [self.r, self.g, self.b]


