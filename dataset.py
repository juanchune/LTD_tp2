#importa todo del archivo participante,
#tanto la clase como funciones auxiliares
import participante as p
import resumen as r
class DataSet:
    def __init__(self, archivo_csv:str):
        ''' Inicializa un objeto de la clase Dataset a partir del csv
        archivo_csv'''
        self.participantes:list[p.Participante] = p.crear_lista_participantes('rmet.csv')
        self.niveles:set[str] = set()
        for i in self.participantes:
            self.niveles.add(i.nivel)
        
    def __len__(self) -> int:
        '''Devuelve la cantidad de participantes de self'''
        return len(self.participantes)

    def participantes_en_rango_etario(self, edad1:int, edad2:int) -> list[p.Participante]:
        ''' Req: 0 < edad1 < edad2.
            Dev: una lista con los participantes cuya edad
                esté entre edad1 y edad2 (inclusive). '''
        xs:list[p.Participante] = []
        for i in self.participantes:
            if i.edad <= edad2 and i.edad >= edad1:
                xs.append(i)
        return xs

    def resumenes_NE(self) -> dict[str, r.Resumen]:
        '''
        Dev: un diccionario donde las claves son los niveles educativos
        presentes en self y los valores son sus resúmenes correspondientes
        '''
        res:dict[str, r.Resumen] = dict()
        
        nivel:list[p.Participante] = []
        
        for n in self.niveles:
            for par in self.participantes:
                if par.nivel == n:
                    nivel.append(par)
            if len(nivel) >= 2:
                res[n] = r.Resumen(nivel)
            nivel = []
        return res
    
    def participantes_mayores_notas(self, ne:str) -> list[p.Participante]:
        ''' Req: ne in self.niveles.
            Dev: una lista de Participante con nivel ne y cantidad
            de respuestas correctas mayor al promedio+desvio estandar '''
        res:list[p.Participante] = []
        for i in self.participantes:
            if i.nivel == ne:
                res.append(i)
        resumen_ne:r.Resumen = r.Resumen(res)
        for i in res:
            if i.correctas <= int(resumen_ne.correctas[0] + resumen_ne.correctas[1]):
                res.pop(i)
        return res

    def exportar_por_edad(self):
        ''' completar docstring '''
        pass
    
    ## y asi con el resto de los metodos


p1:list[p.Participante] = p.crear_lista_participantes('rmet.csv', 5)
print(len(p1))
r1:r.Resumen = r.Resumen(p1)
dt:DataSet = DataSet('rmet.csv')
d:dict[str, r.Resumen] = dt.resumenes_NE()
for i in d:
    print(i, ': ', d[i])