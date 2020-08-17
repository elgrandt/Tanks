'''
Created on 09/03/2014

@author: Dylan, trigonometric Ariel
'''
import pygame
import Loaded.Images as img
import Loaded.Fonts as Fonts
import gui
import TankGenerator
import Shoot
import random
import math


### SI QUERES OBTENER UN VALOR DEL JUGADOR ACTUAL PODES USAR LA VARIABLE LOCAL PRIVADA DE ESTA CLASE PERO SI QUERES OBTENER UN VALOR LO VAS A TENER QUE MODIFICAR DE LA VARIABLE self.__Players  ###
class DataMenu:
    def __init__(self):
        #  Values
        self.__Name = ""
        self.__Nafta = 0
        self.__Energy = 0
        self.__RepairKit = 0
        self.__Teleport = 0
        self.__Money = 0
        self.__Force = 100
        self.__Angle = 0
        self.__PlayerColor = "Blue"
        self.__Weapons = []
        self.__WeaponsSurfaces = []
        self.__WeaponsSurfaceSize = [0,0]
        self.__Engine = 0
        self.__ID = 0
        self.__Xposition = 0
        self.__Wind = random.randrange(100)
        self.__WindDir = 1
        self.__Points = []
        self.__Players = []
        
        #  Images
        self.ImageName = img.Tank
        self.ImageNafta = img.Nafta
        self.ImageEnergy = img.Energy
        self.ImageRepairKit = img.RepairKit
        self.ImageTeleport = img.Teleport
        self.ImageForce = img.Force
        self.ImageAngle = img.Angle
        self.ImageTankMobile = TankGenerator.AngleLine()
        self.ImageFire = {"Hover":img.FireActive,"Not Hover":img.FireInactive}
        self.ImageWind = img.Wind
        self.ImageFlechaWind = img.FlechaWind
        self.ImageExplosion = img.Explosion
        self.ImageFlechaMouse = img.FlechaMouse
        self.OriginalImageWind = img.Wind
        
        #  Position declarations
        
        self.PosImageRepair = [0,0]
        
        #  Other variables
        self.ScreenSize = [800,600]
        self.FireHoverState = "Not Hover"
        self.FT = True
        self.MovingForcePoint = False
        self.MovingAnglePoint = False
        self.__TankImage = img.Tanks[self.__PlayerColor]
        self.WeaponSelectActive = 0
        self.PosWeaponFlechas = None
        self.Shooting = False
        self.ShootClass = None
        self.Exploiting = False
        self.ExploitingData = []
        self.Events = None
        self.PlayerAct = 0
        self.VolcanoExplosion = False
        self.VolcanoBombs = []
        self.RecienPuesto = 0
        self.Teleporting = False
        self.PosFlechaMouse = [0,0]
        self.FlechaMouseActive = False
        self.BallExplosion = False
        self.SelectingAirStrike = False
        self.MultipleBalls = []
        self.MultipleShooting = False
    def UpdateData(self):
        PlayerData = self.__Players[self.PlayerAct]
        self.__ID = PlayerData["ID"]
        self.__Name = PlayerData["Name"]
        self.__Nafta = PlayerData["Actual fuel"]
        self.__Energy = PlayerData["Energy"]
        self.__RepairKit = PlayerData["Repair kit"]
        self.__Teleport = PlayerData["Teleport"]
        self.__Money = PlayerData["Money"]
        self.__PlayerColor = PlayerData["Color"]
        if self.__Weapons != PlayerData["Weapons"]:
            self.__Weapons = PlayerData["Weapons"]
            self.GenerateWeapons()
        self.__Engine = PlayerData["Upgrade engine"]
        self.__Xposition = PlayerData["Xposition"]
        self.__Angle = PlayerData["Angle"]
        self.__Color = (190,222,244)
        self.__TankImage = img.Tanks[self.__PlayerColor]
        
        self.UpdateSurface()
    def SetPoints(self,Points):
        self.__Points = Points
    def SetPlayers(self,Players):
        self.__Players = Players
    def Render(self,Text):
        Font = Fonts.ClassicFont(18)
        return Font.render(str(Text),1,(0,0,0))
    def GetMid(self,Img,Rend):
        return Img.get_size()[1]/2-self.Rendered[Rend].get_size()[1]/2
    def GetPoints(self):
        return self.__Points
    def GetPlayerAct(self):
        return self.PlayerAct
    def GetColition(self,Point,ObjectsPos):
        Y = 0
        for q in range(len(ObjectsPos)):
            if ObjectsPos[q][0] == int(Point.GetX()):
                Y = ObjectsPos[q][1]
        if Y != 0:
            if int(Point.GetY()) > Y:
                return True
        return False
    def GetPoint(self,Point):
        for q in range(len(self.__Points)):
            if self.__Points[q][0] == Point:
                return q
        return False
    def GenerateWeapons(self):
        ###  GENERATING SIZE OF SURFACE  ###
        
        self.__WeaponsSurfaceSize = [0,30]
        for q in range(len(self.__Weapons)):
            TestRender = self.Render(self.__Weapons[q]["Title"]).get_size()[0]
            if TestRender > self.__WeaponsSurfaceSize[0]:
                self.__WeaponsSurfaceSize[0] = TestRender
        self.__WeaponsSurfaceSize[0] += 2*self.__WeaponsSurfaceSize[1]
        
        ###  GENERATING ALL SURFACES  ###
        
        self.__WeaponsSurfaces = []
        for q in range(len(self.__Weapons)):
            Surface = pygame.Surface(self.__WeaponsSurfaceSize)
            #   El Surface que contiene la imagen
            ImgSurface = pygame.Surface((self.__WeaponsSurfaceSize[1],self.__WeaponsSurfaceSize[1]))
            ImgSurface.fill((198,198,198))
            gui.add_border.add_border(ImgSurface, (0,0,0), 2, 2, 2, 2)
            ImgSurface = gui.Clasic.BlitCenter(ImgSurface, self.__Weapons[q]["Image"])
            PosImgSurface = [0,0]
            #   El Surface que contiene el titulo
            TitleSurface = pygame.Surface([self.__WeaponsSurfaceSize[0]-2*self.__WeaponsSurfaceSize[1],self.__WeaponsSurfaceSize[1]])
            TitleSurface.fill((255,255,255))
            gui.add_border.add_border(TitleSurface, (0,0,0), 2, 0, 0, 2)
            Render = self.Render(self.__Weapons[q]["Title"])
            TitleSurface = gui.Clasic.BlitCenter(TitleSurface, Render)
            PosTitleSurface = [PosImgSurface[0]+ImgSurface.get_size()[0],PosImgSurface[1]]
            #   El Surface que contiene la cantidad actual que tiene de esta arma
            CantSurface = pygame.Surface([self.__WeaponsSurfaceSize[1],self.__WeaponsSurfaceSize[1]])
            CantSurface.fill((198,198,198))
            gui.add_border.add_border(CantSurface, (0,0,0), 2, 2, 2, 2)
            Render2 = self.Render(self.__Weapons[q]["Actual count"])
            CantSurface = gui.Clasic.BlitCenter(CantSurface, Render2)
            PosCantSurface = [PosTitleSurface[0]+TitleSurface.get_size()[0],PosTitleSurface[1]]
            #   Bliting to surface
            Surface.blit(ImgSurface,PosImgSurface)
            Surface.blit(TitleSurface,PosTitleSurface)
            Surface.blit(CantSurface,PosCantSurface)
            self.__WeaponsSurfaces.append(Surface)
    def GenerateWeaponSelector(self,Data):

        ###  BLITTING ACTUAL WEAPON SURFACE AND THE 2 ARROWS  ###
        
        SelectedSurface = self.__WeaponsSurfaces[self.WeaponSelectActive]
        self.FlechaIzquierda = img.Transform(img.FlechaIzquierda,[self.__WeaponsSurfaceSize[1]-2,self.__WeaponsSurfaceSize[1]-2])
        self.FlechaDerecha = img.Transform(img.FlechaDerecha,[self.__WeaponsSurfaceSize[1]-2,self.__WeaponsSurfaceSize[1]-2])
        GlobalSurface = pygame.transform.scale(img.Vacio,(self.FlechaIzquierda.get_size()[0]+self.FlechaDerecha.get_size()[0]+SelectedSurface.get_size()[0]+10,SelectedSurface.get_size()[1]))
        PosFlechaIzquierda = (0,gui.Clasic.GetCenterPosition(GlobalSurface, self.FlechaIzquierda)[1])
        PosFlechaDerecha = (GlobalSurface.get_size()[0]-self.FlechaDerecha.get_size()[0],gui.Clasic.GetCenterPosition(GlobalSurface, self.FlechaDerecha)[1])
        PosSurface = (self.FlechaIzquierda.get_size()[0]+5,0)
        GlobalSurface.blit(self.FlechaIzquierda,PosFlechaIzquierda)
        GlobalSurface.blit(SelectedSurface,PosSurface)
        GlobalSurface.blit(self.FlechaDerecha,PosFlechaDerecha)
        self.PosWeaponFlechas = [PosFlechaIzquierda,PosFlechaDerecha]
        return GlobalSurface
    def ChangePlayer(self):
        for q in range(len(self.__Players)):
            if self.__Players[q]["ID"] == self.__ID:
                if q < len(self.__Players)-1:
                    NewPlayer = q+1
                else:
                    NewPlayer = 0
        self.PlayerAct = NewPlayer
        self.UpdateData()
        if self.__Energy < 100:
            self.__Force = self.__Energy
        else:
            self.__Force = 100
        Rand = random.randrange(2)
        if Rand == 0:
            self.__WindDir = 1
        elif Rand == 1:
            self.__WindDir = -1
        self.__Wind = random.randrange(0,100)
        self.WeaponSelectActive = self.__Players[self.PlayerAct]["Selected weapon"]
    def DestroyTerrain(self,PosExplosion,RangeOfExplosion):
        #  Exploding
        for x in range(PosExplosion[0]-RangeOfExplosion[0],PosExplosion[0]+RangeOfExplosion[0]):
            if (x < len(self.__Points) and x > 0):
                value = float(x - float(PosExplosion[0])) / float(RangeOfExplosion[0])
                a = math.asin(value)

                y = math.cos(a) * RangeOfExplosion[0] + self.__Points[x][1]
                if (self.__Points[x][1] < y):
                    self.__Points[x][1] = y
    def ModifyPlayersAfterExplode(self,PosExplosion,ExploitingData):
        #  Getting the minor disference with the more cercain player
        MenosDisferencia = 100000
        for q in range(len(self.__Players)):
            Disferencia = abs(PosExplosion[0] - self.__Players[q]["Xposition"])
            if Disferencia < MenosDisferencia:
                if q != self.PlayerAct:
                    MenosDisferencia = Disferencia
            #  Removing energy to players inside the range
            if Disferencia < ExploitingData["Max size"][0]/2:
                self.__Players[q]["Energy"] -= ExploitingData["Max size"][0]/2-Disferencia
        #  Giving money to the shooter, if is the last explosion we give more money
        if ExploitingData["Last explosion"]:
            self.__Players[self.PlayerAct]["Money"] += int((8000-MenosDisferencia*10)/2)
        else:
            self.__Players[self.PlayerAct]["Money"] += int((8000-MenosDisferencia*10)/6)
    def ExplodeClassic(self,WeaponAct):
        #  This type only explode
        self.Exploiting = True
        self.ExploitingData = [{"Pos explosion":(int(self.ShootClass.GetX()),int(self.ShootClass.GetY())),"Actual size":[0,0],"Max size":[WeaponAct["Force"],WeaponAct["Force"]],"Last explosion":True}]
        self.ShootClass.Stop()
        self.Shooting = False
        self.ShootClass = None
    def ExplodeVolcano(self,WeaponAct):
        #  This type generate 4 more bombs
        self.VolcanoExplosion = True
        self.VolcanoBombs = []
        for q in range(4):
            BombAct = self.GenerateShoot(random.randrange(45,135), 10, float(self.__Wind)/1000.0*self.__WindDir, self.ShootClass.GetX(), self.ShootClass.GetY())
            self.VolcanoBombs.append(BombAct)
        self.Exploiting = True
        self.ExploitingData = [{"Pos explosion":self.ShootClass.GetPos(),"Actual size":[0,0],"Max size":[WeaponAct["Force"],WeaponAct["Force"]],"Last explosion":False}]
        self.ShootClass.Stop()
        self.Shooting = False
        self.ShootClass = None
        self.RecienPuesto = 5
    def ExplodeBall(self):
        PosBall = self.ShootClass.GetPos()
        if self.__Points[self.GetPoint(PosBall[0])][1] < self.__Points[self.GetPoint(PosBall[0]-1)][1]:
            self.BallExplosion = "Izq"
        else:
            self.BallExplosion = "Der"
        self.ShootClass.Stop()
    def ExplodeShower(self,WeaponAct):
        self.ExplodeClassic(WeaponAct)
    def ExplodeSimpleVolcano(self,ActualBomb):
        WeaponAct = self.__Weapons[self.WeaponSelectActive]
        Last = False
        if len(self.VolcanoBombs) == 1:
            Last = True
        self.Exploiting = True
        self.ExploitingData = [{"Pos explosion":[int(ActualBomb.GetX()),int(ActualBomb.GetY())],"Actual size":[0,0],"Max size":[WeaponAct["Force"],WeaponAct["Force"]],"Last explosion":Last}]
    def ExplodeCrashedBall(self):
        self.BallExplosion = False
        self.Exploiting = True
        WeaponAct = self.__Weapons[self.WeaponSelectActive]
        self.ExploitingData = [{"Pos explosion":[int(self.ShootClass.GetX()),int(self.ShootClass.GetY())],"Actual size":[0,0],"Max size":[WeaponAct["Force"],WeaponAct["Force"]],"Last explosion":True}]
        self.Shooting = False
        self.ShootClass = None
        self.RecienPuesto = 5
    def EplodeMultipleBall(self,ActualBall):
        ActPos = [int(self.MultipleBalls[ActualBall].GetX()),int(self.MultipleBalls[ActualBall].GetY())]
        ActForce = self.__Weapons[self.WeaponSelectActive]["Force"]
        if len(self.MultipleBalls) > 1:
            Last = False
        else:
            Last = True
            self.MultipleShooting = False
        self.ExploitingData.append({"Pos explosion":ActPos,"Actual size":[0,0],"Max size":[ActForce,ActForce],"Last explosion":Last})
        self.Exploiting = True
        del self.MultipleBalls[ActualBall]
    def StopClasic(self,WeaponAct):
        #  If the bomb is out of the mountain, the bomb disapear
        self.ShootClass.Stop()
        self.Shooting = False
        self.ShootClass = None
    def StopVolcano(self,WeaponAct):
        self.StopClasic(WeaponAct)
    def StopBall(self,WeaponAct):
        self.StopClasic(WeaponAct)
    def StopShower(self,WeaponAct):
        self.StopClasic(WeaponAct)
    def StopCrashedBall(self,WeaponAct):
        self.StopClasic(WeaponAct)
    def StopMultipleBall(self,ActualBall):
        if len(self.MultipleBalls) > 1:
            pass
        else:
            self.MultipleShooting = False
        del self.MultipleBalls[ActualBall]
    def GetColitionWithPlayer(self,ShootX,ShootY,WithActualPlayer):
        Colitionated = []
        for q in self.__Players:
            Col = gui.ColitionDetection.BasicColition({"Pos":[ShootX,ShootY],"Size":[4,4]}, {"Pos":q["Position"],"Size":q["Img"].get_size()})
            if Col:
                if q["ID"] != self.__ID or WithActualPlayer:
                    Colitionated.append(q)
        return Colitionated
    def GenerateShoot(self,Angle,Force,Wind,X,Y):
        ShootAct = Shoot.Shoot()
        ShootAct.SetAngleDirection(270-Angle, Force)
        ShootAct.setCircleSurface(2, (0,0,0))
        ShootAct.setWind(Wind)
        ShootAct.SetX(X)
        ShootAct.SetY(Y)
        ShootAct.Start()
        return ShootAct
    def ChangeWeapon(self,Direction):
        if Direction == "Right":
            if self.WeaponSelectActive > 0:
                self.WeaponSelectActive -= 1
            else:
                self.WeaponSelectActive = len(self.__Weapons)-1
            while self.__Weapons[self.WeaponSelectActive]["Actual count"] == 0:
                if self.WeaponSelectActive > 0:
                    self.WeaponSelectActive -= 1
                else:
                    self.WeaponSelectActive = len(self.__Weapons)-1
        elif Direction == "Left":
            if self.WeaponSelectActive < len(self.__Weapons)-1:
                self.WeaponSelectActive += 1
            else:
                self.WeaponSelectActive = 0
            while self.__Weapons[self.WeaponSelectActive]["Actual count"] == 0:
                if self.WeaponSelectActive < len(self.__Weapons)-1:
                    self.WeaponSelectActive += 1
                else:
                    self.WeaponSelectActive = 0
        self.__Players[self.PlayerAct]["Selected weapon"] = self.WeaponSelectActive
    def UpdateShoot(self,ActualShoot,WeaponAct,DiscountWeapons = True):
        #  Generating all surfaces who are colitionated with the bomb
        Colitionated = self.GetColitionWithPlayer(ActualShoot.GetX(), ActualShoot.GetY(), False)
        #  If bomb are inside the screen
        if ActualShoot.GetX() > 0 and ActualShoot.GetX() < 800 and ActualShoot.GetY() > 0 and ActualShoot.GetY() < 800:
            #  If bomb are colitionated with some part of the mountain
            if self.GetColition(ActualShoot,self.__Points) or len(Colitionated) > 0:
                #  Removing weapon
                if DiscountWeapons:
                    self.__Weapons[self.WeaponSelectActive]["Actual count"] -= 1
                #  Generating action of actual type of bomb
                if WeaponAct["Type"] == "Clasic":
                    self.ExplodeClassic(WeaponAct)
                elif WeaponAct["Type"] == "Volcano":
                    self.ExplodeVolcano(WeaponAct)
                elif WeaponAct["Type"] == "Ball":
                    self.ExplodeBall()
                elif WeaponAct["Type"] == "Shower":
                    self.ExplodeShower(WeaponAct)
                elif WeaponAct["Type"] == "Simple volcano":
                    self.ExplodeSimpleVolcano(ActualShoot)
                elif WeaponAct["Type"] == "Crashed ball":
                    self.ExplodeCrashedBall()
                elif WeaponAct["Type"][:len("Multiple ball")] == "Multiple ball":
                    ActualBall = int(WeaponAct["Type"][len("Multiple ball")+1:])
                    self.EplodeMultipleBall(ActualBall)
                return "Crashed"
        else:
            #  Removing weapon
            if DiscountWeapons:
                self.__Weapons[self.WeaponSelectActive]["Actual count"] -= 1
            if WeaponAct["Type"] =="Clasic":
                self.StopClasic(WeaponAct)
            elif WeaponAct["Type"] == "Volcano":
                self.StopVolcano(WeaponAct)
            elif WeaponAct["Type"] == "Ball":
                self.StopBall(WeaponAct)
            elif WeaponAct["Type"] == "Shower":
                self.StopShower(WeaponAct)
            elif WeaponAct["Type"] == "Crashed ball":
                self.StopCrashedBall(WeaponAct)
            elif WeaponAct["Type"][:len("Multiple ball")] == "Multiple ball":
                ActualBall = int(WeaponAct["Type"][len("Multiple ball")+1:])
                self.StopMultipleBall(ActualBall)
            return "Out Of Screen"
    def UpdateExplosions(self):
        ChangePlayer = False
        
        ###  SHOOTING INFO  ###
        
        if self.Shooting:
            PassTheRest = False
            if self.__Weapons[self.WeaponSelectActive]["Type"] == "Shower":
                if self.ShootClass.IsOnTop():
                    self.__Weapons[self.WeaponSelectActive]["Actual count"] -= 1
                    self.MultipleShooting = True
                    if self.__Angle < 90:
                        Angle = 0
                        Dir = 1
                    else:
                        Angle = 180
                        Dir = -1
                    self.MultipleBalls = []
                    for q in range(5):
                        ShootAct = self.GenerateShoot(Angle, 8, float(self.__Wind)/1000.0*self.__WindDir, self.ShootClass.GetX(), self.ShootClass.GetY())
                        self.MultipleBalls.append(ShootAct)
                        Angle -= 10 * Dir
                    PassTheRest = True
                    self.StopShower(self.__Weapons[self.WeaponSelectActive])
            if not PassTheRest:
                ActionShoot = self.UpdateShoot(self.ShootClass,self.__Weapons[self.WeaponSelectActive])
                if ActionShoot == "Out Of Screen":
                    ChangePlayer = True
        
        ###  MULTIPLE SHOOTING  ###
        
        if self.MultipleShooting:
            for q in range(len(self.MultipleBalls)):
                ActionShoot = self.UpdateShoot(self.MultipleBalls[q], {"Type":"Multiple ball "+str(q)}, False)
                if ActionShoot == "Crashed" or ActionShoot == "Out Of Screen":
                    if ActionShoot == "Out Of Screen" and len(self.MultipleBalls) == 0:
                        ChangePlayer = True
                    break
        
        ###  VOLCANO EXPLOSION  ###
        
        if self.VolcanoExplosion:
            if self.RecienPuesto > 0:
                #  Delay to don't explode in the moment the bomb start
                self.RecienPuesto -= 1
            else:
                #  Once the delay finish
                for q in range(len(self.VolcanoBombs)):
                    ActionShoot = self.UpdateShoot(self.VolcanoBombs[q],{"Type":"Simple volcano"},False)
                    if ActionShoot == "Out Of Screen" or ActionShoot == "Crashed":
                        self.VolcanoBombs[q].Stop()
                        ChangePlayer = True
                        del self.VolcanoBombs[q]
                        break
        
        ###  BALL MOVEMENT AFTER EXPLOSION  ###
        
        if self.BallExplosion != False:
            #  Various variables
            Explotando = False
            PosBall = self.ShootClass.GetPos()
            Vel = 1
            #  Moving ball
            if self.__Points[self.GetPoint(PosBall[0])][1] < self.__Points[self.GetPoint(PosBall[0]-1)][1]:
                if self.BallExplosion == "Izq":
                    PosBall = self.__Points[self.GetPoint(PosBall[0]-Vel)]
                else:
                    Explotando = True
            else:
                if self.BallExplosion == "Der":
                    PosBall = self.__Points[self.GetPoint(PosBall[0]+Vel)]
                else:
                    Explotando = True
            #  Setting new position
            self.ShootClass.SetX(PosBall[0])
            self.ShootClass.SetY(PosBall[1])
            #  Checking crashes
            ActionShoot = self.UpdateShoot(self.ShootClass, {"Type":"Crashed ball"},False)
            if ActionShoot == "Out Of Screen":
                ChangePlayer = True
            if Explotando:
                self.ExplodeCrashedBall()
        
        ###  EXPLOITING  ###
        
        if self.Exploiting:
            #  For in all bombs exploiting
            for e in range(len(self.ExploitingData)):
                #  If the explosion is finished
                if self.ExploitingData[e]["Actual size"][0] >= self.ExploitingData[e]["Max size"][0]*2 and self.ExploitingData[e]["Actual size"][1] >= self.ExploitingData[e]["Max size"][1]:
                    #  Central pos of the explosion
                    PosExplosion = self.ExploitingData[e]["Pos explosion"]
                    #  If the bomb is inside the screen
                    if PosExplosion[0] > 0 and PosExplosion[0] < 800 and PosExplosion[1] > 0 and PosExplosion[1] < 600:
                        PosExplosion = self.__Points[self.GetPoint(PosExplosion[0])]
                        #  Generate explosion in mountain
                        self.DestroyTerrain(PosExplosion,(self.ExploitingData[e]["Max size"][0],self.ExploitingData[e]["Max size"][1]))
                        self.ModifyPlayersAfterExplode(PosExplosion, self.ExploitingData[e])
                    #  If is the last explosion, stop exploiting
                    if self.ExploitingData[e]["Last explosion"]:
                        self.Exploiting = False
                        ChangePlayer = True
                    del self.ExploitingData[e]
                    break
                else:
                    #  Increasing size of explosion
                    self.ExploitingData[e]["Actual size"][0] += 8
                    self.ExploitingData[e]["Actual size"][1] += 8
        
        ###  CHANGING PLAYERS  ###
        
        if ChangePlayer:
            self.ChangePlayer()
    def UpdateSurface(self):

        ###  GENERATING TANK IMAGE  ###
        
        self.__TankImage = img.Tanks[self.__PlayerColor]
        self.ImageTankMobile.setCurrentAngle(180-int(self.__Angle))
        self.__TankImage = self.ImageTankMobile.BlitSurfaceIn(self.__TankImage)
        
        ###  GENERATING SURFACE  ###
        
        SizeSurface = (self.ScreenSize[0],80)
        Surface = pygame.Surface(SizeSurface)
        Surface.fill(self.__Color)

        ###  ALL RENDERED THINGS  ###
        
        self.Rendered = {"Name":self.Render(self.__Name),"Nafta":self.Render(int(self.__Nafta)),"Energy":self.Render(int(self.__Energy)),"Repair kit":self.Render(self.__RepairKit),"Teleport":self.Render(self.__Teleport),"Money":self.Render("$ "+str(int(self.__Money))),"Force":self.Render(int(self.__Force)),"Angle":self.Render(int(self.__Angle)),"Wind":self.Render(int(self.__Wind))}
        
        ###  DATA SURFACE  ###
        
        #  Creating the surface
        SizeDataSurface = (220,SizeSurface[1])
        DataSurface = pygame.Surface(SizeDataSurface)
        DataSurface.fill(self.__Color)
        gui.add_border.add_border(DataSurface, (0,0,0), 0, 0, 1, 0)
        #  Positions
        self.PosImageName = [5,5]
        self.PosName = [self.PosImageName[0]+self.ImageName.get_size()[0]+5,self.PosImageName[1]+self.GetMid(self.ImageName, "Name")]
        self.PosImageNafta = [self.PosImageName[0],self.PosImageName[1]+self.ImageName.get_size()[1]+10]
        self.PosNafta = [self.PosImageNafta[0]+self.ImageNafta.get_size()[0]+5,self.PosImageNafta[1]+self.GetMid(self.ImageNafta, "Nafta")]
        self.PosImageEnergy = [self.PosImageNafta[0],self.PosImageNafta[1]+self.ImageNafta.get_size()[1]+10]
        self.PosEnergy = [self.PosImageEnergy[0]+self.ImageEnergy.get_size()[0]+5,self.PosImageEnergy[1]+self.GetMid(self.ImageEnergy, "Energy")]
        self.PosImageRepair = [self.PosEnergy[0]+self.Rendered["Energy"].get_size()[0]+25,self.PosImageEnergy[1]]
        self.PosRepair = [self.PosImageRepair[0]+self.ImageRepairKit.get_size()[0]+5,self.PosImageRepair[1]+self.GetMid(self.ImageRepairKit, "Repair kit")]
        self.PosImageTeleport = [self.PosRepair[0]+self.Rendered["Repair kit"].get_size()[0]+25,self.PosImageRepair[1]]
        self.PosTeleport = [self.PosImageTeleport[0]+self.ImageTeleport.get_size()[0]+5,self.PosImageTeleport[1]+self.GetMid(self.ImageTeleport, "Teleport")]
        #  Blits
        DataSurface.blit(self.ImageName,self.PosImageName)
        DataSurface.blit(self.Rendered["Name"],self.PosName)
        DataSurface.blit(self.ImageNafta,self.PosImageNafta)
        DataSurface.blit(self.Rendered["Nafta"],self.PosNafta)
        DataSurface.blit(self.ImageEnergy,self.PosImageEnergy)
        DataSurface.blit(self.Rendered["Energy"],self.PosEnergy)
        DataSurface.blit(self.ImageRepairKit,self.PosImageRepair)
        DataSurface.blit(self.Rendered["Repair kit"],self.PosRepair)
        DataSurface.blit(self.ImageTeleport,self.PosImageTeleport)
        DataSurface.blit(self.Rendered["Teleport"],self.PosTeleport)
        Surface.blit(DataSurface,(0,0))
        
        ###  FORCE SURFACE  ###
        
        #  Creating the surface
        SizeForceSurface = (280,SizeSurface[1])
        ForceSurface = pygame.Surface(SizeForceSurface)
        ForceSurface.fill(self.__Color)
        gui.add_border.add_border(ForceSurface, (0,0,0), 0, 0, 1, 0)
        self.Perc1 = float(self.ImageForce.get_size()[1])/100.0
        self.Perc2 = float(self.ImageAngle.get_size()[0])/180.0
        #  Positions
        self.PosImageForce = [10,5]
        self.PosForcePoint = [self.PosImageForce[0],self.PosImageForce[1]+int(self.Perc1*float(100-self.__Force))-1]
        self.PosForce = [self.PosImageForce[0]+self.ImageForce.get_size()[0]+5,self.PosImageForce[1]+self.ImageForce.get_size()[1]-self.Rendered["Force"].get_size()[1]]
        self.PosImageAngle = [self.PosImageForce[0]+self.ImageForce.get_size()[0]+80,10]
        self.PosAnglePoint = [self.PosImageAngle[0]+int(self.__Angle*self.Perc2)-1,self.PosImageAngle[1]]
        self.PosAngle = [self.PosImageAngle[0]+self.ImageAngle.get_size()[0]/2-(self.Rendered["Angle"].get_size()[0]+self.__TankImage.get_size()[0]+10)/2,self.PosImageAngle[1] + self.ImageAngle.get_size()[1] + 10]
        self.PosTankImage = [self.PosImageAngle[0]+self.ImageAngle.get_size()[0]/2-(self.Render("000").get_size()[0]+self.__TankImage.get_size()[0]+10)/2,self.PosAngle[1]+self.Rendered["Angle"].get_size()[1]/2-self.__TankImage.get_size()[1]/2]
        self.PosFire = [self.PosImageAngle[0]+self.ImageAngle.get_size()[0]+20+self.ImageFire["Hover"].get_size()[0]/2,self.ImageFire["Hover"].get_size()[1]]
        #  Size
        self.ForcePointSize = (self.ImageForce.get_size()[0]+1,2)
        #  Blits
        ForceSurface.blit(self.ImageForce,self.PosImageForce)
        ForceSurface.blit(pygame.Surface(self.ForcePointSize),self.PosForcePoint)
        ForceSurface.blit(self.Rendered["Force"],self.PosForce)
        ForceSurface.blit(self.ImageAngle,self.PosImageAngle)
        ForceSurface.blit(pygame.Surface((2,self.ImageAngle.get_size()[1])),self.PosAnglePoint)
        ForceSurface.blit(self.__TankImage,self.PosTankImage)
        ForceSurface.blit(self.Rendered["Angle"],(self.PosAngle[0]+self.__TankImage.get_size()[0]+10,self.PosAngle[1]))
        ForceSurface.blit(self.ImageFire[self.FireHoverState],[self.PosFire[0]-self.ImageFire[self.FireHoverState].get_size()[0]/2,self.PosFire[1]-self.ImageFire[self.FireHoverState].get_size()[1]/2])
        #  Bliting the surface
        self.PosForceSurface = (SizeDataSurface[0],0)
        Surface.blit(ForceSurface,self.PosForceSurface)
        
        ###  WEAPONS SURFACE  ###
        
        #  Creating the surface
        SizeWeaponSurface = [300,SizeSurface[1]]
        self.WeaponsSurface = pygame.Surface(SizeWeaponSurface)
        self.WeaponsSurface.fill(self.__Color)
        #  Creating surfaces
        self.WeaponsSelector = self.GenerateWeaponSelector(self.__Weapons)
        if self.__WindDir == -1:
            DirFlechaWind = 180
        else:
            DirFlechaWind = 0
        self.ImageFlechaWind = pygame.transform.rotate(pygame.transform.scale(img.FlechaWind,(int(img.FlechaWind.get_size()[0]/2.0/100.0*self.__Wind),10)),DirFlechaWind)
        #  Positions
        self.PosWeaponsSelector = [SizeWeaponSurface[0]/2-self.WeaponsSelector.get_size()[0]/2,5]
        self.PosImageWind = [self.PosWeaponsSelector[0]+self.WeaponsSelector.get_size()[0]/2-self.ImageWind.get_size()[0]/2+30,self.PosWeaponsSelector[1]+self.WeaponsSelector.get_size()[1]+5]
        self.PosFlechaWind = [self.PosImageWind[0]+self.ImageWind.get_size()[0]/2-self.ImageFlechaWind.get_size()[0]/2,self.PosImageWind[1]+self.ImageWind.get_size()[1]+2]
        self.PosWind = [self.PosImageWind[0]+self.ImageWind.get_size()[0]+10,self.PosImageWind[1]+10]
        self.PosMoney = [self.PosWeaponsSelector[0]+self.WeaponsSelector.get_size()[0]/2-self.ImageWind.get_size()[0]/2-30-self.Rendered["Wind"].get_size()[0],self.PosWeaponsSelector[1]+self.WeaponsSelector.get_size()[1]+10]
        #  Blits
        self.WeaponsSurface.blit(self.WeaponsSelector,self.PosWeaponsSelector)
        self.WeaponsSurface.blit(self.ImageWind,self.PosImageWind)
        self.WeaponsSurface.blit(self.ImageFlechaWind,self.PosFlechaWind)
        self.WeaponsSurface.blit(self.Rendered["Wind"],self.PosWind)
        self.WeaponsSurface.blit(self.Rendered["Money"],self.PosMoney)
        #  Bliting the surface
        self.PosWeaponSurface = [self.PosForceSurface[0]+ForceSurface.get_size()[0],0]
        Surface.blit(self.WeaponsSurface,self.PosWeaponSurface)
        
        ###  BLITTING THE SURFACE  ###
        
        self.Surface = Surface
    def GraphicUpdate(self,Screen):
        
        ###  TELEPORTING  ###
        
        if self.FlechaMouseActive:
            Screen.blit(self.ImageFlechaMouse,self.PosFlechaMouse)
        
        ###  SHOOTING UPDATE  ###
        
        if self.Shooting:
            if self.ShootClass != None:
                self.ShootClass.graphic_update(Screen)
        
        if self.MultipleShooting:
            if len(self.MultipleBalls) > 0:
                for q in range(len(self.MultipleBalls)):
                    self.MultipleBalls[q].graphic_update(Screen)
        
        ###  VOLCANO UPDATING  ###
        
        if self.VolcanoExplosion:
            for q in self.VolcanoBombs:
                q.graphic_update(Screen)
        
        ###  EXPLOITING  ###
        
        if self.Exploiting:
            for e in range(len(self.ExploitingData)):
                PosImageExplosion = [self.ExploitingData[e]["Pos explosion"][0]-self.ExploitingData[e]["Actual size"][0]/2,self.ExploitingData[e]["Pos explosion"][1]-self.ExploitingData[e]["Actual size"][1]/2]
                Screen.blit(pygame.transform.scale(self.ImageExplosion,self.ExploitingData[e]["Actual size"]),PosImageExplosion)
    
        ###  BLITING THE SURFACE  ###
        
        Screen.blit(self.Surface,(0,0))
    def LogicUpdate(self,Events):
        
        self.UpdateData()
        
        self.UpdateExplosions()
        self.UpdateSurface()
        
        NowPressed = Events.mouse.get_now_pressed()[0]
        
        if not self.FlechaMouseActive:
            ###  LOGIC UPDATE FOR ACTIVE VOLCANO BOMBS  ###
            if self.VolcanoExplosion:
                for q in self.VolcanoBombs:
                    q.logic_update(Events)
            
            self.Events = Events
            ###  LOGIC UPDATE FOR THE SHOOT CLASS IF ACTIVE  ###
            if self.Shooting:
                if self.ShootClass != None:
                    self.ShootClass.logic_update(Events)
            if self.MultipleShooting:
                if len(self.MultipleBalls) > 0:
                    for q in range(len(self.MultipleBalls)):
                        self.MultipleBalls[q].logic_update(Events)
            
            ###  IN THE DATA SURFACE  ###
            
            Events.generate_relative((0,0))
            
            #  If repair kit
            if gui.Clasic.GetFocused(Events, self.PosImageRepair, self.ImageRepairKit.get_size()):
                if NowPressed:
                    if self.__Players[self.PlayerAct]["Repair kit"] > 0:
                        RangeOfRepair = 10
                        if self.__Players[self.PlayerAct]["Energy"] + RangeOfRepair < 100:
                            self.__Players[self.PlayerAct]["Energy"] += RangeOfRepair
                        elif self.__Players[self.PlayerAct]["Energy"] < 100:
                            self.__Players[self.PlayerAct]["Energy"] = 100
                        else:
                            self.__Players[self.PlayerAct]["Repair kit"] += 1
                        self.__Players[self.PlayerAct]["Repair kit"] -= 1
            
            #  If teleport
            if gui.Clasic.GetFocused(Events, self.PosImageTeleport, self.ImageTeleport.get_size()):
                if NowPressed:
                    if self.__Players[self.PlayerAct]["Teleport"] > 0 and not self.Exploiting and not self.Shooting:
                        self.Teleporting = True
                        self.FlechaMouseActive = True
            
            Events.delete_relative()
            
            ###  IN THE FORCE SURFACE  ###
            
            #  Generating relative of the force surface
            Events.generate_relative(self.PosForceSurface)
            
            #  If moving force
            Events.generate_relative(self.PosImageForce)
            if gui.Clasic.GetFocused(Events, (0,0), self.ImageForce.get_size()):
                if NowPressed:
                    self.MovingForcePoint = True
            if self.MovingForcePoint:
                if Events.mouse.get_now_up_pressed()[0]:
                    self.MovingForcePoint = False
                if self.__Players[self.PlayerAct]["Energy"] < 100:
                    MaxForce = self.__Players[self.PlayerAct]["Energy"]
                else:
                    MaxForce = 100
                NewForce = 100-(Events.mouse.get_position()[1])/self.Perc1
                if NewForce >= 0 and NewForce <= MaxForce:
                    self.__Force = NewForce
                elif NewForce < 0:
                    self.__Force = 0
                elif NewForce > MaxForce:
                    self.__Force = MaxForce
            Events.delete_relative()
            
            #  If moving angle
            Events.generate_relative(self.PosImageAngle)
            if gui.Clasic.GetFocused(Events, (0,0), self.ImageAngle.get_size()):
                if NowPressed:
                    self.MovingAnglePoint = True
            if self.MovingAnglePoint:
                if Events.mouse.get_now_up_pressed()[0]:
                    self.MovingAnglePoint = False
                NewAngle = Events.mouse.get_position()[0]/self.Perc2
                if NewAngle >= 0 and NewAngle <= 180:
                    self.__Players[self.PlayerAct]["Angle"] = NewAngle
                elif NewAngle < 0:
                    self.__Players[self.PlayerAct]["Angle"] = 0
                elif NewAngle > 180:
                    self.__Players[self.PlayerAct]["Angle"] = 180
            Events.delete_relative()
            
            #  If fire
            PressedSpace = Events.keyboard[pygame.K_SPACE]
            if gui.Clasic.GetFocused(Events, [self.PosFire[0]-self.ImageFire["Hover"].get_size()[0]/2,self.PosFire[1]-self.ImageFire["Hover"].get_size()[1]/2], self.ImageFire["Hover"].get_size()) or PressedSpace:
                self.FireHoverState = "Hover"
                if NowPressed or PressedSpace:
                    if self.__Weapons[self.WeaponSelectActive]["Type"] != "Air strike":
                        self.Shooting = True
                        Point = self.GetPoint(int(self.__Xposition))
                        self.ShootClass = self.GenerateShoot(self.__Angle, int(self.__Force/5), float(self.__Wind)/1000.0*self.__WindDir, self.__Xposition, self.__Points[Point][1])
                    else:
                        self.FlechaMouseActive = True
                        self.SelectingAirStrike = True
            else:
                self.FireHoverState = "Not Hover"
            
            Events.delete_relative()
            
            ###  IN THE WEAPONS SURFACE  ###
            
            Events.generate_relative(self.PosWeaponSurface)
            #  If changing weapon
            Events.generate_relative(self.PosWeaponsSelector)
            if NowPressed:
                if gui.Clasic.GetFocused(Events, self.PosWeaponFlechas[0], self.FlechaIzquierda.get_size()):
                    self.ChangeWeapon("Left")
                if gui.Clasic.GetFocused(Events, self.PosWeaponFlechas[1], self.FlechaDerecha.get_size()):
                    self.ChangeWeapon("Right")
            Events.delete_relative()
            Events.delete_relative()
            
            ###  MOVING TANK  ###
            
            if self.__Players[self.PlayerAct]["Actual fuel"] > 0 and not self.Shooting:
                if self.__Players[self.PlayerAct]["Xposition"] > 0:
                    if Events.keyboard[pygame.K_LEFT]:
                        TempPos = int(self.__Players[self.PlayerAct]["Xposition"] - 1)
                        Disf = self.__Points[self.GetPoint(TempPos)][1]-self.__Points[self.GetPoint(TempPos)-1][1]
                        if Disf < 2*(self.__Players[self.PlayerAct]["Upgrade hill move"]+1):
                            self.__Players[self.PlayerAct]["Xposition"] -= 1
                        self.__Players[self.PlayerAct]["Actual fuel"] -= 1/(self.__Engine+1)
                if self.__Players[self.PlayerAct]["Xposition"] < 800:
                    if Events.keyboard[pygame.K_RIGHT]:
                        TempPos = int(self.__Players[self.PlayerAct]["Xposition"] + 1)
                        Disf = self.__Points[self.GetPoint(TempPos)][1]-self.__Points[self.GetPoint(TempPos)+1][1]
                        if Disf < 2*(self.__Players[self.PlayerAct]["Upgrade hill move"]+1):
                            self.__Players[self.PlayerAct]["Xposition"] += 1
                        self.__Players[self.PlayerAct]["Actual fuel"] -= 1/(self.__Engine+1)
            
            ###  MOVING ANGLE WITH KEYS  ###
            
            if Events.keyboard[pygame.K_UP]:
                if self.__Players[self.PlayerAct]["Angle"] < 179:
                    self.__Players[self.PlayerAct]["Angle"] += 1.2
            if Events.keyboard[pygame.K_DOWN]:
                if self.__Players[self.PlayerAct]["Angle"] > 0:
                    self.__Players[self.PlayerAct]["Angle"] -= 1.2
        
            ###  CHANGING WEAPONS WITH KEYS  ###
            
            if Events.keyboard[pygame.K_q]:
                self.ChangeWeapon("Left")
            elif Events.keyboard[pygame.K_w]:
                self.ChangeWeapon("Right")
    
        ###  MOUSE POSITION ###
        
        x,y = Events.mouse.get_position()
        
        ###  FLECHA MOUSE  ###
        
        if self.FlechaMouseActive:
            self.PosFlechaMouse = [x-self.ImageFlechaMouse.get_size()[0],y-self.ImageFlechaMouse.get_size()[1]]
            if NowPressed and y > self.Surface.get_size()[1]:
                if self.Teleporting:
                    #  Teleporting
                    self.Teleporting = False
                    self.__Players[self.PlayerAct]["Xposition"] = x
                    self.__Players[self.PlayerAct]["Teleport"] -= 1
                    self.ChangePlayer()
                elif self.SelectingAirStrike:
                    #  Selecting air strike position
                    self.SelectingAirStrike = False
                    self.MultipleShooting = True
                    self.ExploitingData = []
                    XAct = x-50
                    for q in range(5):
                        ShootClass = self.GenerateShoot(0, 8, float(self.__Wind)/1000.0*self.__WindDir, XAct, 0)
                        self.MultipleBalls.append(ShootClass)
                        XAct += 20
                self.FlechaMouseActive = False
    def logic_update(self,Events):
        self.LogicUpdate(Events)
    def graphic_update(self,Screen):
        self.GraphicUpdate(Screen)
