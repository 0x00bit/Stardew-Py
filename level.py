import pygame
import settings
from player import Player

class Level:

    def __init__(self):
        #get display surface
        self.display_surface = pygame.display.get_surface()

        #sprite groups
        self.sprites = pygame.sprite.Group()

        self.setup()
    
    def setup(self):
        self.player = Player((640,360), self.sprites)

    def run(self,dt):
        self.display_surface.fill('black')
        self.sprites.draw(self.display_surface)
        self.sprites.update(dt)

    