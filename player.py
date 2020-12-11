import pygame
import os


class Player:
    def __init__(self, x, y):
        self.right, self.left, self.up, self.down = False, False, False, False
        self.anim_right, self.anim_left, self.anim_up, self.anim_down = False, False, False, False
        self.dir = ''
        self.last_dir = ''
        self.moved = False
        self.x_spd, self.y_spd = 0, 0
        self.x = x
        self.y = y
        self.speed = 4
        self.colliding = False
        self.life = 25
        self.max_life = 25
        self.damaged = False
        self.damage_cont = 0
        self.animation_frames = {}
        self.player_action = 'idle_front'
        self.player_frame = 0
        self.player_flip = False
        self.jewel_img = pygame.image.load(os.path.join('data', 'jewel.png'))
        self.damaged_img = pygame.image.load(os.path.join('data', 'player_animation', 'damaged.png'))
        self.animation_database = {'walk_side': self.load_animation('walk_side', [6, 6, 6, 6, 6, 6]),
     'walk_back': self.load_animation('walk_back', [6, 6, 6, 6, 6, 6, 6]), 'walk_front': self.load_animation('walk_front', [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]),
    'idle_front': self.load_animation('idle_front', [6, 6, 6, 6, 6]), 'idle_back': self.load_animation('idle_back', [6, 6, 6, 6, 6]),
    'idle_side': self.load_animation('idle_side', [6, 6, 6, 6, 6])}
        self.rect = pygame.Rect(x, y, 61, 93)

    def hud(self, win):
        back = pygame.Rect(30, 20, self.max_life * 7, 30)
        pygame.draw.rect(win, (255, 0, 0), back)
        front = pygame.Rect(30, 20, self.life * 7, 30)
        pygame.draw.rect(win, (0, 255, 0), front)

    def load_animation(self, path, frame_duration):
        animation_name = path
        animation_frame_data = []
        n = 0
        for frame in frame_duration:
            animation_frame_id = animation_name + '_' + str(n) + '.png'
            animation_image = pygame.image.load(os.path.join('data', 'player_animation', animation_name, animation_frame_id))
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

    def render(self, win, game_level):
        self.dir = self.last_dir
        if self.moved:
            if self.anim_right:
                self.player_action, self.player_frame = self.change_action(self.player_action,
                                                                                     self.player_frame, 'walk_side')
                self.player_flip = False
            elif self.anim_left:
                self.player_action, self.player_frame = self.change_action(self.player_action,
                                                                                     self.player_frame, 'walk_side')
                self.player_flip = True
            elif self.anim_up:
                self.player_action, self.player_frame = self.change_action(self.player_action,
                                                                                     self.player_frame, 'walk_back')
                self.player_flip = False
            elif self.anim_down:
                self.player_action, self.player_frame = self.change_action(self.player_action,
                                                                                     self.player_frame, 'walk_front')
                self.player_flip = False
        else:
            if self.dir == 'idle_right':
                self.player_action, self.player_frame = self.change_action(self.player_action,
                                                                           self.player_frame, 'idle_side')
                self.player_flip = False
            elif self.dir == 'idle_left':
                self.player_action, self.player_frame = self.change_action(self.player_action,
                                                                           self.player_frame, 'idle_side')
                self.player_flip = True
            elif self.dir == 'idle_up':
                self.player_action, self.player_frame = self.change_action(self.player_action,
                                                                           self.player_frame, 'idle_back')
                self.player_flip = False
            elif self.dir == 'idle_down':
                self.player_action, self.player_frame = self.change_action(self.player_action,
                                                                           self.player_frame, 'idle_front')
                self.player_flip = False

        self.player_frame += 1
        if self.player_frame >= len(self.animation_database[self.player_action]):
            self.player_frame = 0
        player_img_id = self.animation_database[self.player_action][self.player_frame]
        player_img = self.animation_frames[player_img_id]
        if game_level == 'level1':
            win.blit(self.jewel_img, (self.rect.x, self.rect.y))
            if self.damaged:
                if self.damage_cont <= 2:
                    win.blit(self.damaged_img, (self.rect.x, self.rect.y))
                    self.damage_cont += 1
                else:
                    self.damaged = False
                    self.damage_cont = 0
        else:
            win.blit(pygame.transform.flip(player_img, self.player_flip, False), (self.rect.x, self.rect.y))
