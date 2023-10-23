import pygame as pg

pg.init()
font_name = pg.font.match_font('arial') # поиск шрифта arial
size = 18 # размер шрифта
W,H = 600,600
win = pg.display.set_mode((W,H)) # создание игрового окна
name = ''
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
    for y in range(0,H,25):
        for x in range(0,W,25):
            pg.draw.line(win,(0,255,0), (0,y), (W, y))
            pg.draw.line(win,(0,0,0), (x, 0), (x, H))
    pg.display.update()
