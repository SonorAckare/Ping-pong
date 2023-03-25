import pygame as pg
from random import randint
pg.init()
window=pg.display.set_mode((1920, 1080))
pg.display.set_caption("Ping pong")
x2=5
y2=5
gameover="win.png"
class GameSprite():
    def __init__(self, img, x, y, width, height, speed):
        self.image=pg.transform.scale(pg.image.load(img),(width, height))
        self.width=width
        self.height=height
        self.rect=self.image.get_rect()
        self.rect.x=x        
        self.rect.y=y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Ball(GameSprite):
    def move(self):
        global player, player2, x2, y2
        self.rect.x+=x2
        self.rect.y+=y2
        if self.rect.y>980:
            y2=-5
        if self.rect.y<0:
            y2=5
        if pg.sprite.collide_rect(self,player):
            x2=5
        if pg.sprite.collide_rect(self,player2):
            x2=-5
gameover="lose.png"
game=False
class Player(GameSprite):
    def control(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.y>0:
            self.rect.y-=self.speed
        if keys[pg.K_s] and self.rect.y<880:
            self.rect.y+=self.speed
    def control2(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.y>0:
            self.rect.y-=self.speed
        if keys[pg.K_DOWN] and self.rect.y<880:
            self.rect.y+=self.speed
bg = GameSprite("fon.png", 0, 0, 1920, 1080, 0)
player = Player("palka.png", 0,280, 20, 200, 15)
player2 = Player("palka.png",1900,680, 20, 200, 15)
ball=Ball("vz.png",900,500,100,100, 10)
lable=pg.font.SysFont("Arial", 50).render ("lose", True, "red")
while True:
    pg.time.Clock().tick(60)
    for i in pg.event.get():
        if i.type==pg.QUIT:
            exit()
    bg.reset()
    player.reset()
    player.control()
    player2.reset()
    player2.control2()
    ball.reset()
    ball.move()
    if ball.rect.x<0:
        window.blit(lable,(900,500))
    if ball.rect.x>1920:
        window.blit(lable,(900,500))
    pg.display.flip()