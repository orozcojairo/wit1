### ALWAYS IMPORT THESE LIBRARIES
import pygame
import sys

### INITIATING THE PYGAME LIBRARY
pygame.init()

### DIMENSIONS OF YOUR SCREEN
width = 500
height = 500

### CREATING A SCREEN
screen = pygame.display.set_mode((width, height))

### DEFINING THE MAIN COLORS
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#switches
rectangle = False
lines = False
circle = False

#sprite
sprite_w = 20
sprite_h = 20
sprite_x = 50
sprite_y = 50
### RUN THE GAME PROGRAM WIT A WHILE LOOP
while True:

    ### CAPTURE THE KEYS THAT YOU PRESS
    for event in pygame.event.get():
        ### PRESS THE RED X BOTTON ON THE TOP RIGHT AND PROGRAM WILL QUIT
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame. K_w:
                 rectangle = True
            if event.key ==pygame. K_s:
                lines = True
            if event.key == pygame. K_a:
                circle = True
            elif event.key == pygame. K_DOWN:
                 sprite_y = sprite_y + 10
            elif event.key == pygame. K_RIGHT:
                 sprite_x = sprite_x + 10
            elif event.key == pygame. K_UP:
                 sprite_y = sprite_y - 10
            elif event.key == pygame. K_LEFT:
                 sprite_x = sprite_x - 10


    screen.fill(white) ### BACKGROUND IS WHITE

    ### DRAW LINES
    if lines:
        pygame.draw.lines(screen, black, False, [(0, 0), (500, 500)], 3)
        pygame.draw.lines(screen, black, False, [(500, 0), (0,500)], 3)

    if circle:
        pygame.draw.circle(screen, black, (250, 250), 100, 3)

    if rectangle:
        pygame.draw.rect(screen, black, (200, 200, 150, 150), 3)

    #creating sprite
    pygame.draw.rect(screen, red, (sprite_w, sprite_h, sprite_x, sprite_y), 5)

    pygame.display.update() ### NEED THIS SO THAT WE CAN SEE SCREEN
