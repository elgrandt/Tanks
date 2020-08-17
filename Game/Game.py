'''
Created on 08/03/2014

@author: Dylan
'''
import PlayMode
import random
import Loaded.Images as img
import pygame

class Game:
    def __init__(self,PlayerNumber,TerrainType,PlayersData,Main):
        self.Main = Main
        self.PlayerNumber = PlayerNumber
        self.TerrainType = TerrainType
        if self.TerrainType == "RANDOM":
            Rand = random.randrange(2)
            if Rand == 0:
                self.TerrainType = "MOUNTAIN"
            elif Rand == 1:
                self.TerrainType = "FOREST"
            else:
                self.TerrainType = "DESERT"
        self.PlayersData = PlayersData
        NewPlayerData = []
        for w in range(len(self.PlayersData)):
            q = self.PlayersData[w]
            NewPlayerData.append({"ID":q["ID"],"Name":q["Name"],"Color":q["Color"],"Energy":100,"Actual fuel":250,"Money":0,"Xposition":random.randrange(800),"Img":None,"Angle":0,"Position":[0,0],"Weapons":[],"Selected weapon":0})
            for q in img.Weapons:
                NewPlayerData[w]["Weapons"].append({"ID":q["ID"],"Title":q["Title"],"Actual count":q["Default"],"Image":q["Image"],"Force":q["Force"],"Type":q["Type"]})
            for q in img.Extras:
                for w in range(len(NewPlayerData)):
                    NewPlayerData[w][q["Title"]] = q["Default"]
            for q in range(len(NewPlayerData)):
                NewPlayerData[q]["Energy"] += int(NewPlayerData[q]["Upgrade energy"]*10)
        self.PlayersData = NewPlayerData
        self.StartGame()
    def StartGame(self):
        for q in range(len(self.PlayersData)):
            self.PlayersData[q]["Energy"] = 100+10*self.PlayersData[q]["Upgrade energy"]
            self.PlayersData[q]["Actual fuel"] = self.PlayersData[q]["Fuel"]
        self.ActualUpdating = PlayMode.PlayMode.Play(self.PlayerNumber,self.TerrainType,self.PlayersData,self)
        NewBackground = pygame.Surface((100,100))
        NewBackground.fill((78,179,251))
        self.Main.SetBackground(NewBackground)
        self.ActualState = "GAME"
    def StartShop(self):
        self.ActualUpdating = PlayMode.Shop.Shop(self.PlayersData)
        NewBackground = img.TanksBackground
        self.Main.SetBackground(NewBackground)
        self.ActualState = "SHOP"
    def graphic_update(self,Screen):
        if self.ActualUpdating != None:
            self.ActualUpdating.graphic_update(Screen)
    def logic_update(self,Events):
        if self.ActualUpdating != None:
            self.ActualUpdating.logic_update(Events)
            if self.ActualUpdating.GetFinished():
                if self.ActualState == "GAME":
                    self.StartShop()
                elif self.ActualState == "SHOP":
                    self.StartGame()