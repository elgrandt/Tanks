__author__ = 'Dylan'
import pygame
import Loaded.Images as img

def CircleBorderRectangle(tam=(0,0),Color=(0,0,0),Radio=0,Transparecy=False, BorderSize = 1, Opacity = 255):
    Surface = pygame.transform.scale(img.Vacio,tam)
    Position = (0,0)
    if Transparecy == False:
        pygame.draw.rect(Surface, Color, (Position[0]+Radio,Position[1],tam[0]-Radio*2,tam[1]))
        pygame.draw.rect(Surface, Color, (Position[0],Position[1]+Radio,tam[0],tam[1]-Radio*2))
        pygame.draw.ellipse(Surface, Color, (Position[0],  Position[1],   Radio*2,   Radio*2))
        pygame.draw.ellipse(Surface, Color, (Position[0]+tam[0]-Radio*2,  Position[1],   Radio*2,   Radio*2))
        pygame.draw.ellipse(Surface, Color, (Position[0],  Position[1]+tam[1]-Radio*2,   Radio*2,   Radio*2))
        pygame.draw.ellipse(Surface, Color, (Position[0]+tam[0]-Radio*2,  Position[1]+tam[1]-Radio*2,   Radio*2,   Radio*2))
    else:
        pi = 3.14159265359
        Radio1 = Radio*2
        pygame.draw.arc(Surface, Color, (Position[0],Position[1],Radio1,Radio1), pi/2, pi,BorderSize)
        pygame.draw.arc(Surface, Color, (Position[0]+tam[0]-Radio1,Position[1],Radio1,Radio1), 0, pi/2,BorderSize)
        pygame.draw.arc(Surface, Color, (Position[0],Position[1]+tam[1]-Radio1,Radio1,Radio1), pi, 1.5*pi,BorderSize)
        pygame.draw.arc(Surface, Color, (Position[0]+tam[0]-Radio1,Position[1]+tam[1]-Radio1,Radio1,Radio1), 1.5*pi, 2*pi,BorderSize)
        pygame.draw.line(Surface, Color, (Position[0]+Radio,Position[1]), (Position[0]+tam[0]-Radio,Position[1]), BorderSize)
        pygame.draw.line(Surface, Color, (Position[0],Position[1]+Radio), (Position[0],Position[1]+tam[1]-Radio), BorderSize)
        pygame.draw.line(Surface, Color, (Position[0]+tam[0]-BorderSize+1,Position[1]+Radio), (Position[0]+tam[0]-BorderSize+1,Position[1]+tam[1]-Radio), BorderSize)
        pygame.draw.line(Surface, Color, (Position[0]+Radio,Position[1]+tam[1]-BorderSize+1), (Position[0]+tam[0]-Radio,Position[1]+tam[1]-BorderSize+1), BorderSize)
    Surface.fill((255,255,255,Opacity),None,pygame.BLEND_RGBA_MULT)
    return Surface