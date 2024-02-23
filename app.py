import pygame 
from Player import *

pygame.init()
screen = pygame.display.set_mode((500, 580))
pygame.display.set_caption('re-pong')

player1 =  Player(200, 125, color=(255, 255, 255), speed=0.1)
player2 =  Player(200, 525, color=(255, 255, 255), speed=0.1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_RIGHT]:
        player2.right()
    
    if key_pressed[pygame.K_LEFT]:
        player2.left()

    if key_pressed[pygame.K_a]:
        player1.left()

    if key_pressed[pygame.K_d]:
        player1.right()

    screen.fill('black')

    player1.render(screen)
    player2.render(screen)

    pygame.display.flip()

pygame.quit()
