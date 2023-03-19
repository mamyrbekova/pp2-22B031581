import pygame as pg
import time
 
pg.init()
 
pg.display.set_caption("circle")

clock = pg.time.Clock()

WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
WHITE = (255, 255, 255)

dx, dy = 20, 20
 
x,y=WIDTH/2, HEIGHT/2
running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN and y+50<HEIGHT:
                y += dy
            if event.key == pg.K_UP and y-50>0:
                y -= dy
            if event.key == pg.K_RIGHT and x+50<WIDTH:
                x += dx
            if event.key == pg.K_LEFT and x-50>0:
                x -= dx
                
    screen.fill(WHITE)
    pg.draw.circle(screen, RED, (x,y), 50)
    pg.display.flip()
 
pg.quit()  
