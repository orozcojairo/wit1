import pygame
import sys
import random
import time

class snake():
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.change_direction = self.direction


    def change_dir(self, dir):
        if dir == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
        elif dir == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif dir == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif dir == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"

    def move(self, food_pos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10

        self.body.insert(0, list(self.position))
        if self.position == food_pos:
            return True
        else:
            self.body.pop()
            return False

    def check_collision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return True
        elif self.position[1] > 490 or self.position[1] < 0:
            return True
        for bodypart in self.body[1:]:
            if self.position == bodypart:
                return True
        return False

    def get_head_pos(self):
        return self.position

    def get_body(self):
        return self.body


class food():
    def __init__(self):
        self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10] ## *10 to make multiples of snake movements of 10
        self.is_food_onscreen = True

    def spawn_food(self):
        if self.is_food_onscreen == False:
            self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
            self.is_food_onscreen = True
        return self.position

    def set_food_onscreen(self, choice):
        self.is_food_onscreen = choice


screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Wow Snake")
fps = pygame.time.Clock()

score = 0

snake = snake()
food_spawner = food()

def game_over():
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake.change_dir("UP")
            if event.key == pygame.K_s:
                snake.change_dir("DOWN")
            if event.key == pygame.K_a:
                snake.change_dir("LEFT")
            if event.key == pygame.K_d:
                snake.change_dir("RIGHT")

    food_pos = food_spawner.spawn_food()
    if snake.move(food_pos):
        score += 1
        food_spawner.set_food_onscreen(False)

    screen.fill((225, 225, 225))
    for pos in snake.get_body():
        pygame.draw.rect(screen, (0, 255, 0),(pos[0], pos[1], 10, 10), 0)

    pygame.draw.rect(screen, (255, 0, 0), (food_pos[0], food_pos[1], 10, 10), 0)
    if snake.check_collision():
        game_over()

    pygame.display.set_caption("WOW Snake! | Score: {}".format(score))
    pygame.display.update()
    fps.tick(15)
