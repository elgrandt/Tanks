'''
Created on 05/03/2014

@author: Dylan
'''
def CreateLines(texto,ancho,Font):
        if Font.render(texto,1,(0,0,0)).get_size()[0] > ancho:
            lineas = []
            palabras = []
            palabra = ""
            for q in texto:
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
                    n1 = Font.render(test,1,(0,0,0))
                    n2 = Font.render(test2,1,(0,0,0))
                    if n1.get_size()[0] <= ancho and n2.get_size()[0] >= ancho:
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
                if lineas[q][len(lineas[q])-1] == " ":
                    lineas[q] = lineas[q][:len(lineas[q])-1]
            return lineas
        else:
            return [texto]