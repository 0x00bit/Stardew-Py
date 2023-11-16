import pygame, sys
import settings
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCR_WID,settings.SCR_HEI))
        self.game_clock = pygame.time.Clock()
        pygame.display.set_caption("Py Land")
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.QUIT
                    sys.exit()

            dt = self.game_clock.tick(60)/1000 # frame rate
            self.level.run(dt)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()