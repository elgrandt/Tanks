'''
Created on 10/03/2014

@author: Ariel
'''

import pygame
import math


class AngleLine:
    def __init__(self):
        self.setLineLength(20)
        self.setLineWidth(4)
        self.setCurrentAngle(40)
        self.setColor((0,0,100))
    def setLineLength(self,distance):
        self.line_length = distance
    def setLineWidth (self,width):
        self.line_width = width
    def setCurrentAngle(self,angle):
        self.angle = angle+90
    def setColor(self,color):
        self.color = color
    def getSurface(self):


        surface = pygame.surface.Surface((self.line_length*2,self.line_length*2),pygame.SRCALPHA,32)
        surface.convert_alpha()

        positionX = math.sin( math.radians(self.angle) ) * self.line_length
        positionY = math.cos( math.radians(self.angle) ) * self.line_length

        self.__drawLine(surface,(0,0),(positionX,positionY),self.color,self.line_width)

        return surface

    def blitIn(self,surface,position):
        surface.blit(self.getSurface(),position)
    def blitInCenter(self,surface):
        W,H = surface.get_size()
        new = self.getSurface()
        W2,H2 = new.get_size()
        X = W / 2 - W2 / 2
        Y = H / 2 - H2 / 2
        surface.blit(new,(X,Y))
    def BlitSurfaceIn(self,new):
        W,H = new.get_size()
        surface = self.getSurface()
        W2,H2 = surface.get_size()
        X = W2 / 2 - W / 2
        Y = H2 / 2 - H / 2
        surface.blit(new,(X,Y))
        return surface
        
    def __drawLine(self,surface,start_pos,end_pos,color,width):

        pygame.draw.line(surface,color,(start_pos[0]+self.line_length,start_pos[1]+self.line_length),(end_pos[0]+self.line_length,end_pos[1]+self.line_length),width)