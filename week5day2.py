import pygame
import sys

#initiate the library with the program
pygame.init()

# DIMENSIONS OF SCREEN
height = 200
width = 200

#CREATING THE SCREEN
screen = pygame.display.set_mode((width, height))
screen2 = pygame.display.set_mode((width, height))
#running the game/program
while True:
#register the buttons that we press
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.lines(screen, (255, 255, 255), False, [(0, 100),(200, 100)], 5)
    pygame.draw.lines(screen, (255, 255, 255), False, [(50, 0), (50, 200)], 5)
    pygame.draw.lines(screen2, (255, 255, 255), False, [(70, 0), (70, 200)], 5)
    pygame.display.update()
