class Participante:
    def __init__(self, e:int, h:bool, ch:int, g:int,
        ne:int, r:int, pol:int, id_p:int, cor:int):
        '''Inicializa un participante con edad e, hijos h, cantidad de
        hijos ch (si h == True), genero g, nivel educativo ne, nivel de
        religiosidad r, nivel de progresismo politico p, id id_p y
        cantidad de respuestas correctas cor.'''
        self.edad:int = e
        self.tiene_hijos:bool = h
        
        #cantidad de h segun el valor de h
        if h:
            self.cant_hijos:int = ch
        else:
            self.cant_hijos:int = 0
        
        #genero
        if g == 1:
            self.genero:str = 'Varon'
        else:
            self.genero:str = 'Mujer'
            
        #nivel educativo
        if ne == 1:
            self.nivel:str = 'primario incompleto'
        elif ne == 2:
            self.nivel:str = 'primario completo'
        elif ne == 3:
            self.nivel:str = 'secundario completo'
        elif ne == 4:
            self.nivel:str = 'terciario incompleto'
        elif ne == 5:
            self.nivel:str = 'terciario completo'
        elif ne == 6:
            self.nivel:str = 'posgrado completo'
        
        self.politica:int = pol
        self.religion:int = r
        self.id:int = id_p
        self.correctas:int = cor


    def __repr__(self) -> str:
        '''Devuelve: una representacion en string de participante'''
        return 'Genero: ' + self.genero + ', NE: ' + self.nivel + ', Edad: ' + str(self.edad) + ', Correctas: ' + str(self.correctas) + ', ID: ' + str(self.id)
    
    def __eq__(self, other) -> bool:
        '''Devuelve:True si p1 y p2 tienen misma edad y misma cantidad de 
                    respuestas correctas, y False en caso contrario.'''
        return self.edad == other.edad and self.correctas == other.correctas
    
#-----------------------------------------------------------------------------#
#FUNCIONES PARA FACILITAR LA CREACION DE RESUMEN:

def str_a_bool(n:str) -> bool:
    '''
    Req: n tenga un valor binario (n == '0' o n == '1')
    Dev: el valor booleano de n
    '''
    if n == '0':
        return False
    else:
        return True

#Por defecto, n = None, para que se pueda poner un limite opcional de participantes
def crear_lista_participantes(archivo:str, n:int = None) ->list[Participante]:
    '''
    Req: n > 0.
    Dev: una lista de n Participantes a partir del CSV archivo.
        Si n es None, la lista es contiene todos los Participantes de archivo
    '''
    import csv
    participantes:list[Participante] = []
    f = open(archivo)
    for linea in csv.DictReader(f):
        
        #si n es un numero y la lista ya tiene n participantes,
        #interrumpe el ciclo y la devuelve
        if n != None and len(participantes) >= n:
            break
        
        #asigna todos los valores a variables individuales
        e:int = int(linea['edad'])
        h:bool = str_a_bool(linea['tieneHijos'])
        ch:int = int(linea['cantidadHijos'])
        g:int = int(linea['genero'])
        ne:int = int(linea['nivelEducativo'])
        r:int = int(linea['religiosidad'])
        pol:int = int(linea['conservadorProgresista'])
        id_p:int = int(linea['userId'])
        cor:int = sum(int(linea[f'{i}_correct']) for i in range(1, 13))
        
        #crea un participante con los atributos anteriores
        participante:Participante = Participante(e,h,ch,g,ne,r,pol,id_p,cor)
        
        #agrega el participante a la lista
        participantes.append(participante)
        
    f.close()
    return participantes
