import pygame

class Player(pygame.Rect):
    def __init__(self, x, y, color, speed):
        super().__init__(x, y, 140, 10)
        self.speed = speed
        self.color = color
        self.score = 0

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self)

    def move_right(self):
        if self.x < 660:
            self.x += self.speed 

    def move_left(self):
        if self.x > 0: 
            self.x -= self.speed 