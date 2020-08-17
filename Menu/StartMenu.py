import MenuGenerator
import Loaded
import pygame
import gui.Clasic as Clasic
import PlayerConfiguration

class StartMenu:
    def __init__(self):
        self.Started = False
        #Menu que te pregunta el tipo de terreno y la cantiadad de jugadores
        self.__MenuActual = []
        FirstMenu = MenuGenerator.GenerateMenu(200,(255,255,255),(0,0))
        FirstMenu.AddTitle("TERRAIN TYPE")
        FirstMenu.AddSpace(10)
        FirstMenu.AddRadio("MOUNTAIN")
        FirstMenu.AddSpace(5)
        FirstMenu.AddRadio("FOREST")
        FirstMenu.AddSpace(5)
        FirstMenu.AddRadio("DESERT")
        FirstMenu.AddSpace(5)
        FirstMenu.AddRadio("RANDOM")
        FirstMenu.AddSeparator((0,0,255))
        FirstMenu.AddTitle("PLAYER")
        FirstMenu.AddSpace(10)
        FirstMenu.AddText("Cantidad total de jugadores sean controlados por la computadora o por una persona", 13)
        FirstMenu.AddSpace(5)
        FirstMenu.AddSelect(["2","3","4","5"],"Player select")
        FirstMenu.SetSelectedRadio("RANDOM")
        self.__MenuActual.append([FirstMenu, "Selector of players and terrain"])
        #Menu con los controles
        Controls = MenuGenerator.GenerateMenu(200,(255,255,255),(0,0))
        Controls.AddTitle("CONTROLS")
        Controls.AddSeparator((0,0,255))
        Controls.AddText("LEFT & RIGHT ARROW MOVE", 15)
        Controls.AddSpace(17)
        Controls.AddText("UP & DOWN ARROW CANNON ROTATION", 15)
        Controls.AddSpace(17)
        Controls.AddText("PGUP & PGON FIRE POWER",15)
        Controls.AddSpace(17)
        Controls.AddText('"Q" & "W" CHANGE WEAPON',15)
        Controls.AddSpace(17)
        Controls.AddText("SPACE FIRE",15)
        self.__MenuActual.append([Controls,"Controls"])
        #Algunas declaraciones de variables
        self.FlechaContinue = pygame.transform.scale(Loaded.Images.FlechaSiguiente,(60,50))
        self.Title = pygame.transform.scale(Loaded.Images.TanksTitle,(500,150))
        self.PositionFlechaContinue = [0,0]
        self.MenuSeleccionado = "Primer menu"
        self.LT = pygame.time.get_ticks()
        self.Data = {"Terrain type":None,"Number of players":None,"Players":[]}
        self.ActualPlayer = 1
        self.Started = True
    def GetMenuForName(self,Name):
        for q in self.__MenuActual:
            if q[1] == Name:
                return q[0]
    def graphic_update(self,Screen):
        if self.Started:
            self.PositionNames = [200,20+self.Title.get_size()[1]+70]
            self.PositionFlechaContinue = (Screen.get_size()[0]-self.FlechaContinue.get_size()[0]-10,Screen.get_size()[1]-self.FlechaContinue.get_size()[1]-5)
            Screen.blit(self.FlechaContinue,self.PositionFlechaContinue)
            Screen.blit(self.Title,(50,20))
            if self.MenuSeleccionado == "Primer menu":
                PosMenu1 = [100,20+self.Title.get_size()[1]+70]
                self.GetMenuForName("Selector of players and terrain").UpdatePosition(PosMenu1)
                self.GetMenuForName("Controls").UpdatePosition([PosMenu1[0]+200+50,PosMenu1[1]])
            FirstMenuAct = self.__MenuActual
            for q in range(len(self.__MenuActual)):
                if self.__MenuActual == FirstMenuAct:
                    self.__MenuActual[q][0].graphic_update(Screen)
    def logic_update(self,Events):
        for q in range(len(self.__MenuActual)):
            self.__MenuActual[q][0].logic_update(Events)
        if Clasic.GetFocused(Events, self.PositionFlechaContinue, self.FlechaContinue.get_size()):
            self.FlechaContinue = pygame.transform.scale(Loaded.Images.FlechaSiguienteHover,(60,50))
            if Events.mouse.get_now_pressed()[0]:
                if pygame.time.get_ticks() > self.LT + 200:
                    self.LT = pygame.time.get_ticks()
                    if self.MenuSeleccionado == "Primer menu":
                        TerrainType = self.GetMenuForName("Selector of players and terrain").GetSelectedRadio()
                        NumberOfPlayers = self.GetMenuForName("Selector of players and terrain").GetSelectedSelect("Player select")
                        self.Data["Terrain type"] = TerrainType
                        self.Data["Number of players"] = int(NumberOfPlayers)
                        self.MenuSeleccionado = "Selector de nombres"
                        self.__MenuActual = [[PlayerConfiguration.PlayerConfiguration(self.ActualPlayer,self.PositionNames),"Player "+str(self.ActualPlayer)]]
                    elif self.MenuSeleccionado == "Selector de nombres":
                        NewData = self.GetMenuForName("Player "+str(self.ActualPlayer)).GetData()
                        if NewData != False:
                            self.Data["Players"].append(NewData)
                            if self.ActualPlayer < self.Data["Number of players"]:
                                self.ActualPlayer += 1
                                self.__MenuActual = [[PlayerConfiguration.PlayerConfiguration(self.ActualPlayer,self.PositionNames),"Player "+str(self.ActualPlayer)]]
                            else:
                                self.__MenuActual = []
                                self.MenuSeleccionado = ""
                                return [{"Title":"Start game","Data":self.Data}]
        else:
            self.FlechaContinue = pygame.transform.scale(Loaded.Images.FlechaSiguiente,(60,50))