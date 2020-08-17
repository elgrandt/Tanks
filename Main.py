'''
Created on 04/03/2014

@author: Dylan
'''
import pygame
import gui.events as events
from Tkinter import Tk
import Loaded
import Menu.StartMenu as SM
import Game
import thread

TkinterTest = Tk()

class Main:
    def __init__(self):
        self.CLOCK      = pygame.time.Clock()
        self.FRECUENCY  = 20
        self.ScreenSize = [800,600]
        self.Screen     = pygame.display.set_mode(self.ScreenSize,pygame.RESIZABLE|pygame.DOUBLEBUF)

        self.Finished      = False
        self.Fullscreen    = False
        self.Events        = events.events()
        self.CurrentsAreas = []
        self.LastSize      = [0,0]
        pygame.display     . set_caption("Tanks")
        
        self.Background = Loaded.Images.MenuBackground
        
        self.CurrentsAreas.append(SM.StartMenu())
        self.StartedLogic = False
        thread.start_new_thread(self.logic_update,())
        thread.start_new_thread(self.graphic_update,())
        self.ThreadsFinished = 0
        while True:
            for E in pygame.event.get():
                if E.type == pygame.QUIT:
                    self.Finished = True
            if self.Finished and self.ThreadsFinished == 2:
                break
    def graphic_update(self):
        while not self.Finished:
            try:
                if self.StartedLogic:
                    pygame.display.update()
                    self.Screen.fill((255,255,255))
                    if self.Background != None:
                        self.Screen.blit(pygame.transform.scale(self.Background,self.ScreenSize),(0,0))
                    for q in range(len(self.CurrentsAreas)):
                        self.CurrentsAreas[q].graphic_update(self.Screen)
                self.CLOCK.tick(30)
            except:
                raise
        self.ThreadsFinished += 1
        thread.exit()
    def logic_update(self):
        while not self.Finished:
            try:
                Commands = []
                ###  FOR IN EVENTS  ###
                for Event in pygame.event.get():
                    if Event.type == pygame.QUIT:
                        Commands.append("Quit")
                    if Event.type == pygame.VIDEORESIZE:
                        self.ScreenSize = Event.dict['size']
                        if self.Fullscreen:
                            self.Screen = pygame.display.set_mode(self.ScreenSize,pygame.RESIZABLE|pygame.FULLSCREEN|pygame.DOUBLEBUF)
                        else:
                            self.Screen = pygame.display.set_mode(self.ScreenSize,pygame.RESIZABLE|pygame.DOUBLEBUF)
                ###  UPDATING SELF.EVENTS  ###
                self.Events.update_keyboard(pygame.key.get_pressed())
                self.Events.update_mouse(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
                ###  SETTING FULLSCREEN  ###
                if self.Events.keyboard[pygame.K_F11]:
                    if not self.Fullscreen:
                        self.Fullscreen = True
                        self.LastSize = [self.ScreenSize[0],self.ScreenSize[1]]
                        self.ScreenSize = TkinterTest.maxsize()
                        self.Screen = pygame.display.set_mode(self.ScreenSize,pygame.RESIZABLE|pygame.FULLSCREEN|pygame.DOUBLEBUF)
                    else:
                        self.Fullscreen = False
                        self.ScreenSize = [self.LastSize[0],self.LastSize[1]]
                        self.Screen = pygame.display.set_mode(self.ScreenSize,pygame.RESIZABLE|pygame.DOUBLEBUF)
                ### UPDATING  ###
                for q in range(len(self.CurrentsAreas)):
                    RetLogic = self.CurrentsAreas[q].logic_update(self.Events)
                    if RetLogic != None:
                        for q in RetLogic:
                            Commands.append(q)
                ###  INTERPRETING COMMANDS  ###
                for q in Commands:
                    self.InterpreteCommands(q)
                ###  CLOCK ###
                self.CLOCK.tick(30)
                self.StartedLogic = True
            except:
                raise
        self.ThreadsFinished += 1
        thread.exit()
    def SetBackground(self,NewBackground):
        self.Background = NewBackground

    def InterpreteCommands(self,Command):
        if Command == "Quit":#Comando para salir
            self.Finished = True
        elif Command == "Restart":#Comando para reiniciar el juego
            Main()
            self.Finished = True
        elif Command["Title"] == "Start game":
            self.CurrentsAreas = []
            self.CurrentsAreas.append(Game.Game.Game(Command["Data"]["Number of players"],Command["Data"]["Terrain type"],Command["Data"]["Players"],self))
        else:
            print Command

Main()
