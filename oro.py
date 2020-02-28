import pygame
import sys

### INITIATING THE PYGAME LIBRARY
pygame.init()

### DIMENSIONS OF YOUR SCREEN
width = 500
height = 500
posx = 250
posy = 350
### CREATING A SCREEN
screen = pygame.display.set_mode((width, height))
screenName = pygame.display.set_caption("Joe mAMA <3")
### DEFINING THE MAIN COLORS
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
yellow = (0, 255, 255)

moveup = False
movedown = False
moveleft = False
moveright = False
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveup = True
                movedown = moveright = moveleft = False
            if event.key == pygame.K_s:
                movedown = True
                moveup = moveleft = moveright = False
            if event.key == pygame.K_a:
                moveright = True
                moveup = movedown = moveleft = False
            if event.key == pygame.K_d:
                moveleft = True
                movedown = moveup = moveright = False


    if moveup and posy > 0:
        posy -= 10
    if movedown and posy < 490:
        posy += 10
    if moveright and posx > 0:
        posx -= 10
    if moveleft and posx < 490:
        posx += 10



    screen.fill(red)
    pygame.draw.rect(screen, white, (posx, posy, 10, 10), 3)
    myfont = pygame.font.Font(None, 30)
    textsurface = myfont.render('{},{}'.format(posx, posy), True,  green)
    screen.blit(textsurface, (220, 0))
    textsurface = myfont.render("jairo is a beast", True, green)
    screen.blit(textsurface, (250, 240))
    pygame.display.update()
