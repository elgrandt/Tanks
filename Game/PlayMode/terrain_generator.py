__author__ = 'ariel'

import random
import math
import pygame

class NOW:
    UP,  \
    DOWN \
    = range(2)

def joinRanges(A,B):
    for x in range(len(B)):
        A.append(B[x])

def azarNegativo():
    n = random.randrange(2)

    if (n == 1):
        return 1
    else:
        return -1

class cor:
    def __init__(self,position):
        self.__x,self.__y = position
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self,x):
        self.__x = x
    def setY(self,y):
        self.__y
    def sumX(self,x):
        self.setX( self.getX() + x)
    def sumY(self,y):
        self.setY( self.getY() + y)
    def showValues(self):
        print "(",self.__x,",",self.__y,"),"

def show_value(cord):
    print "(",cord[0],",",cord[1],",",cord[2],"),"

class TerrainFactory:
    def __init__(self):
	self.setDimensions((800,600))
        self.setMaxDistanceBetweenTops(400)
        self.setMinDistanceBetweenTops(100)
        self.setMaxTop(600)
        self.setMinTop(200)
        self.setLocalIrregularity(3)
        self.setMaxDistanceBetweenTopsH(100)
        self.setMinDistanceBetweenTopsH(100)
        

    ### SETTING VALUES ###
    def setMaxDistanceBetweenTops (self,distance    ):
        if (distance < 0):
            self.__errorNegativo()
        self.__distanceHBT = distance
    def setMinDistanceBetweenTops (self,distance    ):
        if (distance < 0):
            self.__errorNegativo()
        self.__distanceLBT = distance
    def setMaxTop                 (self,top         ):
        if (top < 0):
            self.__errorNegativo()
        self.__TOP = top
    def setMinTop                 (self,top         ):
        if (top < 0):
            self.__errorNegativo()
        self.__LOW = top
    def setLocalIrregularity      (self,irregularity):
        self.__irregularity = irregularity
    def getLocalIrregularity      (self             ):
        return self.__irregularity
    def setMaxDistanceBetweenTopsH(self,distance    ):
        if (distance < 0):
            self.__errorNegativo()
        self.__distanceHBTH = distance
    def setMinDistanceBetweenTopsH(self,distance    ):
        if (distance < 0):
            self.__errorNegativo()
        self.__distanceLBTH = distance
    def setDimensions             (self,DIMENSIONS  ):
        self.__W , self.__H = DIMENSIONS

    ### ERROR HANDLING ###
    def __errorNegativo  (self):
        raise ValueError,"Error fatal, no puede ser negativo!"
    def __checkeo        (self):
        if (self.__TOP < 0 or self.__LOW < 0 or self.__distanceHBTH < 0 or self.__distanceLBTH < 0 or self.__distanceHBT < 0 or self.__distanceLBT < 0 or self.__irregularity < 0):
            self.__errorNegativo()
        if (self.__TOP < self.__LOW):
            raise ValueError, "El punto minimo no puede ser mayor al maximo!"
        if (self.__distanceHBT < self.__distanceLBT):
            raise ValueError, "La minima distancia de picos no puede ser mayor a la maxima!"
        if (self.__distanceLBTH > self.__distanceHBTH):
            raise ValueError, "La minima distancia en x de picos no puede ser mayor a la maxima!"

    ### SUB-FUNCTION ###
    def __filterInvalid       (self,A    ):
        for x in range(len(A)-1,-1,-1):
            if (A[x] > self.__TOP):
                del A[x]
            elif (A[x] < self.__LOW):
                del A[x]
        return A

    ### MACRO-FUNCTIONS ###
    def __generateTops        (self      ):
        tops = []

        Continue = True
        Starting = True

        altitude = self.__LOW + (self.__TOP-self.__LOW)/2

        position = 0
        current = random.choice([NOW.UP,NOW.DOWN])
        while Continue:
            ###### CREANDO RANGO DE ALTURA #####
            if (current == NOW.DOWN):
                A = range(altitude + self.__distanceLBT, altitude + self.__distanceHBT)
            else:
                A = range(altitude - self.__distanceLBT, altitude - self.__distanceHBT,-1)

            A = self.__filterInvalid(A)

            ##### SORTEANDO RANGO DE ALTURA ####
            if (len(A) == 0):
                altitude = altitude + self.__distanceLBT
            else:
                altitude = random.choice(A)
	
            ##### CREANDO RANGO DE DISTANCIA ####
            if (Starting == True):
                position = 0
                Starting = False
            else:
                R = range(position + self.__distanceLBTH,position + self.__distanceHBTH)
                if (len(R) == 0):
                    A = position + self.__distanceLBTH
                else:
                    A = random.choice(R)

               	position = A
                if (position >= self.__W):
                    Continue = False
            tops.append((position,altitude,current))
            if (current == NOW.UP):
                current = NOW.DOWN
            else:
                current = NOW.UP
        self.__tops = tops
    def __generateRandius     (self      ):
        self.__points = []
        for x in range(len(self.__tops)-1):
            self.__generateUnion(self.__tops[x],self.__tops[x+1])
    def __generateUnion       (self,fr,to):
        current = fr[2]

        Y_to_change =    to[1] - fr[1]
        distanceToFill = to[0] - fr[0]

        if (current == NOW.DOWN):
            angle       = 270.0
            corrimiento = -Y_to_change/2
            sentido = -1

        else:
            angle = 90.0
            corrimiento = -Y_to_change/2
            sentido = 1

        uponAngle = 180.0 / float(distanceToFill)

        for x in range(distanceToFill):

            altitude = math.sin( math.radians(angle) )*(-Y_to_change/2*sentido) - corrimiento + fr[1]
            logitude = x + fr[0]
	    if (int(logitude) > self.__W):
		pass
	    else:
                self.__points.append( [int(logitude),int(altitude)] )

            angle += uponAngle

    def __generateIrregularity(self      ):
        for x in range(len(self.__points)):
            if self.__irregularity != 0:
                self.__points[x][1] += random.randrange(-self.__irregularity,self.__irregularity)
            if (self.__points[x][1] < self.__LOW):
                self.__points[x][1] = self.__LOW
            elif (self.__points[x][1] > self.__TOP):
                self.__points[x][1] = self.__TOP

    ### OUTPUT FUNCTIONS ###

    def generate         (self):
        self.__checkeo()
        self.__generateTops()

        self.__generateRandius()
        self.__generateIrregularity()

    def printTops        (self):
        for x in range(len(self.__tops)):
            show_value(self.__tops[x])
    def getPoints        (self):
	new_points = []
	for x in range(len(self.__points)):
	     new_points.append((self.__points[x][0],self.__H - self.__points[x][1]))
        return new_points
    def getTops          (self):
        return self.__tops

def DrawPoints(surface,points,color):
    for x in range(len(points)):
        DrawPoint(surface,points[x],color)

def DrawPoint(surface,position,color):
    pygame.draw.line(surface,color,(position[0],surface.get_size()[1]),(position[0],surface.get_size()[1]-position[1]))


"""
def main():
    terrain = TerrainFactory()
    terrain.generate()

    surface = pygame.display.set_mode((800,600))
    surface.fill((255,255,255))

    DrawPoints(surface,terrain.getPoints(),(100,200,100))

    pygame.display.update()
    exit = raw_input("Enter")

main()
"""
