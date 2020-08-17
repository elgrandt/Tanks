'''
Created on 07/03/2014

@author: Dylan
'''

class MultipleUpdate:
    def __init__(self):
        self.__Clases = []
    def AddClass(self,Class,Name):
        self.__Clases.append({"Class":Class,"Name":Name})
    def DelClass(self,Name):
        for q in range(len(self.__Clases)):
            if self.__Clases[q]["Name"] == Name:
                del self.__Clases[q]
    def GetClassForName(self,Name):
        for q in self.__Clases:
            if q["Name"] == Name:
                return q["Class"]
    def graphic_update(self,Screen):
        for q in self.__Clases:
            q.graphic_update(Screen)
    def logic_update(self,Events):
        for q in self.__Clases:
            q.logic_update(Events)