from participante import Participante
class Resumen:
    def __init__(self, par:list[Participante]):
        '''
        Req: len(par) >= 2.
        Inicializa un Resumen a partir de la lista de Participante par.
        '''
        if len(par) >= 2:
            
            correctas:list[int]=[]
            edad:list[int]=[]
            politica:list[int]=[]
            religion:list[int]=[]
            
            for p in par: # p  = cada participante
                correctas.append(p.correctas)
                edad.append(p.edad)           # se agregan los distintos datos del
                politica.append(p.politica)   # participante a su respectiva lista 
                religion.append(p.religion)   
            self.participantes:list[Participante]=par
            self.correctas:tuple[float]=(round(promedio(correctas),2), round(desvioestandar(correctas),2))
            self.edad:tuple[float]=(round(promedio(edad),2), round(desvioestandar(edad),2))
            self.politica:tuple[float]=(round(promedio(politica),2), round(desvioestandar(politica),2))
            self.religiosidad:tuple[float]=(round(promedio(religion),2), round(desvioestandar(religion),2))
        
    def __len__(self) -> int:
        '''
        Devuelve: Un entero con la cantidad de 
                  participantes considerados en el resumen'''
        return len(self.participantes)

    def __repr__(self) -> str:
        ''' Devuelve: Una representacion en string de Resumen '''
        return 'Correctas: ' + str(self.correctas) + ', Edad: ' + str(self.edad)+ ', Política: ' + str(self.politica) + ', Religiosidad: ' + str(self.religiosidad) + ', Cant: ' + str(len(self.participantes))

    def __eq__(self, other) -> bool:
        '''Devuelve: True si ambos resúmenes tienen igual cantidad, 
           promedios y desvíos estándares. '''
        return (len(self.participantes)==len(other.participantes)) and abs(self.correctas[0]-other.correctas[0])<0.001 and abs(self.correctas[1]-other.correctas[1])<0.001

def promedio(lista:list[int])->float:
    '''
    Requiere: len(lista)>0
    Devuelve: El promedio de los elementos de lista
    '''
    cant:int = 0
    for i in lista:
        cant+=i
    return round(cant/len(lista),2)

def desvioestandar(lista:list[int]) -> float:
    '''
    Requiere: len(lista)>0
    Devuelve: El desvio estandar en comparación al promedio 
              de los elementos de lista
    '''
    cant:int = 0
    prom:float = promedio(lista)
    for i in lista:
        cant+= (i - prom)**2 # **2 sirve para que el número no de negativo
    return round((cant/(len(lista)-1))**(1/2),2) # **1/2 permite volver a la normalidad
