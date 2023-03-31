import pygame
from setting import settings

class Alinegame:
    def __init__(self):
        pygame.init()
        self.settings = settings()
        pygame.display.set_caption("Alien Invasion")
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.bg_color = self.settings.bg_color
#        self.icon = pygame.display.set_icon("./alien-in.jpg")
    
    def runner(self):
        x = True
        while x:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x=False
                    break
            self.screen.fill(self.bg_color)

#    pygame.display.flip()

instance = Alinegame()
instance.runner()