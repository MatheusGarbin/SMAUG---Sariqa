import pygame
import random
import math
import os


class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.dx = math.cos(math.radians(self.angle))
        self.dy = math.sin(math.radians(self.angle))
        self.vel_x = 4
        self.vel_y = 4
        self.del_cont = 0
        self.horus_cont = 0
        self.horus_hability = False
        self.cooldown_counter = 0
        self.cooldown = 40
        self.projectiles = []
        self.right, self.left, self.up, self.bottom = False, False, False, False
        self.projectile_img = pygame.image.load(os.path.join('data', 'projectile.png'))
        self.rect = pygame.Rect(self.x, self.y, 50, 40)

    def render(self, win):
        win.blit(self.projectile_img, (self.rect.x, self.rect.y))

    def shoot_delay(self):
        if self.cooldown_counter >= self.cooldown:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

    def horus_position(self):

        decision = random.randint(0, 3)
        if decision == 0:
            self.rect.x, self.rect.y = 50, 100
            self.angle = random.randint(300, 330)
        elif decision == 1:
            self.rect.x, self.rect.y = 750, 650
            self.angle = random.randint(120, 150)
        elif decision == 2:
            self.rect.x, self.rect.y = 50, 650
            self.angle = random.randint(210, 240)
        elif decision == 3:
            self.rect.x, self.rect.y = 750, 100
            self.angle = random.randint(30, 60)

    def horus(self, height, width, list):
        self.dx = math.cos(math.radians(self.angle))
        self.dy = math.sin(math.radians(self.angle))
        self.rect.x += (self.dx * self.vel_x)
        self.rect.y += (self.dy * self.vel_y)
        if self.rect.top <= 100:
            self.rect.y += 1
            self.angle = random.randint(-70, 70)
            self.dy *= -1
        if self.rect.bottom >= height:
            self.rect.y -= 1
            self.angle = random.randint(110, 250)
            self.dy *= -1
        if self.rect.left <= 80:
            self.angle = random.randint(-70, 70)
            self.dx *= -1
        if self.rect.right >= width:
            self.angle = random.randint(110, 250)
            self.dx *= -1

        if len(list) > 8:
            list.pop(0)
