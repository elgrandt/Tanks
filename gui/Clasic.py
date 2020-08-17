
#@Edicion 1
#Por: Ariel

#Se creo el clasic que es un conjunto de funciones para saber si un objeto esta marcado por el mouse Focused() o si esa presionado Pressed()
#al hacer una clase heredar de clasic se consiguen estos metodos

#Edicion 2
#Por: Dylan

#Agregue la funcion BlitCenter que le pasas 2 surface y te incerta el segundo surface dentro del primero centrado
#Agregue la funcion GetCenterPosition que le pasas 2 surface y devuelve la posicion en la que deberias insertar el segundo surface para que quede centrado respecto el primero 

#Edicion 3
#Por: Ariel

#agregando modificaciones para el cursor

import events

class Clasic:
    EVENTS = events.events()
    def __init__(self):
        self.EVENTS = None
        self.x,self.y = 0,0
        self.W,self.H = 0,0
        
        self.cursorChange = False
        
    def SetCursorChange(self):
        self.cursorChange = True

    def SetEvents(self,EVENTS):
        self.EVENTS = EVENTS
        
    def UpdateSurface(self,surface):
        self.W,self.H = surface.get_size()
        self.surface = surface
        
    def Focused(self): #Marcado por el mouse
        MOUSE = self.EVENTS.get_mouse()
        
        MOUSE_X = MOUSE.get_position()[0]
        MOUSE_Y = MOUSE.get_position()[1]
        
        if (MOUSE_X > self.x and MOUSE_X < self.x + self.W):
            if (MOUSE_Y > self.y and MOUSE_Y < self.y + self.H):
                try:
                    h = self.cursorChange
                except:
                    self.cursorChange = False
                return True
        return False 

    def Pressed(self,click = 0): #Presionado
        PRESSED = self.EVENTS.get_mouse().get_pressed()[click]
        
        return PRESSED and self.Focused()

def BlitCenter(Surface1,Surface2):
    Surface1.blit(Surface2,GetCenterPosition(Surface1,Surface2))
    return Surface1

def GetCenterPosition(Surface1,Surface2):
    return (Surface1.get_size()[0]/2-Surface2.get_size()[0]/2,Surface1.get_size()[1]/2-Surface2.get_size()[1]/2)

class Clasic2:
    def __init__(self):
        EVENTS = events.events()
        self.__x,self.__y = 0,0
        self.__W,self.__H = 0,0
        
        self.cursorChange = False
        
    def SetCursorChange(self          ):
        self.cursorChange = True
    def SetEvents      (self,EVENTS   ):
        self.EVENTS = EVENTS
    def UpdateSurface  (self,surface  ):
        self.__W,self.__H = surface.get_size()
        self.surface = surface
    def Focused        (self          ): #Marcado por el mouse
        MOUSE = self.EVENTS.get_mouse()
        
        MOUSE_X = MOUSE.get_position()[0]
        MOUSE_Y = MOUSE.get_position()[1]
        
        if (MOUSE_X > self.__x and MOUSE_X < self.__x + self.__W):
            if (MOUSE_Y > self.__y and MOUSE_Y < self.__y + self.__H):
                try:
                    h = self.cursorChange
                except:
                    self.cursorChange = False
                return True
        return False
    def Pressed        (self,click = 0): #Presionado
        PRESSED = self.EVENTS.get_mouse().get_pressed()[click]
        
        return PRESSED and self.Focused()

    def SetPosition(self,position):
        self.__x , self.__y = position
    def SetX       (self,x       ):
        self.__x = x
    def SetY       (self,y       ):
        self.__y = y
    def GetX       (self         ):
        return self.__x
    def GetY       (self         ):
        return self.__y
    def SumX       (self,sum     ):
        self.__x += sum
    def SumY       (self,sum     ):
        self.__y += sum
    def GetW       (self         ):
        return self.__W
    def GetH       (self         ):
        return self.__H

    def getDimensions    (self):
        return self.GetW() , self.GetH()
    def getPosition      (self):
        return (self.GetX(),self.GetY())
    def getCenterPosition(self):
        return self.GetX() + self.GetW()/2 , self.GetY() + self.GetH()/2
    def GetSurface       (self):
        return self.surface


class Clasic3:
    def __init__(self):
        EVENTS = events.events()
        self.__x,self.__y = 0,0
        self.__W,self.__H = 0,0

        self.cursorChange = False

    def SetCursorChange(self          ):
        self.cursorChange = True
    def SetEvents      (self,EVENTS   ):
        self.EVENTS = EVENTS
    def UpdateSurface  (self,surface):

        self.__W,self.__H = surface.get_size()
        self.surface = surface

    def Focused        (self          ): #Marcado por el mouse
        MOUSE = self.EVENTS.get_mouse()

        MOUSE_X = MOUSE.get_position()[0]
        MOUSE_Y = MOUSE.get_position()[1]

        if (MOUSE_X > self.__x and MOUSE_X < self.__x + self.__W):
            if (MOUSE_Y > self.__y and MOUSE_Y < self.__y + self.__H):
                try:
                    h = self.cursorChange
                except:
                    self.cursorChange = False
                return True
        return False
    def Pressed        (self,click = 0): #Presionado
        PRESSED = self.EVENTS.get_mouse().get_pressed()[click]

        return PRESSED and self.Focused()

    def SetPosition(self,position):
        self.__x , self.__y = position
    def SetX       (self,x       ):
        self.__x = x
    def SetY       (self,y       ):
        self.__y = y
    def GetX       (self         ):
        return self.__x
    def GetY       (self         ):
        return self.__y
    def SumX       (self,sum     ):
        self.__x += sum
    def SumY       (self,sum     ):
        self.__y += sum
    def GetW       (self         ):
        return self.__W
    def GetH       (self         ):
        return self.__H

    def getDimensions    (self):
        return self.GetW() , self.GetH()
    def getPosition      (self):
        return (self.GetX(),self.GetY())
    def getCenterPosition(self):
        return self.GetX() + self.GetW()/2 , self.GetY() + self.GetH()/2
    def GetSurface       (self):
        return self.surface
    def GetSurfaceStructure(self):
        return self.__surfaceStructure

def GetFocused(EVENTS,Pos,Size):
        x,y = Pos
        W,H = Size
        MOUSE = EVENTS.get_mouse()
        
        MOUSE_X = MOUSE.get_position()[0]
        MOUSE_Y = MOUSE.get_position()[1]
        if (MOUSE_X > x and MOUSE_X < x + W) and (MOUSE_Y > y and MOUSE_Y < y + H):
                return True
        return False 