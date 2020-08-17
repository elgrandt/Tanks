import Loaded.Fonts as fonts
import pygame
import add_border

class alert:
    def __init__(self,Text = ""):
        self.Text = Text
        self.Font = fonts.ClassicFont(15)
        self.Enabled = True
        self.Color_boton = (255,255,255)
        while self.Enabled:
            pygame.display.update()
            pantalla = pygame.display.get_surface()
            self.graphic_update(pantalla)
            self.logic_update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Enabled = False
    def graphic_update(self,Pantalla):
        self.Render_boton = self.Font.render("Aceptar",1,(0,0,0))
        self.Tboton = [self.Render_boton.get_size()[0] + 40, self.Render_boton.get_size()[1] + 10]
        self.Boton = pygame.Surface((self.Tboton[0] + 4, self.Tboton[1] + 4))
        self.Surface_boton = pygame.Surface(self.Tboton)
        self.Surface_boton.fill(self.Color_boton)
        self.Boton.blit(self.Surface_boton,(2,2))
        self.Boton.blit(self.Render_boton,(self.Boton.get_size()[0]/2-self.Render_boton.get_size()[0]/2,self.Boton.get_size()[1]/2-self.Render_boton.get_size()[1]/2))
        self.Talert = [300,10]
        lineas = []
        palabras = []
        palabra = ""
        for q in self.Text:
            if q == " ":
                palabras.append(palabra)
                palabra = ""
            else:
                palabra += q
        if palabra != "":
            palabras.append(palabra)
        end = False
        while not end:
            for q in range(len(palabras)):
                test = ""
                for w in range(q):
                    test += palabras[w] + " "
                test2 = ""
                for w in range(q+1):
                    test2 += palabras[w] + " "
                n1 = self.Font.render(test,1,(0,0,0))
                n2 = self.Font.render(test2,1,(0,0,0))
                if n1.get_size()[0] < self.Talert[0] and n2.get_size()[0] >= self.Talert[0]:
                    lineas.append(test)
                    for w in range(q):
                        del palabras[0]
                    break
                if q == len(palabras)-1:
                    if len(palabras) > 0:
                        test = ""
                        for w in palabras:
                            test += w + " "
                        lineas.append(test)
                        end = True
        for q in range(len(lineas)):
            self.Talert[1] += self.Font.render(lineas[q],1,(0,0,0)).get_size()[1] + 10
            if lineas[q][len(lineas[q])-1] == " ":
                lineas[q] = lineas[q][:len(lineas[q])-1]
        self.Talert[1] += self.Tboton[1] + 10
        self.Position = [Pantalla.get_size()[0]/2-self.Talert[0]/2,Pantalla.get_size()[1]/2-self.Talert[1]/2]
        self.Alert = pygame.Surface(self.Talert)
        self.Alert.fill((255,255,255))
        self.Alert = add_border.add_border(self.Alert, (0,0,0), 2, 2, 2, 2)
        pos_y = 10
        for q in range(len(lineas)):
            rendered = self.Font.render(lineas[q],1,(0,0,0))
            self.Alert.blit(rendered,(self.Talert[0]/2-rendered.get_size()[0]/2,pos_y))
            pos_y += rendered.get_size()[1] + 10
        pos_boton = (self.Talert[0]/2-self.Tboton[0]/2,pos_y)
        self.Position_boton = (self.Position[0] + pos_boton[0], self.Position[1] + pos_boton[1])
        self.Alert.blit(self.Boton,pos_boton)
        Pantalla.blit(self.Alert,self.Position)
    def logic_update(self):
        x,y = pygame.mouse.get_pos()
        if x > self.Position_boton[0] and x < self.Position_boton[0] + self.Tboton[0] and y > self.Position_boton[1] and y < self.Position_boton[1] + self.Tboton[1]:
            if pygame.mouse.get_pressed()[0]:
                self.Enabled = False
            else:
                self.Color_boton = (190,181,181)
        else:
            self.Color_boton = (255,255,255)