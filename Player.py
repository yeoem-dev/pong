import pygame

class Player():
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x,  self.y, 100, 15))

    def right(self):
        if self.x < 400:
            self.x += self.speed 

    def left(self):
        if self.x > 0: 
            self.x -= self.speed 