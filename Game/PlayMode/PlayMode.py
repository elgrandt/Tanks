'''
Created on 08/03/2014

@author: Dylan
'''
import pygame
import terrain_generator
import Loaded.Images as img
import DataMenu
import TankGenerator

class Play:
    def __init__(self,CantOfPlayers,TerrainType,PlayersData,Game):
        self.__CantOfPlayers = CantOfPlayers
        self.__TerrainType = TerrainType
        self.__PlayersData = PlayersData
        self.__Game = Game
        self.MaxRange = 5
        self.TerrainGenerator = terrain_generator.TerrainFactory()
        self.handleTerrain()
        self.TerrainGenerator.setLocalIrregularity(0)
        self.TerrainGenerator.generate()
        self.Points = self.TerrainGenerator.getPoints()
        self.PlayerAct = 0
        for q in range(len(self.Points)):
            self.Points[q] = [int(self.Points[q][0]),int(self.Points[q][1])]
        self.DataMenu = DataMenu.DataMenu()
        self.DataMenu.SetPoints(self.Points)
        self.DataMenu.SetPlayers(self.__PlayersData)
        self.DataMenu.UpdateData()
        self.TankGenerator = TankGenerator.AngleLine()
        self.__Finished = False
    def GetFinished   (self):
        return self.__Finished
    def handleTerrain (self):
        if self.__TerrainType == "MOUNTAIN":
            self.setMountainType()
        elif self.__TerrainType == "FOREST":
            self.setForestType()
        elif self.__TerrainType == "DESERT":
            self.setDesertType()
    def setMountainType(self):
        self.__Color = (255,255,255)
        self.TerrainGenerator.setDimensions((800,600))
        self.TerrainGenerator.setMaxDistanceBetweenTops(400)
        self.TerrainGenerator.setMinDistanceBetweenTops(100)
        self.TerrainGenerator.setMaxDistanceBetweenTopsH(200)
        self.TerrainGenerator.setMinDistanceBetweenTopsH(100)
        self.TerrainGenerator.setMaxTop(300)
        self.TerrainGenerator.setMinTop(100)
    def setForestType  (self):
        self.__Color = (145,227,63)
        self.TerrainGenerator.setDimensions((800,600))
        self.TerrainGenerator.setMaxDistanceBetweenTops(300)
        self.TerrainGenerator.setMinDistanceBetweenTops(100)
        self.TerrainGenerator.setMaxDistanceBetweenTopsH(200)
        self.TerrainGenerator.setMinDistanceBetweenTopsH(100)
        self.TerrainGenerator.setMaxTop(300)
        self.TerrainGenerator.setMinTop(100)
    def setDesertType  (self):
        self.__Color = (245,230,169)
        self.TerrainGenerator.setDimensions((800,600))
        self.TerrainGenerator.setMaxDistanceBetweenTops(30)
        self.TerrainGenerator.setMinDistanceBetweenTops(10)
        self.TerrainGenerator.setMaxDistanceBetweenTopsH(400)
        self.TerrainGenerator.setMinDistanceBetweenTopsH(100)
        self.TerrainGenerator.setMaxTop(100)
        self.TerrainGenerator.setMinTop(40)
        self.TerrainGenerator.setLocalIrregularity(1)

    def graphic_update(self,Screen):
        self.TankGenerator.setLineLength(img.Tanks["Red"].get_size()[0]/2+3)
        for Pos in self.Points:
            if Pos[1] < Screen.get_size()[1]:
                SurfaceAct = pygame.Surface((1,Screen.get_size()[1]-Pos[1]))
                SurfaceAct.fill(self.__Color)
                Screen.blit(SurfaceAct,Pos)
        ####################################
        for q in range(len(self.__PlayersData)):
            self.TankGenerator.setCurrentAngle(180-self.__PlayersData[q]["Angle"])
            self.__PlayersData[q]["Img"] = img.Tanks[self.__PlayersData[q]["Color"]]
            self.__PlayersData[q]["Img"] = self.TankGenerator.BlitSurfaceIn(self.__PlayersData[q]["Img"])
            Position = [0,0]
            for w in self.Points:
                if w[0] == self.__PlayersData[q]["Xposition"]:
                    Position = [w[0]-self.__PlayersData[q]["Img"].get_size()[0]/2,w[1]-self.__PlayersData[q]["Img"].get_size()[1]/2]
            if Position[1] < Screen.get_size()[1]:
                self.__PlayersData[q]["Position"] = [Position[0],Position[1]]
                Screen.blit(self.__PlayersData[q]["Img"],Position)
            else:
                self.__Finished = True
            if self.__PlayersData[q]["Energy"] <= 0:
                self.__Finished = True
        ####################################
        #Surface = pygame.transform.scale(Surface,Screen.get_size())
        self.DataMenu.graphic_update(Screen)
        #Screen.blit(Surface,(0,0))
    def logic_update(self,Events):
        self.DataMenu.logic_update(Events)
