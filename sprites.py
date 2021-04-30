import pygame

class kukla():
    durus=((0,0,40,50),(35,0,40,50),(75,0,40,50))
    kosma=((0,90,35,45),(30,90,40,45),(70,90,50,45),(120,90,45,45),(155,90,40,45),
           (190,90,35,45),(222,90,35,45),(255,90,45,45),(300,90,35,45),(330,90,35,45))
    yaralanma=((0,50,40,45),
               (35,50,40,45),
               (75,50,40,45),
               (115,50,40,45),
               (150,50,40,45),
               (190,50,35,45),
               (230,50,35,45),
               (265,50,35,45),
               (300,50,35,45))
    vur=((335,50,55,45))
    geriye_don=((0,132,35,45),
                (40,132,35,45),
                (80,132,45,45),
                (125,132,45,45))
    ziplama=((125,0,45,50),
             (170,0,45,50),
             (220,0,45,50))
    resimIndex=-1
    kosuIndex=-1
    geriye_donIndex=-1
    yaralanmaIndex=-1
    yon=1
    ziplamaIndex=-1
    newYon=1
    def __init__(self,resim):
        self.resim=pygame.image.load(resim)
    def getImage(self,x,y,width,height):
        image=pygame.Surface((width,height))
        image.blit(self.resim,(0,0),(x,y,width,height))
        image.set_colorkey((0,0,0))
        return image

    def durusAnimation(self):
        self.resimIndex+=1
        if self.resimIndex>2: self.resimIndex=0
        resxy=self.durus[self.resimIndex]
        # return self.getImage(resxy[0],resxy[1],resxy[2],resxy[3])
        if self.yon == 1:
            return self.getImage(resxy[0], resxy[1], resxy[2], resxy[3])
        if self.yon == -1:
            return pygame.transform.flip(self.getImage(resxy[0], resxy[1], resxy[2], resxy[3]), True, False)
    @property
    def kosmaAnimation(self):
        self.kosuIndex += 1
        if self.kosuIndex > 9: self.kosuIndex = 0
        resxy = self.kosma[self.kosuIndex]
        if self.newYon==self.yon:
            if self.yon==1:
                return self.getImage(resxy[0], resxy[1], resxy[2], resxy[3])
            else:
                return pygame.transform.flip(self.getImage(resxy[0], resxy[1], resxy[2], resxy[3]),True,False)
        else:
            self.geriye_donIndex += 1
            if self.geriye_donIndex > 3:
                self.geriye_donIndex = 0
                self.yon=-self.yon

            resxy = self.geriye_don[self.geriye_donIndex]
            # return self.getImage(resxy[0], resxy[1], resxy[2], resxy[3])
            # if self.newYon==self.yon:
            if (self.yon==1):
                return self.getImage(resxy[0], resxy[1], resxy[2], resxy[3])
            else:
                return pygame.transform.flip(self.getImage(resxy[0], resxy[1], resxy[2], resxy[3]),True,False)

    def yaralanmaAnimation(self):
        self.yaralanmaIndex+=1
        if self.yaralanmaIndex > 9: self.yaralanmaIndex = 0
        resxy = self.yaralanma[self.yaralanmaIndex]
        return self.getImage(resxy[0], resxy[1], resxy[2], resxy[3])

    def geriye_donAnimation(self):
        self.geriye_donIndex += 1
        if self.geriye_donIndex > 3:
            self.geriye_donIndex = 0
        resxy = self.geriye_don[self.geriye_donIndex]
        if self.yon==1:
            return self.getImage(resxy[0], resxy[1], resxy[2], resxy[3])
        if self.yon==-1:
            return pygame.transform.flip(self.getImage(resxy[0], resxy[1], resxy[2], resxy[3]),True,False)
        # return
    def vurAnimation(self):
        res=self.vur[0]
        return self.getImage(res[0], res[1], res[2], res[3])
        if self.yon == 1:
            return self.getImage(res[0], res[1], res[2], res[3])
        if self.yon == -1:
            return pygame.transform.flip(self.getImage(res[0], res[1], res[2], res[3]), True, False)

    def ziplamaAnimation(self):
        self.ziplamaIndex += 1
        if self.ziplamaIndex > 2: self.ziplamaIndex = 0
        resxy = self.ziplama[self.ziplamaIndex]
        return self.getImage(resxy[0], resxy[1], resxy[2], resxy[3])
        if self.yon == 1:
            return self.getImage(resxy[0], resxy[1], resxy[2], resxy[3])
        if self.yon == -1:
            return pygame.transform.flip(self.getImage(resxy[0], resxy[1], resxy[2], resxy[3]), True, False)

    def updateKukla(self,ekran:pygame.Surface,x,y,islem):
        res=pygame.image
        self.islem=islem
        if (self.islem == "kos"): res=self.kosmaAnimation
        if (self.islem == "dur"): res=self.durusAnimation()
        # if (self.islem == "geridon"): res=self.geriye_do   nAnimation()
        if (self.islem == "yaralanma"): res = self.yaralanmaAnimation()
        if (self.islem == "zipla"): res = self.ziplamaAnimation()
        if (self.islem == "vur"): res = self.vurAnimation()
        ekran.blit(res,(x,y))
