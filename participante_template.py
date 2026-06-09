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
            self.nivel_edu:str = 'primario incompleto'
        elif ne == 2:
            self.nivel_edu:str = 'primario completo'
        elif ne == 3:
            self.nivel_edu:str = 'secundario completo'
        elif ne == 4:
            self.nivel_edu:str = 'terciario incompleto'
        elif ne == 5:
            self.nivel_edu:str = 'terciario completo'
        elif ne == 6:
            self.nivel_edu:str = 'posgrado completo'
        
        self.politica:int = pol
        self.religion:int = r
        self.id:int = id_p
        self.correctas:int = cor

    def __repr__(self) -> str:
        '''Devuelve: una representacion en string de participante'''
        return 'Genero: ' + self.genero + ', NE: ' + self.nivel_edu + ', Edad: ' + str(self.edad) + ', Correctas: ' + str(self.correctas) + ', ID: ' + str(self.id)
    
    def __eq__(self, other) -> bool:
        '''Devuelve:True si p1 y p2 tienen misma edad y misma cantidad de 
                    respuestas correctas, y False en caso contrario.'''
        return self.edad == other.edad and self.correctas == other.correctas