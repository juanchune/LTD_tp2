# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:55:30 2026

@author: jmobilia
"""

from participante_template import Participante
def int_bool(n:int) -> bool:
    if n == 0:
        return False
    else:
        return True
    

participantes:list[Participante] = []
f = open('rmet.csv')
for linea in f:
    if len(participantes) >= 30:
        break
    
    #saltamos la primera linea con las claves
    if 'edad' not in linea:
        xs:list[str] = linea.split(',')
        
        #hacemos una lista con las columnas de respuestas,
        #para sumarlas y almacenar la cantidad de respuestas correctas
        #en una misma variable
        xs_cor = xs[8:]
        correctas:int = 0
        for c in xs_cor:
            correctas+= int(c)
            
        #agregamos todos los valores convertidos a su tipo correspondiente
        participantes.append(Participante(
            int(xs[0]), #edad
            int_bool(xs[1]), #hijos
            int(xs[2]), #cantidad de hijos
            int(xs[3]), #genero
            int(xs[4]), #nivel educativo
            int(xs[5]), #religiosidad
            int(xs[6]), #progresismo politico
            int(xs[7]), #id del participante
            correctas
))
print(participantes)