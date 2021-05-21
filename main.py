import pygame
from sprites import kukla
print("ben aLoNeMaN")
pygame.init()
ekran = pygame.display.set_mode((800, 600))

devamet = True
player = kukla("./images/spritesheet.png")
x=400
y=300
ziplamaGucu=30
yukseklik=y
while devamet:
    pygame.time.Clock().tick(10)
    olaylar = pygame.event.get()
    for olay in olaylar:
        if olay.type == pygame.QUIT:
            devamet = False
    ekran.fill((255, 255, 255))

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.newYon=1
        x+=5
        player.updateKukla(ekran, x, y, "kos")
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.newYon=-1
        x-=5
        player.updateKukla(ekran, x, y, "kos")
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        ziplamaGucu-=5
        y-=5
        if yukseklik<270:
            ziplamaGucu=0
            y+=5
        player.updateKukla(ekran, x, y, "zipla")
    if not (True in pygame.key.get_pressed()):
        player.updateKukla(ekran, x, y, "dur")
    pygame.display.update()
