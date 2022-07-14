import pygame as pg

from popup import PopupBlock
import config




bgColor = (0, 0, 0)
CUBE_SIZE = 32



class Game:
    def __init__(self) -> None:
        pg.init()
        pg.font.init()

        self.fps = 60
        self.screen = pg.display.set_mode((config.WIDTH, config.HEIGHT), pg.RESIZABLE)
        pg.display.set_caption('Aim Trainer')
        pg.display.set_icon(pg.image.load('icon.png'))

        self.blocks = [PopupBlock(self.screen)]
        self.clock = pg.time.Clock()
        self.clicked = 0
        self.missed = 0
        self.time = 0


    def render(self):
        for block in self.blocks:
            block.render()

        self.renderStats()

    def renderStats(self):
        font = pg.font.SysFont('Arial', 20)

        clicksText = font.render(f'Clicked: {self.clicked}', False, [255, 255, 255])
        self.screen.blit(clicksText, [8, 8])
        missedText = font.render(f'Missed: {self.missed}', False, [255, 255, 255])
        self.screen.blit(missedText, [8, 38])

        fpsText = font.render(f'Seconds: {round(self.time/self.fps)}', False, [255, 255, 255])
        self.screen.blit(fpsText, [8, 68])


    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    for i, block in enumerate(self.blocks):
                        x = event.pos[0]-block.size.width
                        y = event.pos[1]-block.size.height

                        if block.pos.x >= x and block.pos.x <= x+block.size.width:
                            if block.pos.y >= y and block.pos.y <= y+block.size.height:
                                self.blocks.pop(i)
                                self.blocks.append(PopupBlock(self.screen))
                                self.clicked += 1
                                continue
                            continue

                        self.missed += 1

                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            
            self.time += 1

            self.screen.fill(bgColor)
            self.render()

            pg.display.update()
            self.clock.tick(self.fps)




if __name__ == '__main__':
    game = Game()
    game.run()
