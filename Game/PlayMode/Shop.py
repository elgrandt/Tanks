'''
Created on 15/03/2014

@author: Dylan
'''
import Loaded.Images as img
import Loaded.Fonts as Fonts
import pygame
import gui

class Shop:
    def __init__(self,Players):
        self.__Players = Players
        self.Weapons = img.Weapons
        self.ExtraObjects = img.Extras
        self.__Finished = False
        self.WeaponsSurfaces = []
        self.PosWeaponsSurfaces = []
        for q in range(len(self.Weapons)):
            self.PosWeaponsSurfaces.append([0,0])
        self.ExtrasSurfaces = []
        self.PosExtrasSurfaces = []
        for q in range(len(self.ExtraObjects)):
            self.PosExtrasSurfaces.append([0,0])
        self.PlayerAct = 0
        self.ChangedWeapon = True
        self.ChangedExtras = True
        self.WeaponsSurfacesState = 0
        self.ExtrasSurfacesState = 0
        
        ###  GENERATING MAX SIZE OF TEXT  ###
        
        self.MaxSizeX = 0
        for q in range(len(self.Weapons)):
            S = self.Render(self.Weapons[q]["Title"]).get_size()
            if S[0] > self.MaxSizeX:
                self.MaxSizeX = S[0]
        
        for q in range(len(self.ExtraObjects)):
            S = self.Render(self.ExtraObjects[q]["Title"]).get_size()
            if S[0] > self.MaxSizeX:
                self.MaxSizeX = S[0]
        self.MaxSizeX += 10
        
        ###  SURFACE INFO  ###

        self.Altura = 28
        self.SizeSurface = [int(self.Altura*6.5)+self.MaxSizeX,self.Altura]
        
        ###  BUTTON SEND  ###
        
        self.TextButton = "NEXT PLAYER"
        self.SizeButton = (200,40)
        self.Button = self.CreateButton(self.TextButton,self.SizeButton)
        self.PosButton = [0,0]
    def GetFinished(self):
        return self.__Finished
    def Render(self,Text,Color=(0,0,0)):
        Font = Fonts.ClassicFont(18)
        return Font.render(str(Text),1,Color)
    def graphic_update(self,Screen):
        if not self.__Finished:
            
            ###  BLITING WEAPONS AN EXTRAS SURFACES  ###
            
            SeparatorSpace = 5
            WeaponsXPos = Screen.get_size()[0]/2-20-self.SizeSurface[0]
            TotalYsize = (self.SizeSurface[1]+SeparatorSpace)*len(self.WeaponsSurfaces)-SeparatorSpace
            Ystart = Screen.get_size()[1]/2-TotalYsize/2
            Yact = Ystart
            for q in range(len(self.WeaponsSurfaces)):
                if self.WeaponsSurfacesState:
                    PosAct = (WeaponsXPos,Yact)
                    self.PosWeaponsSurfaces[q] = PosAct
                    Screen.blit(self.WeaponsSurfaces[q]["Surface"],PosAct)
                    Yact += self.WeaponsSurfaces[q]["Surface"].get_size()[1]+SeparatorSpace
            
            ExtrasXPos = Screen.get_size()[0]/2+20
            Yact = Ystart
            for q in range(len(self.ExtrasSurfaces)):
                if self.ExtrasSurfacesState:
                    PosAct = (ExtrasXPos,Yact)
                    self.PosExtrasSurfaces[q] = PosAct
                    Screen.blit(self.ExtrasSurfaces[q]["Surface"],PosAct)
                    Yact += self.ExtrasSurfaces[q]["Surface"].get_size()[1]+SeparatorSpace
            
            ###  GENERATING SEND BUTTON  ###
            
            self.Button = self.CreateButton(self.TextButton, self.SizeButton)
            self.PosButton = [WeaponsXPos + self.SizeSurface[0]/2 - self.Button.get_size()[0]/2, Ystart+TotalYsize+10]
            Screen.blit(self.Button,self.PosButton)
            
            ###  BLITTING MONEY INFORMATION  ###
            
            Font = Fonts.ClassicFont(20)
            Money = Font.render("$ "+str(self.__Players[self.PlayerAct]["Money"]),1,(255,255,255))
            Screen.blit(Money,(10,10))
            
    def logic_update(self,Events):
        if not self.__Finished:
            ###  GENERATING SURFACES  ###
            
            if self.ChangedWeapon:
                self.ChangedWeapon = False
                self.GenerateWeaponsSurface()
            if self.ChangedExtras:
                self.ChangedExtras = False
                self.GenerateExtrasSurfaces()
            if Events.mouse.get_now_pressed()[0]:
                
                ###  CHECKING SEND BUTTON PRESSED  ###
                
                if gui.Clasic.GetFocused(Events, self.PosButton, self.SizeButton):
                    self.PlayerAct += 1
                    if self.PlayerAct > len(self.__Players)-1:
                        self.__Finished = True
                    elif self.PlayerAct == len(self.__Players)-1:
                        self.TextButton = "START!"
                    self.ChangedWeapon = True
                    self.ChangedExtras = True
                
                ###  CHECKING ALL WEAPONS PRESSED  ###
                
                for q in range(len(self.WeaponsSurfaces)):
                    if self.WeaponsSurfacesState:
                        if gui.Clasic.GetFocused(Events, self.PosWeaponsSurfaces[q], self.WeaponsSurfaces[q]["Surface"].get_size()):
                            if self.__Players[self.PlayerAct]["Money"] >= self.Weapons[q]["Price"]*1000:
                                self.__Players[self.PlayerAct]["Weapons"][q]["Actual count"] += self.Weapons[q]["Count"]
                                self.__Players[self.PlayerAct]["Money"] -= self.Weapons[q]["Price"]*1000
                                self.UpdateSurfaces()
                                break
                for q in range(len(self.ExtrasSurfaces)):
                    if self.ExtrasSurfacesState:
                        if gui.Clasic.GetFocused(Events, self.PosExtrasSurfaces[q], self.ExtrasSurfaces[q]["Surface"].get_size()):
                            if self.__Players[self.PlayerAct]["Money"] >= self.ExtraObjects[q]["Price"]*1000:
                                self.__Players[self.PlayerAct][self.ExtraObjects[q]["Title"]] += self.ExtraObjects[q]["Count"]
                                self.__Players[self.PlayerAct]["Money"] -= self.ExtraObjects[q]["Price"]*1000
                                self.UpdateSurfaces()
                                break
    def GenerateSimpleSurface(self,Image,Text,Price,Count,ActualCount):
        SurfaceAct = pygame.Surface(self.SizeSurface)
        #  Image surface
        ImageSurface = pygame.Surface((self.Altura,self.Altura))
        ImageSurface.fill((186,186,186))
        gui.add_border.add_border(ImageSurface, (0,0,0), 2, 2, 2, 2)
        TransformedImage = pygame.transform.scale(img.Vacio,ImageSurface.get_size())
        TransformedImage = gui.Clasic.BlitCenter(TransformedImage, Image)
        Reduccion = 6
        TransformedImage = pygame.transform.scale(TransformedImage,(TransformedImage.get_size()[0]-Reduccion,TransformedImage.get_size()[1]-Reduccion))
        ImageSurface = gui.Clasic.BlitCenter(ImageSurface, TransformedImage)
        #  Text surface
        TextSurface = pygame.Surface((self.MaxSizeX,self.Altura))
        TextSurface.fill((255,255,255))
        gui.add_border.add_border(TextSurface, (0,0,0), 2, 2, 2, 2)
        if self.__Players[self.PlayerAct]["Money"] >= Price*1000:
            Render = self.Render(Text)
            Active = True
        else:
            Render = self.Render(Text,(170,170,170))
            Active = False
        TextSurface = gui.Clasic.BlitCenter(TextSurface, Render)
        #  Price surface
        PriceSurface = pygame.Surface((3*self.Altura,self.Altura))
        PriceSurface.fill((186,186,186))
        gui.add_border.add_border(PriceSurface, (0,0,0), 2, 2, 2, 2)
        Render = self.Render(str(int(Price*1000)))
        PriceSurface = gui.Clasic.BlitCenter(PriceSurface, Render)
        #  Count surface
        CountSurface = pygame.Surface((self.Altura,self.Altura))
        CountSurface.fill((186,186,186))
        gui.add_border.add_border(CountSurface, (0,0,0), 2, 2, 2, 2)
        Render = self.Render(str(Count))
        CountSurface = gui.Clasic.BlitCenter(CountSurface, Render)
        #  Actual count surface
        ActualCountSurface = pygame.Surface((int(1.5*self.Altura),self.Altura))
        ActualCountSurface.fill((121,121,121))
        gui.add_border.add_border(ActualCountSurface, (0,0,0), 2, 2, 2, 2)
        Render = self.Render(ActualCount)
        ActualCountSurface = gui.Clasic.BlitCenter(ActualCountSurface, Render)
        #  Positions of surfaces
        PosImageSurface = [0,0]
        PosTextSurface = [PosImageSurface[0]+ImageSurface.get_size()[0],0]
        PosPriceSurface = [PosTextSurface[0]+TextSurface.get_size()[0],0]
        PosCountSurface = [PosPriceSurface[0]+PriceSurface.get_size()[0],0]
        PosActualCountSurface = [PosCountSurface[0]+CountSurface.get_size()[0],0]
        #  Bliting all to the surface
        SurfaceAct.blit(ImageSurface,PosImageSurface)
        SurfaceAct.blit(TextSurface,PosTextSurface)
        SurfaceAct.blit(PriceSurface,PosPriceSurface)
        SurfaceAct.blit(CountSurface,PosCountSurface)
        SurfaceAct.blit(ActualCountSurface,PosActualCountSurface)
        return [SurfaceAct,Active]
    def UpdateSurfaces(self):
        for q in range(len(self.WeaponsSurfaces)):
            if self.__Players[self.PlayerAct]["Money"] >= self.Weapons[q]["Price"]*1000:
                if self.WeaponsSurfaces[q]["Active"] == False:
                    self.UpdateWeaponSurface(q)
            else:
                if self.WeaponsSurfaces[q]["Active"] == True:
                    self.UpdateWeaponSurface(q)
        for q in range(len(self.ExtrasSurfaces)):
            if self.__Players[self.PlayerAct]["Money"] >= self.ExtraObjects[q]["Price"]*1000:
                if self.ExtrasSurfaces[q]["Active"] == False:
                    self.UpdateExtrasSurface(q)
            else:
                if self.ExtrasSurfaces[q]["Active"] == True:
                    self.UpdateExtrasSurface(q)
    def UpdateWeaponSurface(self,SurfaceToUpdate):
        SurfaceAct = self.GenerateSimpleSurface(self.Weapons[SurfaceToUpdate]["Image"], self.Weapons[SurfaceToUpdate]["Title"], self.Weapons[SurfaceToUpdate]["Price"], self.Weapons[SurfaceToUpdate]["Count"], self.__Players[self.PlayerAct]["Weapons"][SurfaceToUpdate]["Actual count"])
        self.WeaponsSurfaces[SurfaceToUpdate] = {"Surface":SurfaceAct[0],"Active":SurfaceAct[1]}
    def UpdateExtrasSurface(self,SurfaceToUpdate):
        SurfaceAct = self.GenerateSimpleSurface(self.ExtraObjects[SurfaceToUpdate]["Image"], self.ExtraObjects[SurfaceToUpdate]["Title"], self.ExtraObjects[SurfaceToUpdate]["Price"], self.ExtraObjects[SurfaceToUpdate]["Count"], self.__Players[self.PlayerAct][self.ExtraObjects[SurfaceToUpdate]["Title"]])
        self.ExtrasSurfaces[SurfaceToUpdate] = {"Surface":SurfaceAct[0],"Active":SurfaceAct[1]}
    def GenerateWeaponsSurface(self):
        self.WeaponsSurfacesState = 0
        self.WeaponsSurfaces = []
        for q in range(len(self.Weapons)):
            SurfaceAct = self.GenerateSimpleSurface(self.Weapons[q]["Image"], self.Weapons[q]["Title"], self.Weapons[q]["Price"], self.Weapons[q]["Count"], self.__Players[self.PlayerAct]["Weapons"][q]["Actual count"])
            self.WeaponsSurfaces.append({"Surface":SurfaceAct[0],"Active":SurfaceAct[1]})
        self.WeaponsSurfacesState = 1
    def GenerateExtrasSurfaces(self):
        self.ExtrasSurfacesState = 0
        self.ExtrasSurfaces = []
        for q in range(len(self.ExtraObjects)):
            SurfaceAct = self.GenerateSimpleSurface(self.ExtraObjects[q]["Image"], self.ExtraObjects[q]["Title"], self.ExtraObjects[q]["Price"], self.ExtraObjects[q]["Count"], self.__Players[self.PlayerAct][self.ExtraObjects[q]["Title"]])
            self.ExtrasSurfaces.append({"Surface":SurfaceAct[0],"Active":SurfaceAct[1]})
        self.ExtrasSurfacesState = 1
    def CreateButton(self,Text,Size):
        PrincipalSurface = pygame.transform.scale(img.Vacio,Size)
        Background = pygame.Surface(Size)
        Background.fill((255,255,255))
        Background.set_alpha(100)
        PrincipalSurface.blit(Background,(0,0))
        Font = Fonts.ClassicFont(22)
        Render = Font.render(Text,0,(255,0,0))
        PrincipalSurface = gui.Clasic.BlitCenter(PrincipalSurface, Render)
        return PrincipalSurface