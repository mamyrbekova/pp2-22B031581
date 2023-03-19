import pygame as pg
from datetime import datetime



pg.init()

WIDTH = 800
HEIGHT = 600
FPS = 45
BLACK = (0,0,0)

pg.display.set_caption('clock')
screen = pg.display.set_mode((WIDTH, HEIGHT))


clock = pg.time.Clock()

base = pg.image.load("./images/photo.jpg")
h = pg.image.load("./images/small1.png")
h2 = pg.image.load("./images/1.png")

def time(t):
    return 360 - t * 6

def rotate(surface, image, pos, angle):
    images = pg.transform.rotate(image, angle)
    rect = images.get_rect(center = image.get_rect(topleft = pos).center)

    surface.blit(images, rect)
running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(base, (0,0))
    t = datetime.now()
    sec_angle = time(t.second)
    min_angle = time(t.minute)
    rotate(screen, h2, (255, 150), sec_angle)
    rotate(screen, h, (255, 150), min_angle)
    
    pg.display.flip()

pg.quit()