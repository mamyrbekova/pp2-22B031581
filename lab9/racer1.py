import pygame as pg, sys
from pygame.locals import *
import random, time


pg.init()


FPS = 60
FramePerSec = pg.time.Clock()


BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0



font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pg.image.load("./images/AnimatedStreet.png")

DISPLAYSURF = pg.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pg.display.set_caption("Game")


class Enemy(pg.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pg.image.load("./images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("./images/player1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pg.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


class Coin(pg.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pg.image.load("./images/coin.png")
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)
            self.random_number = random.randint(0, 6)
            self.mega()
            
        def generate_random_position(self):
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)
            while pg.sprite.spritecollide(self, enemies, False):
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50) 

        def move(self):
            self.rect.move_ip(0, SPEED)
            if (self.rect.top > SCREEN_HEIGHT):
                self.kill()

        def mega(self):
             if self.random_number in [0,1,2]:
                self.image = pg.image.load("./images/supercoin.jpg.png")
        def is_mega_coin(self):
            return self.random_number in [0,1,2]
        
        def check_collision(self, sprite):
            if pg.sprite.collide_rect(self, sprite):
                return True
            return False
       
                  
       
P1 = Player()
E1 = Enemy()

enemies = pg.sprite.Group()
enemies.add(E1)
all_sprites = pg.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)




INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 1000)

COIN_EVENT = pg.USEREVENT + 1
pg.time.set_timer(COIN_EVENT, random.randint(500, 3000))

coins = pg.sprite.Group()


while True:  
    for event in pg.event.get():
        if event.type == COIN_EVENT:
             coin = Coin()
             coins.add(coin)
             all_sprites.add(coin)
        if event.type == INC_SPEED:
            if COIN_SCORE % 10 == 0:
                SPEED += 1
            # COIN_EVENT = pg.USEREVENT + 1
            # pg.time.set_timer(COIN_EVENT, random.randint(500, 3000))

        if event.type == QUIT:
            pg.quit()
            sys.exit()


    for coin in coins:
        if coin.check_collision(P1) and coin != coin.is_mega_coin():
            COIN_SCORE += 1
            if coin.is_mega_coin():
                COIN_SCORE += 4
            coin.kill()
             


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    coin_scores = font_small.render("Coins: " + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(coin_scores, (300, 10))


    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

   
    if pg.sprite.spritecollideany(P1, enemies):
          pg.mixer.Sound('./music/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pg.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pg.quit()
          sys.exit()        
        
    pg.display.update()
    FramePerSec.tick(FPS)