import pygame,sys
pygame.init()
screenwidth= 800
screenheight= 600
screen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Flappy Bird")
screen.fill("white")
pygame.display.update()
bg1=pygame.image.load("GameDev2/grassbg.png")
bg2=pygame.image.load("GameDev2/ground.png")
groundvel= 0
speed= 4
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images= []
        self.index= 0
        for i in range(1,4):
            img= pygame.image.load(f"GameDev2/bird{i}.png")
            self.images.append(img)
        self.image= self.images[self.index]
        self.rect= self.image.get_rect()
        self.rect.center= [x,y]
    def update(self):
        self.index+=1
        if self.index >= len(self.images):
            self.index= 0
        self.image= self.images[self.index]
flappy= Bird(100,300)
Birdgroup= pygame.sprite.Group()
Birdgroup.add(flappy)
while True:
    screen.blit(bg1,(0,0))
    screen.blit(bg2,(groundvel,550))
    groundvel-= speed
    if groundvel>35:
        pass
    Birdgroup.draw(screen)
    Birdgroup.update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
