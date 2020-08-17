'''
Created on 14/03/2014

@author: Dylan
'''

def BasicColition(Obj1,Obj2):
    return Obj1["Pos"][0]+Obj1["Size"][0] > Obj2["Pos"][0] and Obj1["Pos"][0] < Obj2["Pos"][0]+Obj2["Size"][0] and Obj1["Pos"][1]+Obj1["Size"][1] > Obj2["Pos"][1] and Obj1["Pos"][1] < Obj2["Pos"][1]+Obj2["Size"][1]