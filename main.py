import pygame
from sprites import kukla
print("ben Alper")
print("ben ALper")
pygame.init()
ekran = pygame.display.set_mode((400,300))

devamet = True
player = kukla("./images/spritesheet.png")
x=200
y=75
ziplamaGucu=30
zipla=False
yukseklik=y
havada=True
gravity=3
bg=pygame.image.load("./images/bg.png")
while devamet:
    pygame.time.Clock().tick(10)
    olaylar = pygame.event.get()
    for olay in olaylar:
        if olay.type == pygame.QUIT:
            devamet = False
        if olay.type==pygame.KEYDOWN:
            if olay.key==pygame.K_SPACE and not havada:
                havada = True
                ziplamaGucu = 40
                player.updateKukla(ekran, x, y, "dur")
    ekran.fill((255, 255, 255))
    # ground=pygame.Rect(0, 150, 400, 300)
    ground=pygame.draw.rect(ekran, (0, 0, 0),(0, 150, 400, 300))
    # ekran.blit(bg,(0,0),(x,y,1200,300))
    if pygame.key.get_pressed()[pygame.K_RIGHT] and not havada:
        player.newYon=1
        x+=5
        player.updateKukla(ekran, x, y, "kos")
    if pygame.key.get_pressed()[pygame.K_LEFT] and not havada:
        player.newYon=-1
        x-=5
        player.updateKukla(ekran, x, y, "kos")
    # if pygame.key.get_pressed()[pygame.K_SPACE] and not havada:
    #     havada=True
    #     ziplamaGucu = 20
    #     player.updateKukla(ekran, x, y, "dur")
    if havada:
        y -= ziplamaGucu
        if (y>ground.y): y=ground.y
        gravity+=1
        ziplamaGucu -= gravity
        col=pygame.Rect(x,y,player.rect.width,player.rect.height)
        print(col,ground)
        if col.colliderect(ground):
            havada = False
            gravity = 3
        player.updateKukla(ekran, x, y, "zipla")
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            x-=10
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            x+=10
    # else:
        # gravity+=1
        # colRect=pygame.Rect(x,y,player.rect.width,player.rect.height)
        # if not colRect.colliderect(ground):
        #     y+=gravity
        #     gravity=3
    if not 1 in pygame.key.get_pressed():
        player.updateKukla(ekran, x, y, "dur")
    if (y+40>ground.y):
        y-=5
        # havada=True
    else: y+=5

    pygame.display.update()
