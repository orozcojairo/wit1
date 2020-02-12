import pygame
import sys

#initiating the library
pygame.init()

#screen dimensions
width = 500
height = 500

#creating the SCREEN
screen = pygame.display.set_mode((width, height))


#initiate the SCREEN
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 0, 0)) ### screen is red
    pygame.display.update()
