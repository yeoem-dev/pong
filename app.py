import pygame, sys, random
from Player import *
from Ball import *

#Constantes
opponent_speed = 5


pygame.init()
screen_width, screen_height = 800, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('re-pong')

color_player = (255, 255, 255)
light_grey = (180, 180, 180)

opponent = Player(screen_width/2 - 70, 20, color=color_player, speed=7)
player = Player(screen_width/2 - 70, screen_height-30, color=color_player, speed=7)
ball = Ball(screen_width/2 - 7, screen_height/2 - 7, 15, 15)


clock = pygame.time.Clock()

score_time = True
game_font = pygame.font.Font('freesansbold.ttf', 23)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.move()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    if keys[pygame.K_a]:
        opponent.move_left()
    if keys[pygame.K_d]:
        opponent.move_right()

    if ball.score_time:
        ball.restart(screen_width, screen_height)
    
    if ball.bottom >= screen_height:
        opponent.score += 1
        ball.score_time = pygame.time.get_ticks()
        ball.restart(screen_width, screen_height)

    if ball.top <= 0 :
        player.score += 1
        ball.score_time = pygame.time.get_ticks()
        ball.restart(screen_width, screen_height)

    if ball.left <= 0 or ball.right >= screen_width:
        ball.speed_x *= -1 

    # La balle doit rebondir en contact n'importe quel joueur
    if ball.colliderect(opponent) or ball.colliderect(player):
        ball.speed_y *= -1


    screen.fill('black')

    opponent.render(screen)
    player.render(screen)
    ball.render(screen)
    pygame.draw.aaline(screen, light_grey, (0, screen_height/2), (screen_width, screen_height/2))
    
    player_text = game_font.render(f'{player.score}', True, light_grey)
    opponent_text = game_font.render(f'{opponent.score}', True, light_grey)
    screen.blit(player_text, (screen_width / 2, screen_height/2 + 20))
    screen.blit(opponent_text, (screen_width / 2, screen_height/2 - 40))

    pygame.display.flip()
    clock.tick(60)

