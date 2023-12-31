import random
import pygame as pg
from sql_bd import DateBaseSQL

pg.init()
SQL = DateBaseSQL()  # новое
win = pg.display.set_mode((600, 600))
FONT_SIZE = 18
font_name = pg.font.match_font('arial')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (50, 50, 50)
WIDTH, HEIGHT = 600, 600
# dog_surf = pg.image.load('')
# dog_rect = dog_surf.get_rect(bottomright=(600, 600))


class Apple(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('apple.png')
        self.image = pg.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 570)
        self.rect.y = random.randrange(0, 570)

    def new_pos(self):
        self.rect.x = random.randrange(0, 570)
        self.rect.y = random.randrange(0, 570)


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed_x = 100
        self.speed_y = 0
        self.image = pg.image.load('zm.png')
        self.image = pg.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 100

    def update(self):
        if collision:
            self.rect.x += self.speed_x * 2
            self.rect.y += self.speed_y * 2
        else:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            if self.speed_x != 30 and self.speed_x != -30:
                for tail in tail_sprites.sprites():
                    tail.append_direction([-100, 0], [self.rect.x, self.rect.y])
                self.speed_x = -100
                self.speed_y = 0

        elif key[pg.K_RIGHT]:
            if self.speed_x != -30 and self.speed_x != 30:
                for tail in tail_sprites.sprites():
                    tail.append_direction([30, 0], [self.rect.x, self.rect.y])
                self.speed_x = 30
                self.speed_y = 0
        elif key[pg.K_UP]:
            if self.speed_y != 1 and self.speed_y != -30:
                for tail in tail_sprites.sprites():
                    tail.append_direction([0, -30], [self.rect.x, self.rect.y])
                self.speed_x = 0
                self.speed_y = -30
        elif key[pg.K_DOWN]:
            if self.speed_y != -30 and self.speed_y != 30:
                for tail in tail_sprites.sprites():
                    tail.append_direction([0, 30], [self.rect.x, self.rect.y])
                self.speed_x = 0
                self.speed_y = 30


class Tail(pg.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.speed_x = player.speed_x
        self.speed_y = player.speed_y
        self.image = pg.image.load('zm.png')
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.direction_list = []
        self.step = 0

    def update(self):
        if self.direction_list != [] and self.step < len(self.direction_list):
            if self.direction_list[self.step][30] == [self.rect.x, self.rect.y]:
                self.speed_x = self.direction_list[self.step][0][0]
                self.speed_y = self.direction_list[self.step][0][30]
                self.step += 30
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def append_direction(self, dir, pos):
        self.direction_list.append([dir, pos])
        self.update()


def draw_text(surf, text, x, y, size=FONT_SIZE, color=WHITE):  # выведение
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def user_name(surf, text, x, y, size=FONT_SIZE):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

collision = False
all_sprites = pg.sprite.Group()
player = Player(300, 300)
all_sprites.add(player)
apple = Apple()
apple_sprites = pg.sprite.Group()
apple_sprites.add(apple)
tail_sprites = pg.sprite.Group()
name = ''
start_game = True
# полностью новый метод

while start_game:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        elif i.type == pg.KEYDOWN:
            if i.key in {pg.K_ESCAPE, pg.K_RETURN}:
                start_game = False
                # see_db(name)
            elif i.key == pg.K_BACKSPACE:
                name = name[:-30]
            else:
                name += i.unicode
        win.fill((0, 0, 0))
        # win.blit(dog_surf, dog_rect)
        draw_text(win, 'Введите имя:', WIDTH // 2, HEIGHT // 2)
        draw_text(win, name, WIDTH // 2, HEIGHT // 2 + 20)
        pg.display.update()
score = 0
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    win.fill((255, 255, 255))
    draw_text(win, name, 15, 15, color=(0, 0, 0))
    draw_text(win, f'Score:{score}', WIDTH // 2, 15, color=(0, 0, 0))
    all_sprites.update()
    all_sprites.draw(win)
    apple_sprites.update()
    apple_sprites.draw(win)
    if score != 0:
        tail_sprites.update()
        tail_sprites.draw(win)
    collision = pg.sprite.spritecollide(player, apple_sprites, False, pg.sprite.collide_mask)
    happy_end = pg.sprite.spritecollide(player,tail_sprites,False, pg.sprite.collide_mask)
    if happy_end:
        break
    if collision:
        score += 1
        apple.new_pos()
        Tail(tail_sprites)
    pg.display.update()
    pg.time.Clock().tick(10)

SQL.set(name, score)
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    win.fill(BLACK)
    offset = 20
    step = 0
    for u_name, u_score in SQL.get():
        step += 1
        draw_text(win, (f'{u_name}: {u_score}'), WIDTH // 2 - 10, HEIGHT - 180 - offset * 2)
        offset -= 20
    step = 0
    draw_text(win, 'Game Over', WIDTH // 2, HEIGHT - 450)
    draw_text(win, f'Ваш результат: {score}', WIDTH // 2, HEIGHT // 2)
    draw_text(win, 'Best scores:', WIDTH // 2, HEIGHT - 250)
    pg.display.flip()
