import pygame
import sys

pygame.init()

# width = 500
# height = 500
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("snake")

class display():

    def __init__(self):
        self.width = 500
        self.height = 480
        self.caption = "my screen"
        self.color = "red"

    def colors(self):
        if self.color =="red":
            return (255, 0, 0)
        elif self.color == "blue":
            return (0, 0, 255)
        elif self.color == "black":
            return (0, 0, 0)
        elif self.color == "burgandy":
            return (151,5,5)

    # def set_color(self):
    #     self.create_display.fill(self.colors())

    def create_display(self):
        pygame.display.set_caption(self.caption)
        return pygame.display.set_mode((self.width, self.height))

mydisplay = display()
mydisplay.width = 20
screen = mydisplay.create_display()
mydisplay.color = "burgandy"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(mydisplay.colors())
    pygame.display.update()
