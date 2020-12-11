import pygame
import random
import os


class Enemy:
    def __init__(self):
        self.x = 400
        self.y = 75
        self.life = 20
        self.cont = 0
        self.max_cont = 45
        self.last_decision = 0
        self.moving = False
        self.cooldown = False
        self.cooldown_cont = 0
        self.damaged = False
        self.damage_cont = 0
        self.decision = 0
        self.animation_frames = {}
        self.enemy_action = 'idle'
        self.enemy_frame = 0
        self.animation_database = {'idle': self.load_animation('idle', [7, 7, 7, 7, 7, 7])}
        self.damaged_img = pygame.image.load(os.path.join('data', 'enemy_animation', 'damaged.png'))
        self.rect = pygame.Rect(self.x, self.y, 94, 139)

    def movement(self):
        if self.cont < self.max_cont:
            self.cont += 1
        if self.cont == self.max_cont:
            self.moving = True
        if self.moving:
            self.decision = random.randint(0, 4)
            while self.decision == self.last_decision:
                self.decision = random.randint(0, 4)
            if self.decision == 0:
                self.rect.x, self.rect.y = 600, 100
            if self.decision == 1:
                self.rect.x, self.rect.y = 125, 150
            if self.decision == 2:
                self.rect.x, self.rect.y = 710, 300
            if self.decision == 3:
                self.rect.x, self.rect.y = 350, 150
            if self.decision == 4:
                self.rect.x, self.rect.y = 25, 420
            self.last_decision = self.decision
            self.moving = False
            self.cont = 0

        if self.cooldown:
            if self.cooldown_cont <= 3:
                self.cooldown_cont += 1
            else:
                self.cooldown_cont = 0
                self.cooldown = False

    def load_animation(self, path, frame_duration):
        animation_name = path
        animation_frame_data = []
        n = 0
        for frame in frame_duration:
            animation_frame_id = animation_name + '_' + str(n) + '.png'
            animation_image = pygame.image.load(
                os.path.join('data', 'enemy_animation', animation_name, animation_frame_id))
            self.animation_frames[animation_frame_id] = animation_image.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def change_action(self, action_var, frame, new_value):
        if action_var != new_value:
            action_var = new_value
            frame = 0
        return action_var, frame

    def render(self, win):

        self.enemy_action, self.enemy_frame = self.change_action(self.enemy_action, self.enemy_frame, 'idle')

        self.enemy_frame += 1
        if self.enemy_frame >= len(self.animation_database[self.enemy_action]):
            self.enemy_frame = 0
        enemy_img_id = self.animation_database[self.enemy_action][self.enemy_frame]
        enemy_img = self.animation_frames[enemy_img_id]
        win.blit(enemy_img, (self.rect.x, self.rect.y))
        if self.damaged:
            if self.damage_cont <= 1:
                win.blit(self.damaged_img, (self.rect.x, self.rect.y))
                self.damage_cont += 1
            else:
                self.damaged = False
                self.damage_cont = 0
