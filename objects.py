import pygame


class Objects:
    def __init__(self, x, y, width, height, img):
        self.x = x
        self.y = y
        self.img = img
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.collision_rect = pygame.Rect(self.x, self. y, self.width, self.height)

    def render(self, win):
        win.blit(self.img, (self.rect.x, self.rect.y))
