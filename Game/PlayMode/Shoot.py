'''
Created on 13/03/2014

@author: Ariel
'''
import pygame
import math

class Shoot:
    def __init__(self):
        #AUXILIAR VARIABLES
        self.__speedY = 0
    
        #SETTING DEFAULTS
        self.SetX             (600       )
        self.SetY             (200       )
        self.SetAngleDirection(-135, 12  )
        self.SetF             (0.0       )
        self.setWind          (0.0       )
        self.setGravity       (0.40      )
        self.setCircleSurface (5,(0,0,0) )
        self.Stop             (          )

    ### GRAPHIC CONFIGURING FUNCTIONS ###
    def setCustomSurface(self,surface     ):
        self.__surface = surface
        self.__W , self.__H = surface.get_size()
    def setCircleSurface(self,radius,color):
        surface = pygame.surface.Surface((radius*2,radius*2),pygame.SRCALPHA,32)
        pygame.draw.circle(surface,color,(radius,radius),radius)
        self.setCustomSurface(surface)

    ### CONFIGURING FUNCTIONS ###
    def SetAngleDirection(self,angle,speed):
        ### ANGLE GOES FROM 0 TO 360 ### DEFAULT 45
        ### SPEED GOES FROM 0 TO INFINITE ### DEFAULT 1.6

        self.SetSpeedX( math.sin( math.radians(angle) ) * speed )
        self.SetSpeedY( math.cos( math.radians(angle) ) * speed )
    def SetF             (self,f          ):
        ### F GOES FROM 0 TO 10 --> NOT LINEAL
        ### DEFAULT 6 ###
        if (f == 0):
            self.__friccion = 1
        else:
            potencia = 12 - f
            numero = math.pow(2.0,potencia) * 10
            final  = 1.0 / numero
            self.__friccion = final

        #10 1 / 40
        #9  1 / 80
        #8  1 / 160
        #7  1 / 320
        #6  1 / 640
        #5  1 / 1280
        #4  1 / 2560
        #3  1 / 5120
        #2  1 / 10240
        #1  1 / 20480
        #0  0
    def setWind          (self,value      ):
        ### WIND GOES FROM 0 TO INFINITE ### DEFAULT 0
        self.__wind = value
    def setGravity       (self,gravity    ):
        ### GRAVITY GOES FROM -INFINITE TO +INFINITE ### DEFAULT 1.3
        self.__gravity = gravity

    ### START / STOP FUNCTIONS ###
    def Stop (self):
        self.__start = False
    def Start(self):
        self.__start = True

    def SetX     (self,x    ):
        self.__x = x
    def SetY     (self,y    ):
        self.__y = y
    def GetX     (self      ):
        return self.__x
    def GetY     (self      ):
        return self.__y
    def GetPos   (self      ):
        return [int(self.GetX()),int(self.GetY())]
    def SumX     (self,x    ):
        self.SetX( self.GetX() + x)
    def SumY     (self,y    ):
        self.SetY( self.GetY() + y)
    def GetSpeedX(self      ):
        return self.__speedX
    def GetSpeedY(self      ):
        return self.__speedY
    def SetSpeedX(self,speed):
        self.__speedX = speed
    def SetSpeedY(self,speed):
        self.lastSpeedY = self.__speedY
        self.__speedY = speed
    def SumSpeedX(self,x    ):
        self.SetSpeedX( float(self.GetSpeedX()) + x)
    def SumSpeedY(self,y    ):
        self.SetSpeedY( float(self.GetSpeedY()) + y)
    def MulSpeedX(self,fact ):
        self.SetSpeedX( float(self.GetSpeedX()) * float(fact))
    def MulSpeedY(self,fact ):
        self.SetSpeedY( float(self.GetSpeedY()) * float(fact))
    def IsOnTop  (self      ):
        if (not self.__start):
            return False
        if (self.GetSpeedY() >= 0 and self.lastSpeedY <= 0):
            return True
        return False
    def movingUpdating   (self):
        self.SumX(self.GetSpeedX())
        self.SumY(self.GetSpeedY())

        self.MulSpeedX(self.__friccion)
        self.MulSpeedY(self.__friccion)

        self.SumSpeedX(  self.__wind     )
        self.SumSpeedY(  self.__gravity  )

    def graphic_update  (self,SCREEN):
        SCREEN.blit(self.__surface,(int(self.GetX()-self.__W/2),int(self.GetY()-self.__H/2)))
    def logic_update    (self,Events):
        if (self.__start):
            self.movingUpdating()



