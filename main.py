import pygame
from sprites import kukla
print("ben Alper")
print("ben ALper")
pygame.init()
ekran = pygame.display.set_mode((800, 600))

devamet = True
player = kukla("./images/spritesheet.png")
x=400
y=300
ziplamaGucu=30
yukseklik=y
havada=False
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
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        player.newYon=-1
        x-=5
        player.updateKukla(ekran, x, y, "kos")
    elif pygame.key.get_pressed()[pygame.K_SPACE]:
        if not havada:
            havada=True
            ziplamaGucu = 5
    elif havada:
        y -= ziplamaGucu
        ziplamaGucu -= 1
        if (ziplamaGucu == -5):
            havada = False
        player.updateKukla(ekran, x, y, "zipla")
    else:
        player.updateKukla(ekran, x, y, "dur")
    pygame.display.update()
