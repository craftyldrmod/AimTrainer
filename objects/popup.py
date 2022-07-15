import random
import pygame as pg

from typeObjects.position import Position
from typeObjects.size import Size
from utils.config import Config






class PopupObject:
    def __init__(self, screen:pg.display) -> None:
        self.name = 'popup'
        self.windowSize = Config.getWindowSize()
        self.size = Size(16, 16)
        self.pos = Position(256, 256)
        self.placed = False
        self.screen = screen
        self.texture = pg.transform.scale(Config.getTexture(self.name), self.size.toList())
        print(type(self.texture))


    def move(self):
        self.pos.x = random.randint(0, self.windowSize.width-self.size.width)
        self.pos.y = random.randint(0, self.windowSize.height-self.size.height)

    def randSize(self):
        self.size.height = random.randint(16, 32)
        self.size.width = random.randint(16, 32)
        self.texture = pg.transform.scale(Config.getTexture(self.name), self.size.toList())


    def render(self):
        if not self.placed:
            self.move()
            self.randSize()
            self.placed = True
        
        self.screen.blit(self.texture, self.pos.toList())

