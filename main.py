import pygame, sys, random
from elements import bar, ball, collision

pygame.init()

pygame.display.set_caption('Pong')

WIDTH = 1000
HEIGHT = 600
BLACK = 40, 40, 40
WHITE = 220, 220, 220

L_Bar = bar(WIDTH, HEIGHT, 30)
R_Bar = bar(WIDTH, HEIGHT, WIDTH - 30)

ball = ball(WIDTH, HEIGHT)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and not L_Bar['y'] <= 2:
        L_Bar['y'] -= 1
    if keys[pygame.K_s] and not L_Bar['y'] >= HEIGHT - L_Bar['length'] - 2:
        L_Bar['y'] += 1
    if keys[pygame.K_i] and not R_Bar['y'] <= 2:
        R_Bar['y'] -= 1
    if keys[pygame.K_k] and not R_Bar['y'] >= HEIGHT - R_Bar['length'] - 2:
        R_Bar['y'] += 1

    #background
    screen.fill(BLACK)

    #bars
    pygame.draw.rect(screen, WHITE, pygame.Rect(L_Bar['x'], L_Bar['y'], L_Bar['weight'], L_Bar['length']))
    pygame.draw.rect(screen, WHITE, pygame.Rect(R_Bar['x'], R_Bar['y'], R_Bar['weight'], R_Bar['length']))

    #ball
    pygame.draw.circle(screen, WHITE, (ball['x'], ball['y']), ball['radius'])
    ball['x'] += ball['speed'][0]
    ball['y'] += ball['speed'][1]

    #check collision
    if collision(L_Bar['x'], L_Bar['y'], 2*L_Bar['weight'] + ball['radius'], L_Bar['length'], ball['x'], ball['y'], ball['radius']):
        ball['speed'][0] *= -1
    if collision(R_Bar['x'], R_Bar['y'], R_Bar['weight'], R_Bar['length'], ball['x'], ball['y'], ball['radius']):
        ball['speed'][0] *= -1

    pygame.display.flip()
    pygame.display.update()
