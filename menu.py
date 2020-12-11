import pygame
import os


class Menu:
    def __init__(self, win):
        self.font = pygame.font.SysFont(None, 60)
        self.click = False
        self.win = win
        self.menu_img = pygame.image.load(os.path.join('data', 'menu.png'))
        self.main_clock = pygame.time.Clock()

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
