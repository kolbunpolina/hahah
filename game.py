import pygame as pg

pg.init()
font_name = pg.font.match_font('arial') # поиск шрифта arial
size = 18 # размер шрифта
W,H = 600,600
win = pg.display.set_mode((W,H)) # создание игрового окна
name = ''
class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed_x = 0
        self.apeed_y = 1
        self.image = pg.image.load('zm.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.bottom = self.y
    def update(selfself):
        for i in range(4):
            win.blit(self.image,(self.rect.x-100*i,self.rect.y))
            self.ract.x += self.speed_x
            self.y
all_sprites = pg.sprite.Group()
player = Player(300,300)
all_sprites.add(player)
def draw_text(surf, text, x,y, size=size, colir=(255,255,255)):
    def update(selfself):
        self.ract.x += self.speed_x
        self.ract.y += self.speed_y
        key = pg.key.get_prassed()
        if key[pg.K_LEFT]:
            self.speed_x = -1
def draw_text(surf, text, x,y,size=size, color=(255,255,255)):
    font = pg.font.Font(font_name, size) # определение шрифта
    text_surface = font.render(text,True,color)
    text_ract = text_surface.get_rect()
    text_ract .midtop = (x,y)
    surf.blit(text_surface, text_ract)
def user_name(surf, text, x,y,size=size):
    font = pg.font.Font(font_name, size) # определение шрифта
    text_surface = font.render(text,True,color=(255,255,255))
    text_ract = text_surface.get_rect()
    text_ract .midtop = (x,y)
    surf.blit(text_surface, text_ract)
main_loop = True
while main_loop:
    for i in pg.event.get():
        if i.type == pg.QUIT:
          exit()
        elif i.type == pg.KEYDOWN:
          if i.key == pg.K_BACKSPACE:
            name = name[: -1]
          elif i.key == pg.K_RETURN:
            main_loop = False
          else:
            name += i.unicode
    win.fill((0,0,0))
    draw_text(win, 'Введите имя:', W//2,H//2)
    draw_text(win,name, W//2,H//2 + 20)
    pg.display.update()

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    win.fill((255, 255, 255))
    all_sprites.update()
    all_sprites.draw(win)
    for y in range(0,H,25):
        for x in range(0,W,25):
            pg.draw.line(win,(0,255,0), (0,y), (W, y))
            pg.draw.line(win,(0,0,0), (x, 0), (x, H))
    pg.display.update()
