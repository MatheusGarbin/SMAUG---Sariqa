import pygame
import pygame.freetype
import os


class Dialog:
    def __init__(self, font_size):
        self.player_head = pygame.image.load(os.path.join('data', 'normal.png'))
        self.have_letters = True
        self.text_moving = False
        self.choose = False
        self.mini_game = False
        self.message = False
        self.tutorial = False
        self.page = 0
        self.loop_line = 0
        self.expression = ''
        self.font_y_type = True
        self.font_y = 0
        self.font_size = font_size
        self.used_texts = []
        self.list_2 = []
        self.list_1 = []
        self.text = ''
        self.font1 = pygame.freetype.Font(os.path.join('data', 'pixChicago.ttf'), self.font_size)
        self.font4 = pygame.freetype.Font(os.path.join('data', 'pixChicago.ttf'), self.font_size + 10)
        self.font3 = pygame.freetype.Font(os.path.join('data', 'pixChicago.ttf'), self.font_size - 2)
        self.font2 = pygame.freetype.Font(os.path.join('data', 'Pixeled.ttf'), self.font_size - 2)
        self.rect = pygame.Rect(0, 160, 800, 200)

    def compressao(self):
        file = open(os.path.join('data', 'dialogs.txt'), "r", -1, "utf-8")
        list_file = file.read()
        file.close()
        list_file = list_file.split('\n')
        for row in list_file:
            self.list_1.append(row)

        for phrase in self.list_1:
            list_phrase = []
            for letter in phrase:
                list_phrase.append(ord(letter))
            self.list_2.append(list_phrase)

        file_2 = open("./data/dialogs_compressed.txt", "w")
        file_2.write(str(self.list_2))

    def descompressao(self, number):
        list_3 = []
        new_list_3 = []
        for letter in self.list_2[number]:
            list_3.append(chr(letter))
        list_3 = ''.join(list_3)
        list_3 = list_3.split('/')
        for i in range(0, len(list_3)):
            new_value = list_3[i].split('|')
            new_list_3.append(new_value)
        file_3 = open(os.path.join('data', 'dialogs_descompressed.txt'), "w", -1, "utf-8")
        file_3.write(str(new_list_3))
        return new_list_3

    def dialog_type(self, type, number, used, win, height):
        self.text = self.descompressao(number)
        if self.text not in self.used_texts:
            self.have_letters = True
            self.text_moving = True
            self.rect = pygame.Rect(0, height - 160, 800, 200)
            if type == 1:
                if self.page < len(self.text[0]):
                    pygame.draw.rect(win, (0, 0, 0), self.rect)
                    self.render(15, height - 140, win, self.text[0], height)
                else:
                    self.have_letters = False
                    self.text_moving = False
                    if used == True:
                        self.used_texts.append(self.text)
                    self.message = False
                    self.page = 0

            if type == 2:
                if self.page < len(self.text):
                    pygame.draw.rect(win, (0, 0, 0), self.rect)
                    for i in range(len(self.text[self.page])):
                        self.render_multi(15, height - 140, win, i, self.text, height)
                else:
                    self.have_letters = False
                    self.text_moving = False
                    if used == True:
                        self.used_texts.append(self.text)
                    self.message = False
                    self.page = 0
                    self.line = 0

    def text_y(self):
        if self.font_y_type:
            self.font_y += 0.3
            if self.font_y >= 2:
                self.font_y_type = False
        elif not self.font_y_type:
            self.font_y -= 0.3
            if self.font_y <= -2:
                self.font_y_type = True

    def expression_choice(self, win):
        if self.expression == 'raiva':
            self.player_head = pygame.image.load(os.path.join('data', 'raiva.png'))
            win.blit(self.player_head, (490, 130))
        elif self.expression == 'normal':
            self.player_head = pygame.image.load(os.path.join('data', 'normal.png'))
            win.blit(self.player_head, (490, 150))
        elif self.expression == 'desejo':
            self.player_head = pygame.image.load(os.path.join('data', 'desejo.png'))
            win.blit(self.player_head, (510, 150))
        elif self.expression == 'medo':
            self.player_head = pygame.image.load(os.path.join('data', 'medo.png'))
            win.blit(self.player_head, (490, 150))
        elif self.expression == 'risada':
            self.player_head = pygame.image.load(os.path.join('data', 'risada.png'))
            win.blit(self.player_head, (450, 110))

    def render(self, x, y, win, texts, height):
        if not self.message and not self.tutorial:
            self.expression_choice(win)
        elif not self.tutorial:
            self.font3.render_to(win, (25, height - 40), 'Aperte "ESC" para voltar', (255, 255, 255))
        self.font1.render_to(win, (x, y + self.font_y), texts[self.page], (255, 255, 255))
        self.font3.render_to(win, (600, height - 40), 'Aperte "F"', (255, 255, 255))

    def render_multi(self, x, y, win, line, texts, height):
        if not self.message and not self.tutorial:
            self.expression_choice(win)
        elif not self.tutorial:
            self.font3.render_to(win, (25, height - 40), 'Aperte "ESC" para voltar', (255, 255, 255))
        self.font1.render_to(win, (x, (y + 2 * self.font_size * line) + self.font_y), texts[self.page][line], (255, 255, 255))
        self.font3.render_to(win, (600, height - 40), 'Aperte "F"', (255, 255, 255))
