


class Position():
    def __init__(self, x:int=0, y:int=0) -> None:
        self.x = x
        self.y = y


    def toList(self):
        return [self.x, self.y]


