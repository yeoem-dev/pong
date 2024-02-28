import pygame, random

class Ball(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed_x = 5 * random.choice((-1, 1))
        self.speed_y = 5 * random.choice((-1, 1))
        self.score_time = True

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    
    def render(self, screen):
        pygame.draw.ellipse(screen, 'white', self)

    def restart(self, screen_width, screen_height):
        self.center = (screen_width/2 , screen_height/2)
        current_time = pygame.time.get_ticks()


        if current_time - self.score_time < 2100:
            self.speed_x, self.speed_y = 0, 0
        else:
            self.speed_x = 5 * random.choice((1, -1))
            self.speed_y = 5 * random.choice((1, -1))
            self.score_time = None