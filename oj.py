import pygame
import sys

#initiate program
pygame.init()
#color
white = (225, 225, 225)
#define our window
width = 500
height = 420
#screen
screen = pygame.display.set_mode((width, height))
#sprite cordinates
pos_x = 500
pos_y = 420

#start pygame
while True:
    circle = False

    #code the shutdown button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                circle = True
            elif event.key == pygame.K_w:
                pos_y = pos_y - 10
            elif event.key == pygame.K_a:
                pos_x = pos_x - 10
            elif event.key == pygame.K_s:
                pos_y = pos_y + 10
            elif event.key == pygame.K_d:
                pos_x = pos_x +10


    #draw a rectangle sprite
    pygame.draw.rect(screen, white, (250, 210, 10, 10), 5)

    #rectangle sprite
    pygame.draw.rect(screen, white, (pos_x, pos_y, 10, 10),5)

    pygame.display.update()
