import pygame
from sprites import kukla
print("ben Alper")
pygame.init()
ekran = pygame.display.set_mode((800, 600))

devamet = True
player = kukla("./images/spritesheet.png")

while devamet:
    pygame.time.Clock().tick(10)
    olaylar = pygame.event.get()
    for olay in olaylar:
        if olay.type == pygame.QUIT:
            devamet = False
    ekran.fill((255, 255, 255))

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.newYon=1
        player.updateKukla(ekran, 400, 300, "kos")
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.newYon=-1
        player.updateKukla(ekran, 400, 300, "kos")
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        player.updateKukla(ekran, 400, 300, "zipla")
    if not (True in pygame.key.get_pressed()):
        player.updateKukla(ekran, 400, 300, "dur")
    pygame.display.update()
