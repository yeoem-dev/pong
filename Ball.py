import pygame, random

class Ball(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed_x = 5 * random.choice((-1, 1))
        self.speed_y = 5 * random.choice((-1, 1))

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    
    def render(self, screen):
        pygame.draw.ellipse(screen, 'white', self)

    def restart(self, screen_width, screen_height):
        self.center = (screen_width/2 - 7, screen_height/2 - 7)
        self.speed_x *= random.choice((1, -1))
        self.speed_y *= random.choice((1, -1))