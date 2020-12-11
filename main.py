import os
import pygame
import pygame.freetype
from projectile import Projectile
from stealing import Stealing
from player import Player
from enemy import Enemy
from objects import Objects
from dialog import Dialog
from menu import Menu
from connection import Connection

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(64)

music_1 = pygame.mixer.Sound(os.path.join('data', 'another egyptian theme.ogg'))
music_1.set_volume(0.3)
music_2 = pygame.mixer.Sound(os.path.join('data', 'telaSelecao.wav'))
music_2.set_volume(0.7)
music_3 = pygame.mixer.Sound(os.path.join('data', 'Egito2.ogg'))
music_3.set_volume(0.7)
gameover_music = pygame.mixer.Sound(os.path.join('data', 'explode.ogg'))
gameover_music.set_volume(0.7)
projectile_sound = pygame.mixer.Sound(os.path.join('data', 'enchant2.wav'))
projectile_sound.set_volume(0.3)
walk_sound = pygame.mixer.Sound(os.path.join('data', 'Passos.ogg'))
walk_sound.set_volume(0.5)
door_sound = pygame.mixer.Sound(os.path.join('data', 'DoorOpen.ogg'))
door_sound.set_volume(0.7)
player_damage_sound = pygame.mixer.Sound(os.path.join('data', 'Artifact Damaging.wav'))
player_damage_sound.set_volume(0.5)
horus_damage_sound = pygame.mixer.Sound(os.path.join('data', 'HorusDamage.ogg'))
horus_damage_sound.set_volume(0.7)
Horus_sound = pygame.mixer.Sound(os.path.join('data', 'HorusSkill.ogg'))
Horus_sound.set_volume(0.07)

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Sariqa')

end_message_img = pygame.image.load(os.path.join('data', 'endMessage.jpg'))

wall1_img = pygame.image.load(os.path.join('data', 'wall1.png'))
floor_img = pygame.image.load(os.path.join('data', 'floor.png'))
wallTopHor_img = pygame.image.load(os.path.join('data', 'wallTopHor.png'))
wallTopVert_img = pygame.image.load(os.path.join('data', 'wallTopVert.png'))
wallTopSide_img = pygame.image.load(os.path.join('data', 'wallTopSide.png'))
side_img = pygame.image.load(os.path.join('data', 'side.png'))

pilar_img = pygame.image.load(os.path.join('data', 'pilar.png'))
gate_img = pygame.image.load(os.path.join('data', 'gate.png'))
gate_side_img = pygame.image.load(os.path.join('data', 'gate2.png'))
gate_down_img = pygame.image.load(os.path.join('data', 'gate1.png'))
gate_down_img = pygame.transform.rotate(gate_down_img, 90)

armasAfricanas_img = pygame.image.load(os.path.join('data', 'armasAfricanas.png'))
elmoRomano_img = pygame.image.load(os.path.join('data', 'elmoRomano.png'))
estatuaAfricana_img = pygame.image.load(os.path.join('data', 'estatuaAfricano.png'))
mascaraAfricana_img = pygame.image.load(os.path.join('data', 'mascaraAfricana.png'))
vasoChines_img = pygame.image.load(os.path.join('data', 'vasoChines.png'))
farao_img = pygame.image.load(os.path.join('data', 'farao.png'))
poteEgipcio_img = pygame.image.load(os.path.join('data', 'poteEgipcio.png'))
obra1_img = pygame.image.load(os.path.join('data', 'obra1.png'))
obra2_img = pygame.image.load(os.path.join('data', 'obra2.png'))
obra3_img = pygame.image.load(os.path.join('data', 'obra3.png'))

steal_artifacts_1_img = pygame.image.load(os.path.join('data', 'steal_artifact_1.png'))
steal_artifacts_2_img = pygame.image.load(os.path.join('data', 'steal_artifact_2.png'))
steal_artifacts_3_img = pygame.image.load(os.path.join('data', 'steal_artifact_3.png'))
steal_artifacts_4_img = pygame.image.load(os.path.join('data', 'steal_artifact_4.png'))

dialog = Dialog(15)

dialog.compressao()

cutscene = [('Nefertari White é filha de um pai descendente inglês',
             'e de uma mãe de origem egípcia; os seus pais, arqueólogos,',
             'estavam a muito tempo sem conseguir achar alguma',
             'descoberta interessante, passando muita fome nesse',
             'meio tempo. Então, eles se juntaram com um famoso',
             'arqueólogo inglês que lá estava na colonia. Quando',
             'conseguiram achar uma tumba com 4 artefatos muito',
             'raros e impressionantes.',
             'Nisso, acharam que iriam ficar muito bem de vida.',
             'Porem, o arqueólogo alemão acabou ficando com inveja do',
             'valor místico dos artefatos e matou os pais de Nefertari,',
             'deixando-a órfã. Sem nenhum outro parente próximo, Nefertari',
             'foi criada nas ruas, aprendendo a roubar desde cedo. Com a ',
             'grande motivação de vingar os seus pais e arruinar a carreira',
             'do arqueólogo Herr Verhaten, jurou que um dia conseguiria os',
             'artefatos de volta, e treinou a vida inteira para isso.',)]

credit = [('Julio Cesar Alves de Souza – Level Design e Sonoplasta',
            'Matheus Rodrigues Garbin – Programador e Artista',
            'Lucas Cândido Votto – Roteirista e Level Design',
            'Pedro Jorge Veloso Ferreira Achetta – Roteirista e Programador',
            '',
            'Agradecimentos especiais:',
            'Giovanna Catulo Fonseca – Artista',
            'Victor Hugo Pereira Cardoso – Artista e Sonoplasta',
            '',
            'Músicas e efeitos sonoros:',
            'Victor Hugo – Sem títulos',
            'Cinematic Eagle Cry Sound Effect - eagle sounds - SoundEffectsFactory',
            'https://www.youtube.com/watch?v=WSGFatM1ktU&feature=youtu.be',
            'Foram feitas modificações neste trabalho para o uso neste projeto'),
            ('Todos os outros efeitos sonoros foram tirados do site:',
             'OpenGameArt.org',
             '',
             'Bottle Break - spookymodem',
             'https://creativecommons.org/licenses/by/3.0/   legalcode',
             'https://opengameart.org/content/breaking-bottle',
             '',
             '9 explosion sounds',
             'https://creativecommons.org/licenses/by-sa/3.0/legalcode',
             'https://opengameart.org/content/9-explosion-sounds',
             '',
             'Step sound (walking) - IgnasD',
             'https://creativecommons.org/licenses/by-sa/3.0/legalcode',
             'https://opengameart.org/content/step-sound-walking'),
            ('Spell Sounds Starter Pack - p0ss',
             'https://creativecommons.org/licenses/by-sa/3.0/legalcode',
             'http://www.gnu.org/licenses/gpl-3.0.html',
             'http://www.gnu.org/licenses/old-licenses/gpl-2.0.html',
             'https://opengameart.org/content/spell-sounds-starter-pack',
             'Foram feitas modificações neste trabalho para o uso neste projeto',
             '',
             'Another Egyptian Theme - Spring',
             'https://creativecommons.org/licenses/by/4.0/legalcode',
             'https://creativecommons.org/licenses/by/3.0/legalcode',
             'https://creativecommons.org/licenses/by-sa/4.0/legalcode',
             'https://creativecommons.org/licenses/by-sa/3.0/legalcode',
             'https://static.opengameart.org/OGA-BY-3.0.txt',
             'https://opengameart.org/content/another-egyptian-theme')]

pilar = Objects(4000, 1450, pilar_img.get_width(), pilar_img.get_height(), pilar_img)
gate = Objects(3263, 1300, gate_img.get_width(), gate_img.get_height(), gate_img)
gate_down = Objects(3648, 2500, gate_down_img.get_width(), gate_down_img.get_height(), gate_down_img)
gate_side = Objects(2750, 1728, gate_side_img.get_width(), gate_side_img.get_height(), gate_side_img)

armasAfricanas = Objects(4200, 1720, armasAfricanas_img.get_width(), armasAfricanas_img.get_height(), armasAfricanas_img)
mascaraAfricana = Objects(4250, 2100, mascaraAfricana_img.get_width(), mascaraAfricana_img.get_height(), mascaraAfricana_img)
elmoRomano = Objects(3800, 1770, elmoRomano_img.get_width(), elmoRomano_img.get_height(), elmoRomano_img)
estatuaAfricana = Objects(3800, 2100, estatuaAfricana_img.get_width(), estatuaAfricana_img.get_height(), estatuaAfricana_img)
vasoChines = Objects(3300, 2100, vasoChines_img.get_width(), vasoChines_img.get_height(), vasoChines_img)
farao = Objects(4450, 800, farao_img.get_width(), farao_img.get_height(), farao_img)
poteEgipcio = Objects(3300, 1760, poteEgipcio_img.get_width(), poteEgipcio_img.get_height(), poteEgipcio_img)
obra1 = Objects(3900, 1565, obra1_img.get_width(), obra1_img.get_height(), obra1_img)
obra2 = Objects(3500, 1565, obra2_img.get_width(), obra2_img.get_height(), obra2_img)
obra3 = Objects(4670, 1565, obra3_img.get_width(), obra3_img.get_height(), obra3_img)


object_list = [farao, armasAfricanas, elmoRomano, estatuaAfricana, mascaraAfricana, vasoChines, poteEgipcio, obra1, obra2, obra3]

projectile = Projectile(- 50, 0)

player = Player(4450, 2000)
player2 = Player(100, 1000)

enemy = Enemy()

menu = Menu(screen)

stealing = Stealing()


def load_map(path):
    f = open(os.path.join('data', path + '.txt'))
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map


game_map1 = load_map('level1')
game_map2 = load_map('level2')


def collision(tile_list, vector):
    collision_tolerance = 10
    for tile in tile_list:
        if player.rect.colliderect(tile):
            if vector == 'up':
                return abs(tile.bottom - player.rect.top) < collision_tolerance
            elif vector == 'down':
                return abs(tile.top - player.rect.bottom) < collision_tolerance
            elif vector == 'right':
                return abs(tile.left - player.rect.right) < collision_tolerance
            elif vector == 'left':
                return abs(tile.right - player.rect.left) < collision_tolerance


def move():
    player.x_spd, player.y_spd = 0, 0

    if player.right:
        player.x_spd += player.speed
    if player.left:
        player.x_spd -= player.speed
    if player.up:
        player.y_spd -= player.speed
    if player.down:
        player.y_spd += player.speed

    if player.x_spd != 0 and player.y_spd != 0:
        player.x_spd /= 1.414
        player.y_spd /= 1.414

    player.x += player.x_spd
    player.y += player.y_spd

    if collision(tile_rects, 'right'):
        player.x -= 4
    elif collision(tile_rects, 'left'):
        player.x += 4
    elif collision(tile_rects, 'up'):
        player.y += 4
    elif collision(tile_rects, 'down'):
        player.y -= 4


camera = [0, 0]
camera_on = True


def camera_function():
    if camera_on:
        camera[0] += (int(player.x) - camera[0] - WIDTH / 2) / 5
        camera[1] += (int(player.y) - camera[1] - HEIGHT / 2) / 5
        camera[0] = int(camera[0])
        camera[1] = int(camera[1])


def create_map(game_map):
    global tile_rects

    tile_rects = []

    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '2':
                screen.blit(wall1_img, (x * 192 - camera[0], y * 192 - camera[1]))
                wall1_rect = pygame.Rect(x * 192 - camera[0], (y * 192) - camera[1], 192, 132)
                tile_rects.append(wall1_rect)
            if tile == '0':
                screen.blit(floor_img, (x * 192 - camera[0], y * 192 - camera[1]))
            if tile == '3':
                screen.blit(wallTopHor_img, (x * 192 - camera[0], y * 192 - camera[1]))
            if tile == '4':
                screen.blit(pygame.transform.flip(wallTopHor_img, False, True), (x * 192 - camera[0], y * 192 - camera[1]))
                wallTop1_rect = pygame.Rect(x * 192 - camera[0], (y * 192) - camera[1], 192, 40)
                tile_rects.append(wallTop1_rect)
            if tile == '5':
                screen.blit(wallTopVert_img, (x * 192 - camera[0], y * 192 - camera[1]))
                wallTop2_rect = pygame.Rect((x * 192 - 5) - camera[0], (y * 192) - camera[1], 95, 192)
                tile_rects.append(wallTop2_rect)
            if tile == '6':
                screen.blit(pygame.transform.flip(wallTopVert_img, True, False), (x * 192 - camera[0], y * 192 - camera[1]))
                wallTop2_rect = pygame.Rect((x * 192 + 152) - camera[0], (y * 192) - camera[1], 45, 192)
                tile_rects.append(wallTop2_rect)
            if tile == '7':
                screen.blit(wallTopSide_img, (x * 192 - camera[0], y * 192 - camera[1]))
                wallTopSide_rect = pygame.Rect(x * 192 - camera[0], (y * 192) - camera[1], 192, 192)
                tile_rects.append(wallTopSide_rect)
            if tile == '8':
                screen.blit(pygame.transform.flip(wallTopSide_img, True, False), (x * 192 - camera[0], y * 192 - camera[1]))
                wallTopSide_rect = pygame.Rect(x * 192 - camera[0], (y * 192) - camera[1], 192, 192)
                tile_rects.append(wallTopSide_rect)
            if tile == '9':
                screen.blit(pygame.transform.flip(wallTopSide_img, False, True), (x * 192 - camera[0], y * 192 - camera[1]))
                wallTopSide_rect = pygame.Rect(x * 192 - camera[0], (y * 192) - camera[1], 192, 192)
                tile_rects.append(wallTopSide_rect)
            if tile == 'A':
                screen.blit(pygame.transform.flip(wallTopSide_img, True, True), (x * 192 - camera[0], y * 192 - camera[1]))
                wallTopSide_rect = pygame.Rect(x * 192 - camera[0], (y * 192) - camera[1], 192, 192)
                tile_rects.append(wallTopSide_rect)
            if tile == 'B':
                screen.blit(side_img, (x * 192 - camera[0], y * 192 - camera[1]))
            if tile == 'C':
                screen.blit(pygame.transform.flip(side_img, False, True), (x * 192 - camera[0], y * 192 - camera[1]))
            if tile == 'D':
                screen.blit(pygame.transform.flip(side_img, True, False), (x * 192 - camera[0], y * 192 - camera[1]))
            if tile == 'E':
                screen.blit(pygame.transform.flip(side_img, True, True), (x * 192 - camera[0], y * 192 - camera[1]))
            x += 1
        y += 1


fade_on = False
fade_num = 0


def fade_options(width, height, type):
    global fade_num, fade_on

    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    if fade_on:
        if type == 1:
            if fade_num <= 255:
                fade_num += 2
                fade.set_alpha(fade_num)
                if fade_num >= 255:
                    fade_num = 350
                    fade_on = False
        if type == 2:
            if fade_num >= 0:
                fade_num -= 5
                fade.set_alpha(fade_num)
                if fade_num <= 0:
                    fade_num = 0
                    fade_on = False
        return screen.blit(fade, (0, 0))


def objects_render(list):
    for objects in list:
        objects.rect = pygame.Rect((objects.x - 5) - camera[0], objects.y - camera[1], objects.width + 10, objects.height)

        armasAfricanas.collision_rect = pygame.Rect(armasAfricanas.x - camera[0], armasAfricanas.y - camera[1] + 110, armasAfricanas.width,
                                                 armasAfricanas.height - 200)
        tile_rects.append(armasAfricanas.collision_rect)
        elmoRomano.collision_rect = pygame.Rect(elmoRomano.x - camera[0], elmoRomano.y - camera[1] + 60, elmoRomano.width,
                                                    elmoRomano.height - 140)
        tile_rects.append(elmoRomano.collision_rect)
        mascaraAfricana.collision_rect = pygame.Rect(mascaraAfricana.x - camera[0], mascaraAfricana.y - camera[1] + 60,
                                                     mascaraAfricana.width, mascaraAfricana.height - 140)
        tile_rects.append(mascaraAfricana.collision_rect)
        estatuaAfricana.collision_rect = pygame.Rect(estatuaAfricana.x - camera[0], estatuaAfricana.y - camera[1] + 55,
                                                     estatuaAfricana.width, estatuaAfricana.height - 125)
        tile_rects.append(estatuaAfricana.collision_rect)
        vasoChines.collision_rect = pygame.Rect(vasoChines.x - camera[0], vasoChines.y - camera[1] + 50,vasoChines.width,
                                                vasoChines.height - 130)
        tile_rects.append(vasoChines.collision_rect)
        poteEgipcio.collision_rect = pygame.Rect(poteEgipcio.x - camera[0], poteEgipcio.y - camera[1] + 60,
                                                     poteEgipcio.width, poteEgipcio.height - 140)
        tile_rects.append(poteEgipcio.collision_rect)
        obra1.collision_rect = pygame.Rect(obra1.x - camera[0], obra1.y - camera[1] + 60, obra1.width, obra1.height - 140)
        tile_rects.append(obra1.collision_rect)
        obra2.collision_rect = pygame.Rect(obra2.x - camera[0], obra2.y - camera[1] + 60, obra2.width, obra2.height - 140)
        tile_rects.append(obra2.collision_rect)
        obra3.collision_rect = pygame.Rect(obra3.x - camera[0], obra3.y - camera[1] + 60, obra3.width, obra3.height - 140)
        tile_rects.append(obra3.collision_rect)
        farao.collision_rect = pygame.Rect(farao.x - camera[0], farao.y - camera[1] + 60, farao.width,
                                           farao.height - 140)
        tile_rects.append(farao.collision_rect)

        if objects in stealing.stealing_artifacts:
            if objects == armasAfricanas:
                objects.img = steal_artifacts_1_img
            elif objects == obra1 or objects == obra2 or objects == obra3:
                objects.img = steal_artifacts_3_img
            elif objects == vasoChines or objects == farao:
                objects.img = steal_artifacts_2_img
            else:
                objects.img = steal_artifacts_4_img
        else:
            if objects == armasAfricanas:
                objects.img = armasAfricanas_img
            elif objects == obra1:
                objects.img = obra1_img
            elif objects == obra2:
                objects.img = obra2_img
            elif objects == obra3:
                objects.img = obra3_img
            elif objects == vasoChines:
                objects.img = vasoChines_img
            elif objects == poteEgipcio:
                objects.img = poteEgipcio_img
            elif objects == elmoRomano:
                objects.img = elmoRomano_img
            elif objects == mascaraAfricana:
                objects.img = mascaraAfricana_img
            elif objects == estatuaAfricana:
                objects.img = estatuaAfricana_img
            elif objects == farao:
                objects.img = farao_img

        objects.render(screen)


font_size = 1
press_on = False
num = 0
invert_depth = False


def objects_interaction(font):
    global num, font_size, press_on, invert_depth, level_swap

    if player.rect.colliderect(object_list[num].rect):
        press_on = True
        if player.rect.y <= object_list[num].collision_rect.y - 70:
            invert_depth = True
    else:
        invert_depth = False
        font_size = 1
        press_on = False
        dialog.text_moving = False

    if num < len(object_list) - 1 and not press_on:
        num += 1
    elif num == len(object_list) - 1 and not press_on:
        num = 0

    if press_on:
        if font_size < 10:
            font_size += 1
            font.size = int(font_size)
        if not (dialog.mini_game or dialog.message or dialog.choose):
            dialog.text_moving = True
            back = pygame.Rect(player.rect.x + 62, int(player.rect.y + 27 + dialog.font_y), font_size * 9, font_size * 2 + 3)
            pygame.draw.rect(screen, (0, 0, 0), back)
            font.render_to(screen, (player.rect.x + 65, int(player.rect.y + 30 + dialog.font_y)), 'Aperte "E"', (255, 255, 255))
        if dialog.choose:
            back = pygame.Rect(0, 480, 800, 120)
            pygame.draw.rect(screen, (0, 0, 0), back)
            dialog.font1.render_to(screen, (25, 500),'Aperte "R" para roubar                  Aperte "f" para  interagir',(255, 255, 255))
            dialog.font3.render_to(screen, (25, 560), 'Aperte "ESC" para voltar', (255, 255, 255))
            if player.rect.colliderect(farao.rect):
                level_swap = True
            else:
                level_swap = False
        if dialog.message:
            dialog.choose = False
            dialog.dialog_type(2, num + 11, False, screen, HEIGHT)
        if dialog.mini_game:
            dialog.tutorial = True
            dialog.dialog_type(2, 4, True, screen, HEIGHT)
            if dialog.text in dialog.used_texts:
                dialog.tutorial = False
                stealing.steal(screen, object_list[num])
            dialog.choose = False
            if stealing.exit:
                dialog.mini_game = False


level_swap = False

cont = 0
animation = False


def animated_1():
    global cont, camera_on, animation
    if fade_num <= 200:
        if cont <= 60:
            player.moved = True
            player.player_action = 'walk_side'
            player.player_flip = True
            cont += 1
            player.x -= 1
        else:
            player.player_action = 'idle_side'
            player.moved = False
            if dialog.page == 0:
                dialog.expression = 'normal'
            elif dialog.page == 1:
                dialog.expression = 'risada'
            dialog.dialog_type(2, 0, True, screen, HEIGHT)
            if dialog.text in dialog.used_texts:
                camera_on = False
                if cont <= 260:
                    camera[0] -= 6
                    cont += 1
                else:
                    camera_on = True
                    if dialog.page == 0:
                        dialog.expression = 'normal'
                    elif dialog.page == 1:
                        dialog.expression = 'raiva'
                    dialog.dialog_type(2, 1, True, screen, HEIGHT)
                    if dialog.text in dialog.used_texts:
                        if cont <= 300:
                            player.player_action = 'walk_side'
                            player.moved = True
                            cont += 1
                            player.x -= 2
                            player.y += 2
                        else:
                            player.moved = False
                            player.player_action = 'idle_side'
                            if dialog.page == 0:
                                dialog.expression = 'desejo'
                            elif dialog.page == 1:
                                dialog.expression = 'normal'
                            dialog.dialog_type(2, 2, True, screen, HEIGHT)
                            if dialog.text in dialog.used_texts:
                                animation = False
                                cont = 0


def animated_2():
    global cont, camera_on, animation, fade_on
    dialog.expression = 'medo'
    dialog.dialog_type(1, 9, True, screen, HEIGHT)
    player.last_dir = ''
    if dialog.text in dialog.used_texts:
        if cont <= 40:
            player.player_action = 'walk_front'
            player.moved = True
            cont += 1
            player.y += 2
        else:
            player.moved = False
            if dialog.page == 0:
                dialog.expression = 'normal'
            elif dialog.page == 1:
                dialog.expression = 'raiva'
            dialog.dialog_type(2, 10, True, screen, HEIGHT)
            player.player_action = 'idle_front'
            if dialog.text in dialog.used_texts:
                camera_on = False
                if cont <= 150:
                    player.player_action = 'walk_front'
                    player.moved = True
                    cont += 1
                    player.y += 3
                else:
                   animation = False

loop = True
game_level = 'cutscene'
is_pause = False
dt = 0


def game():
    global fade_on, level_swap, loop, game_level, is_pause, animation, screen, HEIGHT, camera_on, music, dt
    """
    font_y_type = True
    font_y = 0
    """
    pixel_font = pygame.freetype.Font("data/Fipps-Regular.otf", 1)

    num_level = 1
    change_level = False

    player_type = 0

    animation_solo = False
    dialog_anim = False
    win = False

    cont = 0

    coop_mode = False
    end_coop = 0

    end_cont = 0

    sound_cont = 0

    projectile_list = []

    clock = pygame.time.Clock()

    music_lobby = False
    music_level1 = False
    music_gameover = False

    conn = Connection()

    while loop:

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if not dialog.have_letters and fade_num == 0 and not is_pause and not dialog.choose \
                        and not dialog.mini_game and not animation and not animation_solo and game_level == 'lobby':
                    if event.key == pygame.K_d:
                        player.right = True
                        player.last_dir = ''
                        player.moved = True
                        player.anim_right = True
                    if event.key == pygame.K_a:
                        player.left = True
                        player.last_dir = ''
                        player.moved = True
                        player.anim_left = True
                    if event.key == pygame.K_s:
                        player.down = True
                        player.last_dir = ''
                        player.moved = True
                        player.anim_down = True
                    if event.key == pygame.K_w:
                        player.up = True
                        player.last_dir = ''
                        player.moved = True
                        player.anim_up = True
                if dialog.mini_game:
                    if event.key == pygame.K_s:
                        stealing.down = True
                    if event.key == pygame.K_w:
                        stealing.up = True
                if event.key == pygame.K_f:
                    if dialog.have_letters:
                        dialog.page += 1
                        dialog.font_y = 0
                    if game_level == 'credit':
                        if dialog.page > 2:
                            dialog.page = 2
                    if game_level == 'cutscene':
                        fade_on = True
                        dialog.page = 0
                    if dialog.choose:
                        dialog.message = True
                if event.key == pygame.K_e:
                    if press_on and not (dialog.mini_game or dialog.message or is_pause or animation_solo or fade_on):
                        dialog.choose = True
                if event.key == pygame.K_r:
                    if dialog.choose and not (object_list[num - 1] in stealing.stealing_artifacts or player.rect.colliderect(farao.rect)):
                        dialog.mini_game = True
                    if level_swap:
                        dialog_anim = True
                if event.key == pygame.K_ESCAPE:
                    dialog.choose = False
                    dialog.message = False

            if event.type == pygame.KEYUP:
                if not animation and not dialog.mini_game:
                    if event.key == pygame.K_d:
                        player.right = False
                        player.last_dir = 'idle_right'
                        player.anim_right = False
                    if event.key == pygame.K_a:
                        player.left = False
                        player.last_dir = 'idle_left'
                        player.anim_left = False
                    if event.key == pygame.K_s:
                        player.down = False
                        player.last_dir = 'idle_down'
                        player.anim_down = False
                    if event.key == pygame.K_w:
                        player.up = False
                        player.last_dir = 'idle_up'
                        player.anim_up = False
                if dialog.mini_game:
                    if event.key == pygame.K_s:
                        stealing.down = False
                    if event.key == pygame.K_w:
                        stealing.up = False

            if game_level == 'game_over' or game_level == 'coop' or game_level == 'credit' or is_pause:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        menu.click = True

        if game_level == 'lobby':
            camera_function()

        if dialog.text_moving:
            dialog.text_y()

        if not player.right and not player.left and not player.up and not player.down:
            player.moved = False


        if game_level == 'lobby':
            music = 'Cutscenes.mid'

            if music_lobby:
                music_2.play(-1)
                if not win:
                    door_sound.play()
                music_lobby = False

            pygame.mouse.set_visible(0)

            create_map(game_map1)

            stop_render = False

            if invert_depth:
                player.render(screen, game_level)
                stop_render = True

            objects_render(object_list)

            gate.rect = pygame.Rect(gate.x - camera[0], gate.y - camera[1], gate.width, 95)
            gate_down.rect = pygame.Rect(gate_down.x - camera[0], gate_down.y - camera[1], gate_down.width, gate_down.height)
            gate_side.rect = pygame.Rect(gate_side.x - camera[0], gate_side.y - camera[1], gate_side.width, gate_side.height)
            tile_rects.append(gate_side.rect)
            tile_rects.append(gate_down.rect)
            tile_rects.append(gate.rect)

            gate.render(screen)
            gate_down.render(screen)
            gate_side.render(screen)

            objects_interaction(pixel_font)

            if not stop_render:
                player.render(screen, game_level)

            if animation:
                if not win:
                    animated_1()
                else:
                    animated_2()
            else:
                if win:
                    change_level = True
                    fade_on = True

            if player.rect.colliderect(farao.rect):
                dialog.dialog_type(1, 6, True, screen, HEIGHT)
                dialog.expression = 'desejo'
                if dialog.text not in dialog.used_texts:
                    animation_solo = True
                else:
                    animation_solo = False

            if dialog_anim:
                dialog.choose = False
                if dialog.page == 0:
                    dialog.expression = 'medo'
                elif dialog.page == 1:
                    dialog.expression = 'raiva'
                dialog.dialog_type(2, 7, True, screen, HEIGHT)
                if dialog.text in dialog.used_texts:
                    change_level = True
                    fade_on = True
                    dialog_anim = False

            move()
            player.rect = pygame.Rect(int(player.x + 50) - camera[0], int(player.y + 10) - camera[1], 62, 93)

            if player.moved:
                if sound_cont < 25:
                    sound_cont += 1
                if sound_cont == 25:
                    walk_sound.play()
                    sound_cont = 0

            if stealing.failed == 3:
                change_level = True
                fade_on = True

            if not change_level:
                fade_options(WIDTH, HEIGHT, 2)
            else:
                fade_options(WIDTH, HEIGHT, 1)
                enemy.life = 20
                player2.life = 25
                player2.x = 320
                player2.y = 450
                enemy.max_cont = 45
                enemy.x = 600
                enemy.y = 100
                projectile.cooldown_counter = 0
                projectile.horus_cont = 0
                projectile.del_cont = 0
                enemy.cont = 0
                enemy.last_decision = 0
                if fade_num >= 255:
                    music_2.stop()
                    cont = 0
                    dialog.choose = False
                    if stealing.failed == 3:
                        music_gameover = True
                        game_level = 'game_over'
                    elif win:
                        game_level = 'end'
                    else:
                        music_level1 = True
                        game_level = f'level{num_level}'
                    fade_on = True
                    change_level = False

            if not animation:
                dialog.tutorial = True
                dialog.dialog_type(1, 3, True, screen, HEIGHT)
                if dialog.text in dialog.used_texts:
                    dialog.tutorial = False

            if stealing.exit:
                dialog.tutorial = True
                dialog.dialog_type(1, 5, True, screen, HEIGHT)
                if dialog.text in dialog.used_texts:
                    dialog.tutorial = False
                    stealing.exit = False

            stealing.hud(dialog, screen)


        if game_level == 'level1':
            camera[0], camera[1] = 0, 0
            create_map(game_map2)

            pygame.mouse.set_visible(0)

            if music_level1:
                music_3.play(-1)
                music_level1 = False

            if not is_pause:

                if not fade_on:
                    player2.render(screen, game_level)

                    if not coop_mode:
                        dialog.dialog_type(1, 8, True, screen, HEIGHT)
                        dialog.tutorial = True
                    else:
                        dialog.used_texts.append(dialog.text)
                    if dialog.text in dialog.used_texts:
                        dialog.tutorial = False
                        if cont < 50:
                            cont += 1
                    if cont == 50:
                        mx, my = pygame.mouse.get_pos()
                        player2.x += (mx - player2.x) / 5
                        player2.y += (my - player2.y) / 5
                        if player2.x + 61 >= WIDTH:
                            player2.x = WIDTH - 61
                        if player2.x <= 0:
                            player2.x = 0
                        if player2.y <= 100:
                            player2.y = 100
                        if player2.y + 93 >= HEIGHT:
                            player2.y = HEIGHT - 93

                        projectile.shoot_delay()
                        enemy.movement()

                        if projectile.cooldown_counter == 0:
                            projectile_sound.play()
                            projects = Projectile(0, 0)
                            projectile_list.append(projects)
                            projects.horus_position()
                            projectile.cooldown_counter = 1

                    player2.rect = pygame.Rect(int(player2.x) - camera[0], int(player2.y) - camera[1], 62, 93)

                    if player2.rect.colliderect(enemy.rect):
                        if not enemy.cooldown:
                            if not enemy.damaged:
                                enemy.life -= 1
                                enemy.damaged = True
                                horus_damage_sound.play()
                                enemy.cooldown = True
                        enemy.moving = True

            if enemy.life <= 0:
                enemy.life = 0
                win = True
                stealing.stealing_artifacts.append(farao)
                change_level = True
                fade_on = True
                player.x = 4400
                player.y = 880
                animation = True

            player_rect_horus = pygame.Rect(int(player2.x) - 200, int(player2.y) - 150, 461, 393)

            enemy.render(screen)

            for i in projectile_list:
                i.rect = pygame.Rect(i.rect.x, i.rect.y, 10, 10)
                if not win:
                    if player2.rect.colliderect(i.rect):
                        if sound_cont == 0:
                            player_damage_sound.play()
                        if sound_cont <= 10:
                            sound_cont += 1
                        else:
                            sound_cont = 0
                        if not player2.damaged:
                            player2.damaged = True
                            player2.life -= 1
                    i.horus(HEIGHT, WIDTH, projectile_list)
                if enemy.life <= 10:
                    pygame.draw.rect(screen, (0, 255, 0), player_rect_horus, 1)
                    enemy.max_cont = 35
                    i.vel_y = 5
                    i.vel_x = 5
                    if not projectile.horus_cont == 1:
                        projectile.horus_cont = 0
                        if projectile.horus_cont == 0:
                            projectile.horus_hability = True
                            projectile.horus_cont = 1
                        if projectile.horus_hability:
                            Horus_sound.play()
                            projectile.horus_hability = False
                    if player_rect_horus.colliderect(i.rect):
                        i.render(screen)
                else:
                    i.render(screen)

            player2.hud(screen)

            if player2.life <= 0:
                player2.life = 0
                change_level = True
                fade_on = True

            if player_type == 1:
                conn.player1(player2, enemy)
            elif player_type == 2:
                conn.player2(player2, enemy)

            if not change_level:
                fade_options(WIDTH, HEIGHT, 2)
            else:
                fade_options(WIDTH, HEIGHT, 1)
                if fade_num >= 255:
                    music_3.stop()
                    projectile_list.clear()
                    if coop_mode:
                        rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
                        pygame.draw.rect(screen, (0, 0, 0), rect)
                        if end_coop <= 50:
                            if win:
                                dialog.font1.render_to(screen, (300, 200),'Vocês Venceram', (255, 255, 255))
                            else:
                                dialog.font1.render_to(screen, (300, 200), 'Vocês Perderam', (255, 255, 255))
                        elif end_coop <= 80:
                            if player_type == 2:
                                dialog.font1.render_to(screen, (150, 200),
                                                       'Você foi sacrificado para seu parceiro continuar',
                                                       (255, 255, 255))
                            if player_type == 1:
                                dialog.font1.render_to(screen, (200, 200),
                                                       'Você foi escolhido para sobreviver',
                                                       (255, 255, 255))
                        else:
                            if player_type == 1:
                                end_coop = 0
                                main_menu()
                        end_coop += 1
                    else:
                        if not win:
                            music_gameover = True
                            game_level = 'game_over'

                        else:
                            music_lobby = True
                            game_level = 'lobby'
                        fade_on = True
                        change_level = False
                else:
                    end_coop = False


        if game_level == 'cutscene':
            pygame.mouse.set_visible(0)

            if dialog.page < len(cutscene):
                for i in range(len(cutscene[dialog.page])):
                    dialog.render_multi(15, 25, screen, i, cutscene, HEIGHT)
            else:
                dialog.have_letters = False
                dialog.text_moving = False
                dialog.message = False
                dialog.page = 0
                dialog.line = 0

            fade_options(WIDTH, HEIGHT, 1)

            if fade_num >= 255:
                game_level = 'lobby'
                music_1.stop()
                win = False
                player.last_dir = ''
                player.flip = False
                player.player_action = 'walk_side'
                dialog.tutorial = False
                camera_on = True
                music_lobby = True
                fade_on = True
                animation = True


        if game_level == 'game_over':
            if music_gameover:
                gameover_music.play()
                music_gameover = False

            pygame.mouse.set_visible(100)

            if stealing.failed == 3:
                menu.draw_text('Você Foi Presa', menu.font, (255, 0, 0), screen, 250, 200)
            else:
                menu.draw_text('Você Morreu', menu.font, (255, 0, 0), screen, 280, 200)

            mx, my = pygame.mouse.get_pos()

            button_again = pygame.Rect(50, 400, 260, 50)
            button_exit = pygame.Rect(450, 400, 210, 50)

            if button_again.collidepoint((mx, my)):
                if menu.click:
                    fade_on = True
                    change_level = True
            if button_exit.collidepoint((mx, my)):
                if menu.click:
                    main_menu()

            menu.click = False
            dialog.font1.render_to(screen, (70, 420), 'Tentar Novamente', (255, 255, 255))
            dialog.font1.render_to(screen, (470, 420), 'Voltar ao Menu', (255, 255, 255))

            if not change_level:
                fade_options(WIDTH, HEIGHT, 2)
            else:
                fade_options(WIDTH, HEIGHT, 1)
                if fade_num >= 255:
                    if stealing.failed == 3:
                        stealing.failed = 0
                        stealing.money = 0
                        stealing.stealing_artifacts.clear()
                        player.x = 4650
                        player.y = 2000
                        stealing.bad_endind = 0
                    music_lobby = True
                    game_level = 'lobby'
                    fade_on = True
                    change_level = False


        if game_level == 'coop':
            mx, my = pygame.mouse.get_pos()

            if not coop_mode:
                menu.draw_text('Escolha o Jogador', menu.font, (255, 255, 255), screen, 220, 100)
                button_player1 = pygame.Rect(150, 300, 110, 50)
                button_player2 = pygame.Rect(500, 300, 110, 50)
                button_back = pygame.Rect(50, 530, 150, 50)
                pygame.draw.rect(screen, (255, 255, 255), button_back)

                if button_back.collidepoint((mx, my)):
                    if menu.click:
                        main_menu()
                if button_player1.collidepoint((mx, my)):
                    if menu.click:
                        conn.connection1()
                        player_type = 1
                        game_level = 'level1'
                        coop_mode = True
                if button_player2.collidepoint((mx, my)):
                    if menu.click:
                        conn.connection2()
                        player_type = 2
                        game_level = 'level1'
                        coop_mode = True

                menu.click = False
                dialog.font4.render_to(screen, (70, 540), 'Voltar', (0, 0, 0))
                dialog.font1.render_to(screen, (160, 320), 'Player1', (255, 255, 255))
                dialog.font1.render_to(screen, (510, 320), 'Player2', (255, 255, 255))


        if game_level == 'end':
            screen.blit(end_message_img, (0, 0))

            fade_options(WIDTH, HEIGHT, 2)

            if end_cont <= 350:
                end_cont += 1
            else:
                loop = False


        if game_level == 'credit':
            pygame.mouse.set_visible(100)

            menu.draw_text('Créditos', menu.font, (255, 255, 255), screen, 280, 25)

            if dialog.page < len(credit):
                for i in range(len(credit[dialog.page])):
                    dialog.font1.render_to(screen, (15, (95 + 2 * dialog.font_size * i) + dialog.font_y),
                                           credit[dialog.page][i], (255, 255, 255))

            mx, my = pygame.mouse.get_pos()

            button_back = pygame.Rect(50, 530, 150, 50)
            pygame.draw.rect(screen, (255, 255, 255), button_back)

            if button_back.collidepoint((mx, my)):
                if menu.click:
                    main_menu()

            menu.click = False
            dialog.font4.render_to(screen, (70, 540), 'Voltar', (0, 0, 0))
            if dialog.page < 2:
                dialog.font1.render_to(screen, (600, HEIGHT - 40), 'Aperte "F"', (255, 255, 255))

        pygame.display.update()
        clock.tick(60)


def main_menu():
    global loop, game_level, music

    music_1.play(-1)

    while loop:
        pygame.mouse.set_visible(100)

        screen.fill((0, 0, 0))
        screen.blit(menu.menu_img, (0, 0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(40, 258, 120, 40)
        button_2 = pygame.Rect(40, 308, 160, 40)
        button_3 = pygame.Rect(40, 358, 100, 40)
        button_4 = pygame.Rect(40, 408, 100, 40)

        if button_1.collidepoint((mx, my)):
            if menu.click:
                game_level = 'cutscene'
                player.x = 4650
                player.y = 2000
                game()
        if button_2.collidepoint((mx, my)):
            if menu.click:
                game_level = 'credit'
                dialog.page = 0
                music_1.stop()
                game()
        if button_3.collidepoint((mx, my)):
            if menu.click:
                game_level = 'coop'
                game()
        if button_4.collidepoint((mx, my)):
            if menu.click:
                loop = False
        dialog.font4.render_to(screen, (50, 260), 'Jogar', (0, 0, 0))
        dialog.font4.render_to(screen, (50, 310), 'Créditos', (0, 0, 0))
        dialog.font4.render_to(screen, (50, 360), 'Coop', (0, 0, 0))
        dialog.font4.render_to(screen, (50, 410), 'Sair', (0, 0, 0))

        menu.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu.click = True

        pygame.display.update()


main_menu()
