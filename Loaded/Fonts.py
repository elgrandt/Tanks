'''
Created on 05/03/2014

@author: Dylan
'''
import pygame

pygame.font.init()
Ruta = "Data/Fonts/"

def ClassicFont(Size):
    global Ruta
    return pygame.font.Font(Ruta+"Ubuntu-B.ttf",Size)