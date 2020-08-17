'''
Created on 05/03/2014

@author: Dylan
'''
import pygame

def Load(Dir):
    try:
        return pygame.image.load("Data/Images/" + Dir)
    except:
        raise NameError, 'ERROR AL CARGAR LA IMAGEN "' + Dir + '"'
def Transform(Img, NewSize):
    return pygame.transform.scale(Img, NewSize)

Vacio = Load("Vacio.png")
MenuBackground = Load("MenuBackground.jpg")
FlechaIzquierda = Load("FlechaIzquierda.png")
FlechaDerecha = Load("FlechaDerecha.png")
FlechaSiguiente = Load("FlechaSiguiente.png")
FlechaSiguienteHover = Load("FlechaSiguienteHover.png")

TanksTitle = Load("TanksImage.png")

Energy = Transform(Load("MenuImages/Energy.png"), (19, 15))
Nafta = Transform(Load("MenuImages/Nafta.png"), (15, 18))
RepairKit = Transform(Load("MenuImages/RepairKit.png"), (17, 17))
Tank = Transform(Load("MenuImages/Tank.png"), (25, 18))
Teleport = Transform(Load("MenuImages/Teleport.png"), (18, 17))
Force = Transform(Load("MenuImages/Force.png"), (30, 70))
Angle = Transform(Load("MenuImages/Angle.png"), (90, 15))

FireActive = Load("MenuImages/FireActive.png")
FireActive = Transform(FireActive, (int(FireActive.get_size()[0] * 1.3), int(FireActive.get_size()[1] * 1.3)))
FireInactive = Load("MenuImages/FireInactive.png")
FireInactive = Transform(FireInactive, (int(FireInactive.get_size()[0] * 1.3), int(FireInactive.get_size()[1] * 1.3)))

Tanks = {"Blue":None, "Green":None, "Grey":None, "Orange":None, "Red":None, "Yellow":None}
Tanks["Red"] = Transform(Load("Tanks/Red.png"), (28, 15))
Tanks["Blue"] = Transform(Load("Tanks/Blue.png"), (28, 15))
Tanks["Grey"] = Transform(Load("Tanks/Grey.png"), (28, 15))
Tanks["Orange"] = Transform(Load("Tanks/Orange.png"), (28, 15))
Tanks["Green"] = Transform(Load("Tanks/Green.png"), (28, 15))
Tanks["Yellow"] = Transform(Load("Tanks/Yellow.png"), (28, 15))

Weapons = [
    {"Title":"Small misile",    "Price":0,   "Count":1,  "Force":15,  "Default":99, "Type":"Clasic"     },
    {"Title":"Misile",          "Price":2,   "Count":10, "Force":20,  "Default":0,  "Type":"Clasic"     },
    {"Title":"Small atom bomb", "Price":5,   "Count":2,  "Force":50,  "Default":0,  "Type":"Clasic"     },
    {"Title":"Atom bomb",       "Price":12,  "Count":1,  "Force":100, "Default":0,  "Type":"Clasic"     },
    {"Title":"Volcano bomb",    "Price":8,   "Count":2,  "Force":20,  "Default":99, "Type":"Volcano"    },
    {"Title":"Shower",          "Price":9,   "Count":2,  "Force":60,  "Default":50,  "Type":"Shower"     },
    {"Title":"Hot shower",      "Price":30,  "Count":1,  "Force":80,  "Default":0,  "Type":"Shower"     },
    {"Title":"Small ball",      "Price":5,   "Count":5,  "Force":80,  "Default":0,  "Type":"Ball"       },
    {"Title":"Ball",            "Price":6,   "Count":2,  "Force":90,  "Default":0,  "Type":"Ball"       },
    {"Title":"Large ball",      "Price":15,  "Count":1,  "Force":100, "Default":0,  "Type":"Ball"       },
    {"Title":"Small ball V2",   "Price":6.5, "Count":5,  "Force":85,  "Default":0,  "Type":"Ball"       },
    {"Title":"Ball V2",         "Price":7.5, "Count":2,  "Force":95,  "Default":0,  "Type":"Ball"       },
    {"Title":"Large ball V2",   "Price":18,  "Count":1,  "Force":105, "Default":0,  "Type":"Ball"       },
    {"Title":"Air strike",      "Price":25,  "Count":1,  "Force":50,  "Default":0,  "Type":"Air strike" }
]

Extras = [
    {"Title":"Parachutes",        "Price":5,  "Count":5,  "Default":8   },
    {"Title":"Repair kit",        "Price":4,  "Count":5,  "Default":8   },
    {"Title":"Fuel",              "Price":3,  "Count":50, "Default":250 },
    {"Title":"Weak shield",       "Price":5,  "Count":2,  "Default":8   },
    {"Title":"Shield",            "Price":10, "Count":1,  "Default":8   },
    {"Title":"Strong shield",     "Price":15, "Count":1,  "Default":8   },
    {"Title":"Super shield",      "Price":20, "Count":1,  "Default":8   },
    {"Title":"Teleport",          "Price":15, "Count":1,  "Default":8   },
    {"Title":"Upgrade energy",    "Price":5,  "Count":1,  "Default":0   },
    {"Title":"Upgrade armor",     "Price":10, "Count":1,  "Default":0   },
    {"Title":"Upgrade engine",    "Price":7,  "Count":1,  "Default":0   },
    {"Title":"Upgrade hill move", "Price":5,  "Count":1,  "Default":0   }
]

Weapons2 = []
for q in range(len(Weapons)):
    Weapons2.append({"ID":q, "Title":Weapons[q]["Title"], "Price":Weapons[q]["Price"], "Count":Weapons[q]["Count"], "Default":Weapons[q]["Default"], "Force":Weapons[q]["Force"], "Type":Weapons[q]["Type"], "Image":Load("Buyable/Weapons/" + str(q) + ".png")})

Extras2 = []
for q in range(len(Extras)):
    Extras2.append({"ID":q, "Title":Extras[q]["Title"], "Price":Extras[q]["Price"], "Count":Extras[q]["Count"], "Default":Extras[q]["Default"], "Image":Load("Buyable/Extras/" + str(q) + ".png")})

Extras = Extras2
Weapons = Weapons2

Wind = Transform(Load("Wind.png"), (80, 20))
FlechaWind = Load("FlechaWind.png")

Explosion = Load("Explosion.png")

TanksBackground = Load("TanksBackground.png")

FlechaMouse = Load("FlechaMouse.png")