import pygame 
from Player import *
from Ball import *
import random

#Constantes

pygame.init()
screen_width, screen_height = 800, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('re-pong')

color_player = (255, 255, 255)
light_grey = (180, 180, 180)

player1 =  Player(screen_width/2 - 70, 20, color=color_player, speed=7)
player2 =  Player(screen_width/2 - 70, screen_height-30, color=color_player, speed=7)
ball = Ball(screen_width/2 - 7, screen_height/2 - 7, 15, 15)

ball_speed_x = 7
ball_speed_y = 7

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1.left()
    if keys[pygame.K_RIGHT]:
        player1.right()
    if keys[pygame.K_a]:
        player2.left()
    if keys[pygame.K_d]:
        player2.right()

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1 

    # La balle doit rebondir en contact n'importe quel joueur
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_y *= -1 


    screen.fill('black')

    player1.render(screen)
    player2.render(screen)
    ball.render(screen)
    
    pygame.draw.aaline(screen, light_grey, (0, screen_height/2), (screen_width, screen_height/2))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
