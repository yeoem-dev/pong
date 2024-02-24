import pygame

class Ball(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
    
    def render(self, screen):
        pygame.draw.ellipse(screen, 'white', self)