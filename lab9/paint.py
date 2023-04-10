import pygame as pg
from math import cos, sin , pi 
pg.init()
WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
font = pg.font.SysFont("Verdana", 15)
cur_color = 'black'


def menu():
    
    
    green = pg.draw.rect(screen, (0, 255, 0), [WIDTH - 35, 10, 25, 25])
    blue = pg.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 35, 25, 25])
    red = pg.draw.rect(screen, (255, 0, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pg.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    purple = pg.draw.rect(screen, (128, 0, 32), [WIDTH - 85, 10, 25, 25])
    dark_green = pg.draw.rect(screen, (153, 153, 0), [WIDTH - 85, 35, 25, 25])
    pink = pg.draw.rect(screen, (255, 192, 203), [WIDTH - 110, 10, 25, 25])
    gray = pg.draw.rect(screen, (128, 128, 128), [WIDTH - 110, 35, 25, 25])
    color = [green, blue, red, yellow, purple, dark_green, pink, gray]
    rgb = [(0, 255, 0), (0, 0, 255),(255, 0, 0), (255, 255, 0),(128, 0, 32),(153, 153, 0),(255, 192, 203),(128, 128, 128)]

    return color, rgb

def get_distance(a,b): 
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

def right_triangle(screen, cur, end, d, color): 
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    difx = abs(x1-x2) 
    dify = abs(y1-y2) 
    # if x1 <= x2: 
    if y1 < y2: 
        pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 + dify), (x2, y2)], d)    
    else: 
        pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 - dify), (x2, y2)], d)    
             
    # else: 
    #     if y1 < y2: 
    #         pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 + dify), (x2, y2)], d)    
    #     else: 
    #         pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 - dify), (x2, y2)], d)    

def triangle(color, pos):
    pg.draw.polygon(screen, color, pos, 3)

def square(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    a = abs(x1-x2)
    if x1 <= x2:
        if y1 < y2:
            pg.draw.rect(screen, color, (x1, y1, a, a), d)
        else:
            pg.draw.rect(screen, color, (x1, y2, a, a), d)
    else:
        if y1 < y2:
            pg.draw.rect(screen, color, (x2, y1, a, a), d)
        else:
            pg.draw.rect(screen, color, (x2, y2, a, a), d)

def rhombus(color, pos):
    pg.draw.polygon(screen, color, pos, 3)

# def circle(screen, color, center, radius, d):
#     pg.draw.circle(screen, color, center, 3, d)

def rectangle(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    if x1 <= x2:
        if y1 <= y2:
            pg.draw.rect(screen, color, (x1, y1, abs(x1 - x2), abs(y1 - y2)), d)
        else:
            pg.draw.rect(screen, color, (x1, y2, abs(x1 - x2), abs(y1 - y2)), d)
    else:
        if y1 <= y2:
            pg.draw.rect(screen, color, (x2, y1, abs(x1 - x2), abs(y1 - y2)), d)
        else:
            pg.draw.rect(screen, color, (x2, y2, abs(x1 - x2), abs(y1 - y2)), d)


last_pos = (0, 0)
w = 2
draw_line = False
erase = False
ed = 50

di = {
    'sqr': False,
    'triangle': False,
    'rhombus': False,
    'right_triangle': False,
    'rectangle': False,
    'circle': False
}
screen.fill((255,255,255))
# screen.blit(surf, (0,0))
running = True
while running:
    pos = pg.mouse.get_pos()
    colors, rgbs = menu()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    cur_color = rgbs[i]

                  
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                di['sqr'] = True
                for i, j in di.items(): # for i in di.keys():
                    if i != 'sqr':
                        di[i] = False
            if event.key == pg.K_2:
                di['triangle'] = True
                for i, j in di.items():
                    if i != 'triangle':
                        di[i] = False
            if event.key == pg.K_3:
                di['rhombus'] = True
                for i, j in di.items():
                    if i != 'rhombus':
                        di[i] = False
            if event.key == pg.K_4:
                di['right_triangle'] = True
                for i, j in di.items():
                    if i != 'right_triangle':
                        di[i] = False
            if event.key == pg.K_5:
                di['rectangle'] = True
                for i, j in di.items():
                    if i != 'rectangle':
                        di[i] = False
                        di[i] = False
            if event.key == pg.K_6:
                di['circle'] = True
                for i, j in di.items():
                    if i != 'circle':
                        di[i] = False
                 
        elif di['sqr'] == True:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                square(screen, last_pos, pos, w, cur_color)
               
        elif di['triangle'] == True:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                d = get_distance(last_pos, pos)
                triangle(cur_color,[last_pos, pos,((pos[0] - last_pos[0])*cos(pi/3) - (pos[1] - last_pos[1])*sin(pi/3) + last_pos[0], (pos[0] - last_pos[0])*sin(pi/3) + (pos[1] - last_pos[1])*cos(pi/3) + last_pos[1])])
        if di['right_triangle'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                right_triangle(screen, last_pos, pos, w, cur_color)
        elif di['rhombus'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                d = get_distance(last_pos, pos)
                rhombus(cur_color, [last_pos, (last_pos[0] + d, last_pos[1]), (pos[0] + d, pos[1]), pos])
        elif di['rectangle'] == True:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                rectangle(screen, last_pos, pos, w, cur_color)
        # elif di['circle'] == 1:
        #     if event.type == pg.MOUSEBUTTONDOWN:
        #         last_pos = pos
        #     if event.type == pg.MOUSEBUTTONUP:
        #         circle(screen, cur_color, pos,last_pos, w)
        txt = font.render("square - 1 right triangle - 2 rhombus - 3 equivalent triangle - 4 rectangle - 5 ", True, (255,0,0))
        screen.blit(txt, (0,0))
    pg.display.update()
pg.quit()

