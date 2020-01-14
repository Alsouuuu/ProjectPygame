import os
import pygame
from os import path

pygame.init()
pygame.font.init()
size = width, height = 1100, 619
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()


def draw(text, h, x, otstup, maxx, sh, play):
    global pravila, y_oftext, x_oftext
    #Рисую все текста на экране
    lenght = ''
    text1 = []
    if play:
        text = text.split()
        for i in text:
            if len(lenght) + len(i) + 1 < maxx:
                if lenght == '':
                    lenght = i
                else:
                    lenght += ' ' + i
            else:
                text1.append(lenght)
                lenght = i
            if i == text[-1]:
                k = 0
                while len(lenght) + k < maxx:
                    lenght = ' ' + lenght
                    k += 1
                text1.append(lenght)
    else:
        text1 = text.split('!')
    font = pygame.font.Font(None, sh)
    text = font.render('f', 1, (100, 255, 0))
    text_h = text.get_height()
    text_y = h
    for i in text1:
        if i.strip() == '*':
            x_oftext = x
            y_oftext = text_y
            text_y += otstup + text_h
        else:
            font = pygame.font.Font(None, sh)
            text = font.render(i, 1, (30, 195, 0))
            text_x = x
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            text_y += otstup + text_h
    if pravila == 1:
        font = pygame.font.Font(None, 30)
        text1 = font.render('Cоблюдайте правила PEP8!', 1, (100, 255, 0))
        text_x = 240
        text_y = 430
        screen.blit(text1, (text_x, text_y))
    elif pravila == 2:
        font = pygame.font.Font(None, 30)
        text1 = font.render('ERROR', 1, (100, 255, 0))
        text_x = 275
        text_y = 430
        screen.blit(text1, (text_x, text_y))


def print_text(message, x, y, font_color=(40, 40, 0), font_size=30):
    #Рисую текст задачи
    font = pygame.font.SysFont("GOTHIC", font_size)
    text = font.render(message, True, font_color)
    screen.blit(text, (x, y))


def get_input():
    global need_input, input_text, input_tick, x_oftext, y_oftext
    #Редактирую введенный текст
    input_rect = pygame.Rect(x_oftext + 5, y_oftext, 230, 30)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if input_rect.collidepoint(mouse[0], mouse[1]) and click[0]:
        need_input = True
    if len(input_text):
        print_text(message=input_text, x=input_rect.x, y=input_rect.y, font_size=30)
    input_tick -= 1
    if input_tick == 0:
        input_text = input_text[:-1]
    if input_tick == -20:
        input_text += '|'
        input_tick = 20

#Действия с боссами
class Gameboss:
    def __init__(self):
        global text, defen, level
        if text:
            self.karta()
            self.run()
            self.heart()

    def karta(self):
        global now, sprite, x_x, y_y
        #Рисую экран с боссами
        igrovoe.draw(screen)
        now.rect.x = x_x
        now.rect.y = y_y
        sprite.draw(screen)

    def run(self):
        global zadachi, level, text, hp
        #Рисую текст задачи
        xlevel = zadachi[level - 1][text - 1][hp].split('^^')
        draw(xlevel[0].split('#')[0], 130, 220, 10, 40, 31, True)
        draw(xlevel[1], 265, 244, 7, 50, 29, False)
        get_input()

    def return1(self):
        global text
        return text is False

    def Pravilno(self):
        global input_text, zadachi, level, text, hp, defen, pravila
        #Проверяю введный игроком текст
        xlevel = zadachi[level - 1][text - 1][hp].split('^^')[0].split('#')[1]
        m = []
        for i in xlevel.split('@'):
            if i != xlevel.split('@')[-1]:
                m.append(''.join(i[:].split()))
            else:
                m.append(''.join(i[:-1].split()))
        m1 = []
        for i in xlevel.split('@'):
            if i != xlevel.split('@')[-1]:
                m1.append(i)
            else:
                m1.append(i[:-1])
        if input_text not in m1 and ''.join(input_text.split()) in m:
            pravila = 1
        elif input_text in m1:
            if hp < 2:
                hp += 1
            else:
                hp = 0
                defen[level - 1][text - 1] = 1
                text = False
            input_text = ''
            pravila = 0
        else:
            pravila = 2

    def heart(self):
        global hp
        #Отображаю сердца
        for i in range(3 - hp):
            heart_sprite.rect.y = 420
            heart_sprite.rect.x = 655 + i * 50
            heart1.draw(screen)


class Game:
    def __init__(self):
        self.coords = person_sprite.rect
        self.coords = [self.coords[0] + self.coords[2], self.coords[1] + self.coords[3]]
        self.levels = [all_sprites, all_sprites_2]
        self.run()
        self.moution()

    def defeat(self):
        global level, person_sprite, heroes_cords, menu, defen
        #Меняю уровни
        level += 1
        if level == 3:
            level = 1
            person_sprite.rect.x = 50
            person_sprite.rect.y = 120
            enemy2_sprite.rect.x = 700
            enemy2_sprite.rect.y = 140
            enemy1_sprite.rect.x = 500
            enemy1_sprite.rect.y = 290
            enemy3_sprite.rect.x = 360
            enemy3_sprite.rect.y = 260
            defen = [[0, 0, 0], [0, 0, 0]]
            menu = True
        if level == 2:
            person_sprite.rect.x = heroes_cords[level - 1][0]
            person_sprite.rect.y = heroes_cords[level - 1][1]
            # кошка700140
            enemy2_sprite.rect.x = 500
            enemy2_sprite.rect.y = 100
            # большой паук
            enemy1_sprite.rect.x = 870
            enemy1_sprite.rect.y = 340
            # паук
            enemy3_sprite.rect.x = 180
            enemy3_sprite.rect.y = 260

    def run(self):
        global level
        #Рисую уровень
        self.levels[level - 1].draw(screen)

    def position(self, x, y):
        global level
        #Проверяю , чтобы игрок ходил только определенным координатам
        if level == 1:
            if 0 < self.coords[0] + x < 290:
                if 152 < self.coords[1] + y < 242:
                    return True
            elif 289 < self.coords[0] + x < 400:
                if 152 < self.coords[1] + y < 532:
                    return True
            elif 399 < self.coords[0] + x < 870:
                if 432 < self.coords[1] + y < 532:
                    return True
            elif 870 < self.coords[0] + x < 1000:
                if 100 < self.coords[1] + y < 532:
                    return True
            elif 999 < self.coords[0] + x < 1200:
                if 100 < self.coords[1] + y < 180:
                    return True
        elif level == 2:
            if 130 < self.coords[0] + x < 300:
                if 120 < self.coords[1] + y < 640:
                    return True
            elif 299 < self.coords[0] + x < 460:
                if 90 < self.coords[1] + y < 200:
                    return True
            elif 459 < self.coords[0] + x < 570:
                if 90 < self.coords[1] + y < 350:
                    return True
            elif 569 < self.coords[0] + x < 1100:
                if 277 < self.coords[1] + y < 370:
                    return True

    def moution(self):
        global text, defen, boss, now, sprite, x_x, y_y
        m = person_sprite.rect
        #Открытие окна с боссами
        if level == 1:
            if defen[0][0] == 0 and (220 <= m[0] <= 370 or m[0] <= 220 <= m[0] + m[2]) and \
                    (300 <= m[1] <= 370 or m[1] <= 300 <= m[1] + m[3]):
                text = 1
                enemy_3 = load_image("PAUK.png", -1)
                enemy3_sprite2 = pygame.sprite.Sprite()
                enemy3_sprite2.image = enemy_3
                enemy3_sprite2.rect = enemy3_sprite2.image.get_rect()
                sprite = pygame.sprite.Group()
                sprite.add(enemy3_sprite2)
                now = enemy3_sprite2
                x_x = 660
                y_y = 300
                sprite.add(now)

            if defen[0][1] == 0 and (520 <= m[0] <= 590 or m[0] <= 520 <= m[0] + m[2]) and \
                    (385 <= m[1] <= 535 or m[1] <= 385 <= m[1] + m[3]):
                text = 2
                enemy_1 = load_image("PAUK2.png", -1)
                enemy1_sprite2 = pygame.sprite.Sprite()
                enemy1_sprite2.image = enemy_1
                enemy1_sprite2.rect = enemy1_sprite2.image.get_rect()
                sprite = pygame.sprite.Group()
                sprite.add(enemy1_sprite2)
                x_x = 625
                y_y = 267
                now = enemy1_sprite2
                sprite.add(now)
            if defen[0][2] == 0 and (800 <= m[0] <= 870 or m[0] <= 800 <= m[0] + m[2]) and \
                    (250 <= m[1] <= 320 or m[1] <= 250 <= m[1] + m[3]):
                text = 3
                enemy_2 = load_image("KOT3.png", -1)
                enemy2_sprite2 = pygame.sprite.Sprite()
                enemy2_sprite2.image = enemy_2
                enemy2_sprite2.rect = enemy2_sprite2.image.get_rect()
                sprite = pygame.sprite.Group()
                sprite.add(enemy2_sprite2)
                x_x = 670
                y_y = 220
                now = enemy2_sprite2
                sprite.add(now)
            if (1080 <= m[0] <= 1150 or m[0] <= 1080 <= m[0] + m[2]) and \
                    (30 <= m[1] <= 180 or m[1] <= 30 <= m[1] + m[3]):
                self.defeat()
        if level == 2:
            if defen[1][0] == 0 and (40 <= m[0] <= 290 or m[0] <= 40 <= m[0] + m[2]) and \
                    (200 <= m[1] <= 270 or m[1] <= 200 <= m[1] + m[3]):
                text = 1
                enemy_3 = load_image("PAUK.png", -1)
                enemy3_sprite2 = pygame.sprite.Sprite()
                enemy3_sprite2.image = enemy_3
                enemy3_sprite2.rect = enemy3_sprite2.image.get_rect()
                sprite = pygame.sprite.Group()
                sprite.add(enemy3_sprite2)
                now = enemy3_sprite2
                x_x = 660
                y_y = 300
                sprite.add(now)
            if defen[1][1] == 0 and (500 <= m[0] <= 570 or m[0] <= 500 <= m[0] + m[2]) and \
                    (200 <= m[1] <= 400 or m[1] <= 200 <= m[1] + m[3]):
                text = 2
                enemy_2 = load_image("KOT3.png", -1)
                enemy2_sprite2 = pygame.sprite.Sprite()
                enemy2_sprite2.image = enemy_2
                enemy2_sprite2.rect = enemy2_sprite2.image.get_rect()
                sprite = pygame.sprite.Group()
                sprite.add(enemy2_sprite2)
                x_x = 670
                y_y = 220
                now = enemy2_sprite2
                sprite.add(now)
            if defen[1][2] == 0 and (920 <= m[0] <= 990 or m[0] <= 920 <= m[0] + m[2]) and \
                    (240 <= m[1] <= 440 or m[1] <= 240 <= m[1] + m[3]):
                text = 3
                enemy_1 = load_image("PAUK2.png", -1)
                enemy1_sprite2 = pygame.sprite.Sprite()
                enemy1_sprite2.image = enemy_1
                enemy1_sprite2.rect = enemy1_sprite2.image.get_rect()
                sprite = pygame.sprite.Group()
                sprite.add(enemy1_sprite2)
                x_x = 625
                y_y = 267
                now = enemy1_sprite2
                sprite.add(now)
            if (1050 <= m[0] <= 1120 or m[0] <= 1050 <= m[0] + m[2]) and \
                    (240 <= m[1] <= 440 or m[1] <= 240 <= m[1] + m[3]):
                self.defeat()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# спрайты уровня
pravila = 0
sprite = ''
# КАРТА 1
defen = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
all_sprites = pygame.sprite.Group()
karta1 = load_image("top1.jpg")
karta1_sprite = pygame.sprite.Sprite()
karta1_sprite.image = karta1
karta1_sprite.rect = karta1_sprite.image.get_rect()
all_sprites.add(karta1_sprite)
# ГЛАВНЫЙ ГЕРОЙ
one = '1.png'
two = '2.png'
person = load_image(one, -1)
person_sprite = pygame.sprite.Sprite()
person_sprite.image = person
person_sprite.rect = person_sprite.image.get_rect()
all_sprites.add(person_sprite)
person_sprite.rect.x = 50
person_sprite.rect.y = 120

# Враги
enemy2 = load_image("KOT3.png", -1)
enemy2_sprite = pygame.sprite.Sprite()
enemy2_sprite.image = enemy2
enemy2_sprite.rect = enemy2_sprite.image.get_rect()
all_sprites.add(enemy2_sprite)
enemy2_sprite.rect.x = 700
enemy2_sprite.rect.y = 140

enemy1 = load_image("PAUK2.png", -1)
enemy1_sprite = pygame.sprite.Sprite()
enemy1_sprite.image = enemy1
enemy1_sprite.rect = enemy1_sprite.image.get_rect()
all_sprites.add(enemy1_sprite)
enemy1_sprite.rect.x = 500
enemy1_sprite.rect.y = 290

enemy3 = load_image("PAUK.png", -1)
enemy3_sprite = pygame.sprite.Sprite()
enemy3_sprite.image = enemy3
enemy3_sprite.rect = enemy3_sprite.image.get_rect()
all_sprites.add(enemy3_sprite)
enemy3_sprite.rect.x = 360
enemy3_sprite.rect.y = 260

# Игровое окно
igrovoe = pygame.sprite.Group()
okno = load_image("MENYu.jpg")
okno_sprite = pygame.sprite.Sprite()
okno_sprite.image = okno
okno_sprite.rect = okno_sprite.image.get_rect()
igrovoe.add(okno_sprite)
okno_sprite.rect.x = 185
okno_sprite.rect.y = 89

# Карта 2
all_sprites_2 = pygame.sprite.Group()
karta2 = load_image("top2.jpg")
karta2_sprite = pygame.sprite.Sprite()
karta2_sprite.image = karta2
karta2_sprite.rect = karta2_sprite.image.get_rect()
all_sprites_2.add(karta2_sprite)
all_sprites_2.add(person_sprite)

all_sprites_2.add(enemy1_sprite)
all_sprites_2.add(enemy2_sprite)
all_sprites_2.add(enemy3_sprite)

# Жизни спрайты
heart1 = pygame.sprite.Group()
heart = load_image("heart.png", -1)
heart_sprite = pygame.sprite.Sprite()
heart_sprite.image = heart
heart_sprite.rect = heart_sprite.image.get_rect()
heart1.add(heart_sprite)

# спрайты меню
all_sprites2 = pygame.sprite.Group()
menu = load_image("menu.png")
menu_sprite2 = pygame.sprite.Sprite()
menu_sprite2.image = menu
menu_sprite2.rect = menu_sprite2.image.get_rect()
all_sprites2.add(menu_sprite2)

# Инструкция
instruct = pygame.sprite.Group()
menu2 = load_image("inst.png")
menu_sprite3 = pygame.sprite.Sprite()
menu_sprite3.image = menu2
menu_sprite3.rect = menu_sprite3.image.get_rect()
instruct.add(menu_sprite3)
menu_sprite3.rect.x = 150
menu_sprite3.rect.y = 100
k_k = 0

fr = load_image("213.jpg", -1)
en = pygame.sprite.Sprite()
en.image = fr
en.rect = en.image.get_rect()
all_sprites_2.add(en)
en.rect.x = 950
en.rect.y = 210
#Меняю анимацию персонажа
def animate(param1, param2):
    global person_sprite, one, all_sprites, all_sprites_2, level, k_k
    k_k += 1
    if k_k == 3:
        k_k = 0
        pygame.mixer.music.play()
    if level == 1:
        xx = person_sprite.rect.left + param1
        yy = person_sprite.rect.top + param2
        all_sprites = pygame.sprite.Group()
        all_sprites.add(karta1_sprite)
        all_sprites.add(enemy2_sprite)
        all_sprites.add(enemy3_sprite)
        all_sprites.add(enemy1_sprite)
        if one == '1.png':
            one = '2.png'
        elif one == '2.png':
            one = '3.png'
        else:
            one = '1.png'
        person = load_image(one, -1)
        person.set_colorkey((255, 255, 255))
        person_sprite = pygame.sprite.Sprite()
        person_sprite.image = person
        person_sprite.rect = person_sprite.image.get_rect()
        all_sprites.add(person_sprite)
        person_sprite.rect.x = xx
        person_sprite.rect.y = yy
    else:
        xx = person_sprite.rect.left + param1
        yy = person_sprite.rect.top + param2
        all_sprites_2 = pygame.sprite.Group()
        all_sprites_2.add(karta2_sprite)
        all_sprites_2.add(enemy2_sprite)
        all_sprites_2.add(enemy3_sprite)
        all_sprites_2.add(enemy1_sprite)
        all_sprites_2.add(en)
        if one == '1.png':
            one = '2.png'
        elif one == '2.png':
            one = '3.png'
        else:
            one = '1.png'
        person = load_image(one, -1)
        person_sprite = pygame.sprite.Sprite()
        person_sprite.image = person
        person_sprite.rect = person_sprite.image.get_rect()
        all_sprites_2.add(person_sprite)
        person_sprite.rect.x = xx
        person_sprite.rect.y = yy


# Задачи
heroes_cords = [[50, 140], [140, 500]]
m = ''
data = open('zadachi.txt', encoding='utf-8').read()
for row in data.split('\n'):
    m += ' ' + row
m = m.split('-----')
for i in range(len(m)):
    m[i] = m[i].split('---')
    for j in range(len(m[i])):
        m[i][j] = m[i][j].split('/////')
zadachi = m
x_x = 0
y_y = 0
now = ''
level = 1
hp = 0
x_oftext = 50
y_oftext = 50
input_tick = 30
input_text = '|'
instr = False
text = False
need_input = True
menu = True
running = True
pygame.mixer.music.load("trava.mp3")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if False and need_input and event.type == pygame.K_KP_ENTER:
            Gameboss().Pravilno()
        if need_input and event.type == pygame.KEYDOWN:
            input_text = input_text.replace('|', '')
            input_tick = 30
            if event.key == pygame.K_RETURN:
                Gameboss().Pravilno()
            elif event.key == pygame.K_TAB:
                input_text += '    '
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if len(input_text) < 50:
                    input_text += event.unicode
            input_text += '|'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu and 846 < event.pos[0] < 1064 and 519 < event.pos[1] < 591:
                menu = False
            elif not instr and menu:
                if 24 < event.pos[0] < 234 and 531 < event.pos[1] < 564:
                    instr = True
            elif instr and menu:
                if 916 < event.pos[0] < 950 and 99 < event.pos[1] < 132:
                    instr = False

    keys = pygame.key.get_pressed()
    #Передвижение
    if not text:
        if keys[pygame.K_DOWN]:
            if Game().position(0, 10):
                Game().moution()
                animate(0, 10)
        if keys[pygame.K_UP]:
            if Game().position(0, -10):
                Game().moution()
                animate(0, -10)
        if keys[pygame.K_RIGHT]:
            if Game().position(10, 0):
                Game().moution()
                animate(10, 0)
        if keys[pygame.K_LEFT]:
            if Game().position(-10, 0):
                Game().moution()
                animate(-10, 0)
    screen.fill((0, 0, 0))
    if text:
        Game().run()
        Gameboss()
    elif menu:
        all_sprites2.draw(screen)
        if instr:
            instruct.draw(screen)
    else:
        Game()
    clock.tick(10)
    pygame.display.flip()

pygame.quit()
