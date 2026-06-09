import csv
from participante_template import Participante
from resumen_template import Resumen
def int_bool(n:str) -> bool:
    if n == '0':
        return False
    else:
        return True

participantes:list[Participante] = []
f = open('rmet.csv')
for linea in csv.DictReader(f):
    e:int=int(linea['edad'])
    h:bool=int_bool(linea['tieneHijos'])
    ch:int=int(linea['cantidadHijos'])
    g:int=int(linea['genero'])
    ne:int=int(linea['nivelEducativo'])
    r:int=int(linea['religiosidad'])
    pol:int=int(linea['conservadorProgresista'])
    id_p:int=int(linea['userId'])
    cor:int= sum(int(linea[f'{i}_correct']) for i in range(1, 13))
    participante:Participante= Participante(e,h,ch,g,ne,r,pol,id_p,cor)
    participantes.append(participante)

parti= list(participantes[:2])
participantes2=list(participantes[3:5])
Res:Resumen=Resumen(parti)
res2=Resumen(participantes2)
print(Res==res2)