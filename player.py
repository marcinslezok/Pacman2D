import pygame


class Player:
    def __init__(self):
        self.y = 480
        self.x = 270

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

    def moveUp(self, map):
        if map[((self.y - 1) / 30)][(self.x / 30)] > 0:
            if map[((self.y - 1) / 30)][((self.x + 29) / 30)] > 0:
                self.y -= 1

    def moveDown(self, map):
        if map[((self.y + 30) / 30)][(self.x / 30)] > 0:
            if map[((self.y + 30) / 30)][((self.x + 29) / 30)] > 0:
                self.y += 1

    def moveLeft(self, map):
        if self.x - 1 < 0:
            self.x = 540
        elif map[(self.y / 30)][((self.x - 1) / 30)] > 0:
            if map[((self.y + 29) / 30)][((self.x - 1) / 30)] > 0:
                self.x -= 1

    def moveRigth(self, map):
        if self.x + 1 > 540:
            self.x = 0
        elif map[self.y / 30][((self.x + 30) / 30)] > 0:
            if map[(self.y + 29) / 30][((self.x + 30) / 30)] > 0:
                self.x += 1

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(self.x, self.y, 30, 30))
