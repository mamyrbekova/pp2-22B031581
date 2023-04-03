import pygame as pg

pg.init()

fps = 60
time = pg.time.Clock()
WIDTH = 800
HEIGHT = 600
current = 'white'

WHITE = (255, 255, 255)

screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('paint')
painting = []

def menu():
    # pg.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pg.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
    
    green = pg.draw.rect(screen, (0, 255, 0), [WIDTH - 35, 10, 25, 25])
    blue = pg.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 35, 25, 25])
    red = pg.draw.rect(screen, (255, 0, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pg.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    purple = pg.draw.rect(screen, (128, 0, 32), [WIDTH - 85, 10, 25, 25])
    black = pg.draw.rect(screen, (0, 0, 0), [WIDTH - 85, 35, 25, 25])
    pink = pg.draw.rect(screen, (255, 192, 203), [WIDTH - 110, 10, 25, 25])
    gray = pg.draw.rect(screen, (128, 128, 128), [WIDTH - 110, 35, 25, 25])
    color = [green, blue, red, yellow, purple, black, pink, gray]
    rgb = [(0, 255, 0), (0, 0, 255),(255, 0, 0), (255, 255, 0),(128, 0, 32),(0, 0, 0),(255, 192, 203),(128, 128, 128)]

    return color, rgb

def draw(a):
    for i in range(len(a)):
        pg.draw.circle(screen, a[i][0], a[i][1], a[i][2])


running = True

while running:
    time.tick(fps)
    screen.fill(WHITE)
    mouse = pg.mouse.get_pos() 
    click = pg.mouse.get_pressed()[0]
    if click and mouse[1] > 70:
        painting.append((current, mouse, 20))

    if mouse[1] > 70:
        pg.draw.circle(screen, current, mouse, 20)
    
    draw(painting)

    colors, rgbs = menu()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    current = rgbs[i]

    pg.display.flip() 
pg.quit()

