'''
Created on 05/03/2014

@author: Dylan
'''
import pygame
import gui
import Loaded

class GenerateMenu:
    def __init__(self,SizeX,Color,Position):
        self.Size = [SizeX,0]
        self.Color = Color
        self.Position = Position
        self.Yact = 10
        self.__Titles = []
        self.__Radios = []
        self.SizeRadios = [20,20]
        SizeSurfaceInside = [self.SizeRadios[0]-6,self.SizeRadios[1]-6]
        self.SurfaceInside = gui.Circle.CircleBorderRectangle(SizeSurfaceInside, (0,0,0), SizeSurfaceInside[0]/2, False, 0)
        self.__RadioActive = 0
        self.__Separators = []
        self.__Selects = []
        self.FlechaIzquierda = pygame.transform.scale(Loaded.Images.FlechaIzquierda,(20,20))
        self.FlechaDerecha = pygame.transform.scale(Loaded.Images.FlechaDerecha,(20,20))
        self.LT = pygame.time.get_ticks()
        self.__Texts = []
        self.__Inputs = []
        self.__LinesOfRadios = []
        self.LinesOfRadiosActives = []
        self.Margin = 40
    def UpdatePosition(self,NewPos):
        self.Position = NewPos
    def AddTitle(self,Title,Color = (0,0,0)):
        FontTitle = Loaded.Fonts.ClassicFont(20)
        Titles = gui.Lines.CreateLines(Title, self.Size[0], FontTitle)
        for q in Titles:
            RenderedAct = FontTitle.render(q,1,Color)
            PosAct = [self.Size[0]/2-RenderedAct.get_size()[0]/2,self.Yact]
            self.__Titles.append({"Surface":RenderedAct,"Position":PosAct})
            self.Yact += RenderedAct.get_size()[1] + 5
        self.Yact -= 5
    def AddRadio(self,Text,Color=(255,255,255)):
        FontRadios = Loaded.Fonts.ClassicFont(15)
        RenderedText = FontRadios.render(Text,1,(0,0,0))
        Xact = self.Margin+self.SizeRadios[0]+5
        self.__Radios.append({"Rendered":RenderedText,"Position":[Xact,self.Yact],"Text":Text,"Color":Color})
        self.Yact += self.SizeRadios[1]
    def AddSpace(self,Space):
        self.Yact += Space
    def AddSeparator(self,Color):
        SurfaceSeparator = pygame.Surface((self.Size[0]-20,1))
        SurfaceSeparator.fill(Color)
        self.__Separators.append({"Surface":SurfaceSeparator,"Position":[10,self.Yact+10]})
        self.Yact += 21
    def AddSelect(self,Options,Name):
        if len(Options) > 0:
            FontAct = Loaded.Fonts.ClassicFont(15)
            RenderedOptions = []
            for q in Options:
                RenderedOptions.append(FontAct.render(q,1,(0,0,0)))
            self.__Selects.append({"Options":RenderedOptions,"YPosition":self.Yact,"Selected":0,"PositionFlechaI":[0,0],"PositionFlechaD":[0,0],"PositionText":[0,0],"Name":Name,"OptionTexts":Options})
            self.Yact += self.FlechaDerecha.get_size()[1]
    def AddText(self,Text,Size):
        FontText = Loaded.Fonts.ClassicFont(Size)
        TextList = gui.Lines.CreateLines(Text, self.Size[0]-10, FontText)
        for q in TextList:
            Rend = FontText.render(q,1,(0,0,0))
            Pos = [self.Size[0]/2-Rend.get_size()[0]/2,self.Yact]
            self.__Texts.append({"Rendered":Rend,"Position":Pos})
            self.Yact += Rend.get_size()[1]+5
        self.Yact -= 5
    def AddInput(self,Text,Name):
        Text = Text+":"
        Input = gui.input_text.text_input()
        Input.allowLetters()
        Input.allowNumbers()
        Input.set_alpha_states(0.9, 1)
        Input.set_show_text("Here")
        Input.set_background((255,255,255))
        Font = Loaded.Fonts.ClassicFont(18)
        RenderedText = Font.render(Text,1,(0,0,0))
        Position = [self.Margin+RenderedText.get_size()[0]+10,self.Yact]
        Input.set_position(Position)
        Input.set_dimensions((self.Size[0]-Position[0]-40,30))
        self.Yact += Input.H
        PositionText = [Position[0]-10-RenderedText.get_size()[0],Position[1]+Input.H/2-RenderedText.get_size()[1]/2]
        self.__Inputs.append({"Object":Input,"Text":RenderedText,"PositionText":PositionText,"Name":Name})
    def AddLineOfRadios(self,Title,Radios):
        Title = Title + ":"
        FontRadios = Loaded.Fonts.ClassicFont(17)
        RenderedTitle = FontRadios.render(Title,1,(0,0,0))
        PosText = [self.Margin,self.Yact+RenderedTitle.get_size()[1]/2-self.SizeRadios[1]/2]
        Xact = PosText[0]+RenderedTitle.get_size()[0]+10
        ActualLine = []
        for q in Radios:
            PosRadAct = [Xact,self.Yact]
            ActualLine.append({"Position":PosRadAct,"Text":q["Title"],"Color":q["Color"]})
            Xact += self.SizeRadios[0]+5
        self.__LinesOfRadios.append({"RenderedTitle":RenderedTitle,"Title":Title,"Objects":ActualLine,"PositionTitle":PosText})
        self.LinesOfRadiosActives.append(0)
        if RenderedTitle.get_size()[1] > self.SizeRadios[1]:
            self.Yact += RenderedTitle.get_size()[1]
        else:
            self.Yact += self.SizeRadios[1]
    def SetSelectedRadio(self,Text):
        for q in range(len(self.__Radios)):
            if self.__Radios[q]["Text"] == Text:
                self.__RadioActive = q
                break
    def GetSelectedRadio(self):
        return self.__Radios[self.__RadioActive]["Text"]
    def GetSelectedSelect(self,SelectName):
        for q in self.__Selects:
            if q["Name"] == SelectName:
                return q["OptionTexts"][q["Selected"]]
    def GetInputWritten(self,Name):
        for q in self.__Inputs:
            if q["Name"] == Name:
                return q["Object"].get_curent_text()
    def GetSelectedLineOfRadios(self,TitleOfLine):
        for w in range(len(self.__LinesOfRadios)):
            q = self.__LinesOfRadios[w]
            if q["Title"][:len(q["Title"])-1] == TitleOfLine:
                return q["Objects"][self.LinesOfRadiosActives[w]]["Text"]
    def graphic_update(self,Screen):
        self.Size[1] = self.Yact + 10
        Surface = gui.Circle.CircleBorderRectangle(self.Size, self.Color, 20, False, 0, 150)
        for q in self.__Titles:
            Surface.blit(q["Surface"],q["Position"])
        for w in range(len(self.__Radios)):
            q = self.__Radios[w]
            if self.__RadioActive == w:
                self.__SurfaceRadioActive = gui.Circle.CircleBorderRectangle(self.SizeRadios, q["Color"], self.SizeRadios[0]/2, False, 2)
                self.__SurfaceRadioActive.blit(self.SurfaceInside,(3,3))
                Surface.blit(self.__SurfaceRadioActive,[self.Margin,q["Position"][1]])
            else:
                self.__SurfaceRadioInactive = gui.Circle.CircleBorderRectangle(self.SizeRadios, q["Color"], self.SizeRadios[0]/2, False, 2)
                Surface.blit(self.__SurfaceRadioInactive,[self.Margin,q["Position"][1]])
            if q["Rendered"] != None:
                Surface.blit(q["Rendered"],[q["Position"][0],q["Position"][1]+self.SizeRadios[1]/2-q["Rendered"].get_size()[1]/2])
        for q in self.__Separators:
            Surface.blit(q["Surface"],q["Position"])
        for w in range(len(self.__Selects)):
            q = self.__Selects[w]
            SelectedOption = q["Options"][q["Selected"]]
            GlobalSizeX = self.FlechaIzquierda.get_size()[0]+self.FlechaDerecha.get_size()[0]+SelectedOption.get_size()[0]+20
            Position = [self.Size[0]/2-GlobalSizeX/2,q["YPosition"]]
            PositionFlechaI = Position[0]
            PositionText = PositionFlechaI+self.FlechaIzquierda.get_size()[0]+10
            PositionFlechaD = PositionText+SelectedOption.get_size()[0]+10
            PositionY = q["YPosition"]
            self.__Selects[w]["PositionFlechaI"] = [PositionFlechaI,PositionY]
            self.__Selects[w]["PositionText"] = [PositionText,PositionY+self.FlechaIzquierda.get_size()[1]/2-SelectedOption.get_size()[1]/2]
            self.__Selects[w]["PositionFlechaD"] = [PositionFlechaD,PositionY]
            Surface.blit(self.FlechaIzquierda,q["PositionFlechaI"])
            Surface.blit(SelectedOption,q["PositionText"])
            Surface.blit(self.FlechaDerecha,q["PositionFlechaD"])
        for q in self.__Texts:
            Surface.blit(q["Rendered"],q["Position"])
        for q in self.__Inputs:
            Surface.blit(q["Text"],q["PositionText"])
            q["Object"].graphic_update(Surface)
        for e in range(len(self.__LinesOfRadios)):
            q = self.__LinesOfRadios[e]
            Surface.blit(q["RenderedTitle"],q["PositionTitle"])
            for r in range(len(q["Objects"])):
                w = q["Objects"][r]
                if self.LinesOfRadiosActives[e] == r:
                    self.__SurfaceRadioActive = gui.Circle.CircleBorderRectangle(self.SizeRadios, w["Color"], self.SizeRadios[0]/2, False, 2)
                    self.__SurfaceRadioActive.blit(self.SurfaceInside,(3,3))
                    Surface.blit(self.__SurfaceRadioActive,w["Position"])
                else:
                    self.__SurfaceRadioInactive = gui.Circle.CircleBorderRectangle(self.SizeRadios, w["Color"], self.SizeRadios[0]/2, False, 2)
                    Surface.blit(self.__SurfaceRadioInactive,w["Position"])
                    
        Screen.blit(Surface,self.Position)
    def logic_update(self,Events):
        Events.generate_relative(self.Position)
        for q in range(len(self.__Radios)):
            if gui.Clasic.GetFocused(Events, (self.Margin,self.__Radios[q]["Position"][1]), self.SizeRadios):
                if Events.mouse.get_now_pressed()[0]:
                    self.__RadioActive = q
        for q in range(len(self.__LinesOfRadios)):
            for w in range(len(self.__LinesOfRadios[q]["Objects"])):
                e = self.__LinesOfRadios[q]["Objects"][w]
                if gui.Clasic.GetFocused(Events, e["Position"], self.SizeRadios):
                    if Events.mouse.get_now_pressed()[0]:
                        self.LinesOfRadiosActives[q] = w
        for q in self.__Inputs:
            q["Object"].logic_update(Events)
        self.LT = pygame.time.get_ticks()
        for w in range(len(self.__Selects)):
            q = self.__Selects[w]
            if Events.mouse.get_now_pressed()[0]:
                if gui.Clasic.GetFocused(Events, q["PositionFlechaI"],self.FlechaIzquierda.get_size()):
                    self.__Selects[w]["Selected"] -= 1
                    if self.__Selects[w]["Selected"] < 0:
                        self.__Selects[w]["Selected"] = len(q["Options"])-1
                if gui.Clasic.GetFocused(Events, q["PositionFlechaD"],self.FlechaDerecha.get_size()):
                    self.__Selects[w]["Selected"] += 1
                    if self.__Selects[w]["Selected"] > len(q["Options"])-1:
                        self.__Selects[w]["Selected"] = 0
        Events.delete_relative()