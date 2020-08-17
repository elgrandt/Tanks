'''
Created on 07/03/2014

@author: Dylan
'''
import pygame
from MenuGenerator import GenerateMenu

class PlayerConfiguration(GenerateMenu):
    def __init__(self,PlayerAct,Position):
        self.__PlayerAct = PlayerAct
        self.__Player = PlayerAct
        GenerateMenu.__init__(self,350,(255,255,255),Position)
        self.AddTitle("PLAYER "+str(PlayerAct))
        self.AddSeparator((0,0,255))
        self.AddInput("NAME","Name of player")
        self.AddSeparator((0,0,255))
        self.Colors = [
        {"Title":"Red","Color":(255,86,86)},
        {"Title":"Green","Color":(131,247,133)},
        {"Title":"Blue","Color":(120,147,255)},
        {"Title":"Grey","Color":(87,90,100)},
        {"Title":"Yellow","Color":(254,255,108)},
        {"Title":"Orange","Color":(255,198,83)},
        ]
        self.AddLineOfRadios("COLOR", self.Colors)
    def GetData(self):
        NameOfPlayer = self.GetInputWritten("Name of player")
        SelectedColor = self.GetSelectedLineOfRadios("COLOR")
        #if NameOfPlayer != "":
        return {"Name":NameOfPlayer,"Color":SelectedColor,"ID":self.__PlayerAct-1}
        #else:
        #    return False