import pygame
import sys

#   Simple pygame initialization
pygame.init()

color = (255, 255, 255)
screen_size = (900, 800)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("First pygame program")

#   Initializing variables
x = 900 / 2
y = 800 / 2
max_y = 20
vel_x = 1
vel_y = 10
jumping = False
rad = 20

running = True
while running:

    screen.fill(color)
    cords = (x, y)
    pygame.draw.circle(screen, (0, 0, 0), cords, rad)

    for event in pygame.event.get():  # how to quit
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    u_input = pygame.key.get_pressed()  # User input
    if u_input[pygame.K_d] and x < 900:
        x += vel_x
    if u_input[pygame.K_a] and x > 0:
        x -= vel_x

    if u_input[pygame.K_SPACE] and jumping == False:  # Code that makes em jump
        jumping = True
    if jumping:
        y -= vel_y
        vel_y -= 1
    if vel_y == -11:
        vel_y = 10
        jumping = False

    pygame.display.update()
