import pygame
import random


class Ghost:
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.direction = 0

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

    def move(self, map):

        if self.direction == 0:
            if map[((self.y - 1) / 30)][(self.x / 30)] > 0:
                if map[((self.y - 1) / 30)][((self.x + 29) / 30)] > 0:
                    self.y -= 1
                else:
                    self.direction = random.randint(0, 3)
            else:
                self.direction = random.randint(0, 3)

        if self.direction == 1:
            if map[((self.y + 30) / 30)][(self.x / 30)] > 0:
                if map[((self.y + 30) / 30)][((self.x + 29) / 30)] > 0:
                    self.y += 1
                else:
                    self.direction = random.randint(0, 3)
            else:
                self.direction = random.randint(0, 3)
        if self.direction == 2:
            if self.x - 1 < 0:
                self.x = 540
            elif map[(self.y / 30)][((self.x - 1) / 30)] > 0:
                if map[((self.y + 29) / 30)][((self.x - 1) / 30)] > 0:
                    self.x -= 1
                else:
                    self.direction = random.randint(0, 3)
            else:
                self.direction = random.randint(0, 3)

        if self.direction == 3:
            if self.x + 1 > 540:
                self.x = 0
            elif map[self.y / 30][((self.x + 30) / 30)] > 0:
                if map[(self.y + 29) / 30][((self.x + 30) / 30)] > 0:
                    self.x += 1
                else:
                    self.direction = random.randint(0, 3)
            else:
                self.direction = random.randint(0, 3)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 128, 128), pygame.Rect(self.x, self.y, 30, 30))

    def overlap(self, py, px):
        if self.x >= (px + 30) or self.y >= (py + 30):
            return False
        if (self.x + 30) <= px or (self.y + 30) <= py:
            return False
        return True
