#edicion 1
#por ariel
#copiado de menu

import pygame
from Loaded.Fonts import *
from gui import Gradient,Clasic,add_border

class Button(Clasic.Clasic):
    def __init__(self,Title,Background,Position,Gradient=False):
        self.Title       = Title

        if not Gradient:
            self.Background  = [Background[0],Background[1],Background[2]]
        else:
            self.Background = Background
        self.x,self.y       = Position

        self.UbuntuBoldB = ClassicFont(20)
        self.UbuntuBoldS = ClassicFont(19)
        self.UbuntuBoldSS= ClassicFont(16)
        
        self.W,self.H = [0,0]
        self.OriginalPosition = Position
        
        self.NormalSize = [200,30]
        self.FocusSize = [220,40]
        
        Surface = pygame.surface.Surface((self.W,self.H))
        
        self.UpdateSurface(Surface)
        self.SetCursorChange()
        
        self.Gradient = Gradient
        
        self.indice  = 0
        self.sentido = 1
        self.speed   = 1
        self.updating= 1
        self.loops   = 0
        
    def IncIndice(self):
        self.indice += 1
        if (self.indice >= 3):
            self.indice = 0
        
        if (self.Background[self.indice] == 255):
            self.sentido = -1
        else:
            self.sentido = 1
    def updateBackground(self):
        self.Background[self.indice] += self.sentido * self.speed
        if (self.Background[self.indice] >= 255 or self.Background[self.indice] <= 100):
            self.IncIndice()
    def UpdatePosition(self,NewPosition):
        self.OriginalPosition = NewPosition
    def graphic_update(self,SCREEN):
        
        SCREEN.blit(self.surface , (self.x,self.y))
        
    def logic_update(self,EVENTS):
        self.EVENTS = EVENTS
        self.SetEvents(EVENTS)
        if (self.Pressed()):
            self.GeneratePressed()
        elif (self.Focused()):
            self.GenerateFocused()
        else:
            self.GenerateNormal()
        if not self.Gradient:
            if (self.loops % self.updating == 0):
                self.updateBackground()
        
            self.loops += 1
        if self.Pressed():
            return self.Title
    def GenerateNormal(self):
        self.x,self.y = self.OriginalPosition
        Surface = pygame.surface.Surface(self.NormalSize)
        if not self.Gradient:
            Surface.fill(self.Background)
        else:
            Gradient.FillGradient(Surface, self.Background[0], self.Background[1])
        Surface = add_border.add_border(Surface, (0,0,0), 2, 2, 2, 2)
        
        Text = self.UbuntuBoldSS.render(self.Title,0,(0,0,0))
        TextPosition = Clasic.GetCenterPosition(Surface, Text)
        
        Surface.blit(Text,TextPosition)
        
        self.UpdateSurface(Surface)
    def GenerateFocused(self):
        self.x = self.OriginalPosition[0]-((self.FocusSize[0]-self.NormalSize[0])/2)
        self.y = self.OriginalPosition[1]-((self.FocusSize[1]-self.NormalSize[1])/2)
        Surface = pygame.surface.Surface(self.FocusSize)
        if not self.Gradient:
            Surface.fill(self.Background)
        else:
            Gradient.FillGradient(Surface, self.Background[0], self.Background[1])
        Surface = add_border.add_border(Surface, (0,0,0), 2, 2, 2, 2)
        
        Text = self.UbuntuBoldS.render(self.Title,0,(0,0,0))
        TextPosition = Clasic.GetCenterPosition(Surface, Text)
        
        Surface.blit(Text,TextPosition)
        
        self.UpdateSurface(Surface)
    def GeneratePressed(self):
        self.x = self.OriginalPosition[0]-((self.FocusSize[0]-self.NormalSize[0])/2)
        self.y = self.OriginalPosition[1]-((self.FocusSize[1]-self.NormalSize[1])/2)
        Surface = pygame.surface.Surface(self.FocusSize)
        if not self.Gradient:
            Surface.fill(self.Background)
        else:
            Gradient.FillGradient(Surface, self.Background[0], self.Background[1])
        Surface = add_border.add_border(Surface, (0,0,0), 4, 4, 4, 4)
        
        Text = self.UbuntuBoldB.render(self.Title,0,(0,0,0))
        TextPosition = Clasic.GetCenterPosition(Surface, Text)
        
        Surface.blit(Text,TextPosition)
        
        self.UpdateSurface(Surface)