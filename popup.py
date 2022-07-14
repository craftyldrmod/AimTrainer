import random
import pygame as pg

from base.color import Color
from base.position import Position
from base.size import Size
import config






class PopupBlock:
    def __init__(self, screen:pg.display) -> None:
        self.size = Size(32, 32)
        self.pos = Position(256, 256)
        self.color = Color(0, 255, 0)
        self.placed = False
        self.screen = screen


    def move(self):
        self.pos.x = random.randint(0, config.WIDTH-self.size.width)
        self.pos.y = random.randint(0, config.HEIGHT-self.size.height)


    def render(self):
        if not self.placed:
            self.move()
            self.placed = True


        blockRect = pg.Rect(self.pos.x, self.pos.y, self.size.width, self.size.height)

        pg.draw.rect(self.screen, self.color.toList(), blockRect)

