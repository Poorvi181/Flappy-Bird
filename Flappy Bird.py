import pygame,sys,random
flying=False
gameover=False
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
fps= 60
font= pygame.font.SysFont("Bauhaus 93",60)
score= 0
pipegap=150
pipefrequency= 1500
lastpipe=pygame.time.get_ticks()
clock= pygame.time.Clock()
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
Pipegroup= pygame.sprite.Group()
def drawtext(text,x,y):
    txt= font.render(text,True,"navy")
    screen.blit(txt,(x,y))
class pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        super().__init__()
        self.image= pygame.image.load("GameDev2/pipe.png")
        self.rect= self.image.get_rect()
        if position== 1:
            self.image= pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft= [x,y-int(pipegap/2)]
        elif position== -1:
            self.rect.topleft= [x,y+int(pipegap/2)]
    def update(self):
        self.rect.x-=speed
        if self.rect.right<0:
            self.kill()
while True:
    clock.tick(fps)
    screen.blit(bg1,(0,0))
    Birdgroup.draw(screen)
    Birdgroup.update()
    if flying==True and gameover==False:
        timenow= pygame.time.get_ticks()
        if timenow- lastpipe > pipefrequency:
            pipeheight=random.randint(-100,100)
            toppipe= pipe(screenwidth,screenheight/2+pipeheight,1)
            bottompipe= pipe(screenwidth,screenheight/2+pipeheight,-1)
            Pipegroup.add(toppipe)
            Pipegroup.add(bottompipe)
            lastpipe=timenow
    Pipegroup.draw(screen)
    Pipegroup.update()
    screen.blit(bg2,(groundvel,550))
    groundvel-= speed
    drawtext(str(score),40,35)
    if abs(groundvel)>35:
        groundvel= 0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
