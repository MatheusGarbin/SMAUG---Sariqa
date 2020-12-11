import pygame
import random
import os


class Stealing:
    def __init__(self):
        self.background_img = pygame.image.load(os.path.join('data', 'lockBackground.png'))
        self.lock_img = pygame.image.load(os.path.join('data', 'lock.png'))
        self.key_img = pygame.image.load(os.path.join('data', 'key.png'))
        self.pontuation_background_img = pygame.image.load(os.path.join('data', 'pontuationBackground.png'))
        self.key_part_img = pygame.image.load(os.path.join('data', 'keyPart.png'))
        self.key_body_img = pygame.image.load(os.path.join('data', 'keyBody.png'))
        self.lock_pontuation_img = pygame.image.load(os.path.join('data', 'lockPontuation.png'))
        self.y = 230
        self.y2 = 200
        self.up, self.down = False, False
        self.speed = 6
        self.lock_speed = 5
        self.rand_spd = 20
        self.rand_cont = 0
        self.sound_cont = 45
        self.pontuation_cont = 0
        self.is_down = True
        self.pont = 100
        self.theft = False
        self.failed = 0
        self.exit = False
        self.money = 0
        self.bad_endind = 0
        self.stealing_artifacts = []
        self.lock_sound = pygame.mixer.Sound(os.path.join('data', 'UnlockDoor.ogg'))
        self.lock_sound.set_volume(0.7)
        self.lock1_sound = pygame.mixer.Sound(os.path.join('data', 'Key Jiggle.wav'))
        self.lock1_sound.set_volume(0.7)

    def steal(self, win, artifact):
        y_spd = 0

        if self.up:
            y_spd -= self.speed
        if self.down:
            y_spd += self.speed

        self.y += y_spd

        back_in = pygame.Rect(210, 70, 35, 340)
        win.blit(self.background_img, (200, 50))
        lock = pygame.Rect(210, self.y2, 35, 59)
        mouse = pygame.Rect(210, self.y, 35, 30)
        win.blit(self.lock_img, (210, self.y2 - 6))
        win.blit(self.key_img, (210, self.y))

        win.blit(self.pontuation_background_img, (260, 95))
        win.blit(self.key_body_img, (282, 135))
        win.blit(self.key_part_img, (282, 125 + self.pont + 10))
        self.key_body_img = pygame.transform.scale(self.key_body_img, (9, self.pont + 10))
        win.blit(self.lock_pontuation_img, (273, 390))

        self.lock_move(lock, back_in)

        if mouse.top <= back_in.top:
            self.y = back_in.top + 5
        elif mouse.bottom >= back_in.bottom:
            self.y = back_in.bottom - mouse.height - 5

        self.pontuation(mouse, lock, artifact)

    def hud(self, dialog, win):
        if self.theft:
            if self.pontuation_cont <= 150:
                self.pontuation_cont += 1
                back = pygame.Rect(500, 20, 250, 80)
                pygame.draw.rect(win, (0, 0, 0), back)
                dialog.font1.render_to(win, (550, 50), f'Dinheiro: {self.money}', (255, 255, 255))
            else:
                self.theft = False
                self.pontuation_cont = 0

    def lock_move(self, lock, back_in):
        if self.is_down:
            self.y2 += self.lock_speed
        if not self.is_down:
            self.y2 -= self.lock_speed

        if self.rand_cont <= self.rand_spd:
            self.rand_cont += 1
        elif self.rand_cont >= self.rand_spd:
            randomizer = random.randint(1, 2)
            if randomizer == 1:
                self.is_down = True
            elif randomizer == 2:
                self.is_down = False
            self.rand_cont = 0

        if lock.bottom >= back_in.bottom - 5:
            self.is_down = False
        if lock.top <= back_in.top:
            self.is_down = True

    def pontuation(self, rect_player, rect_lock, artifact):
        if rect_player.colliderect(rect_lock):
            if self.sound_cont <= 45:
                self.sound_cont += 1
            elif self.sound_cont >= 45:
                self.lock1_sound.play()
                self.sound_cont = 0
            self.pont += 1
        else:
            self.lock1_sound.stop()
            self.pont -= 1

        if self.pont >= 250:
            self.lock_sound.play()
            self.lock1_sound.stop()
            self.theft = True
            self.exit = True
            self.stealing_artifacts.append(artifact)
            self.money += 500
            self.bad_endind += 1
            self.pont = 100
            self.y = 200
            self.up, self.down = False, False
        elif self.pont <= 0:
            self.theft = False
            self.failed += 1
            self.exit = True
            self.pont = 100
            self.y = 200
            self.up, self.down = False, False

        if self.bad_endind < 2:
            self.lock_speed = self.bad_endind + 1
