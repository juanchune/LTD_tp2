from participante import Participante
from participante import str_a_bool
from participante import crear_lista_participantes

def test_atributos():
    p1:Participante=Participante(25, 1, 3, 1, 5, 85, 56, 3, 8)
    assert p1.edad==25
    assert p1.tiene_hijos==True
    assert p1.cant_hijos==3
    assert p1.genero=='Varon'
    assert p1.nivel=='terciario completo'
    assert p1.religion==85
    assert p1.politica==56
    assert p1.id==3
    assert p1.correctas==8
    
    p2:Participante=Participante(29, 0, -999, 2, 3, 2, 66, 5464, 12)
    assert p2.edad==29
    assert p2.tiene_hijos==False
    assert p2.cant_hijos==0
    assert p2.genero=='Mujer'
    assert p2.nivel=='secundario completo'
    assert p2.religion==2
    assert p2.politica==66
    assert p2.id==5464
    assert p2.correctas==12
    

def test_repr():
    p1:Participante=Participante(25, 1, 3, 1, 5, 85, 56, 3, 8)
    p2:Participante=Participante(29, 0, -999, 2, 3, 2, 66, 5464, 12)
    assert str(p1)=='Genero: Varon, NE: terciario completo, Edad: 25, Correctas: 8, ID: 3'
    assert str(p2)=='Genero: Mujer, NE: secundario completo, Edad: 29, Correctas: 12, ID: 5464'
    
    
def test_eq():
    p1:Participante=Participante(25, 1, 3, 1, 5, 85, 56, 3, 8)
    p2:Participante=Participante(29, 0, -999, 2, 3, 2, 66, 5464, 12)
    p3:Participante=Participante(25, 0, -999, 2, 8, 5, 96, 8685, 8)
    assert not p1==p2
    assert p1==p3


def test_str_a_bool():
    assert str_a_bool('0') == False
    assert str_a_bool('1') == True


def test_lista_participantes():
    p1:list[Participante]=crear_lista_participantes('rmet.csv', 2)
    p2:list[Participante]=crear_lista_participantes('rmet.csv', 0)
    assert str(p1)== '[Genero: Varon, NE: posgrado completo, Edad: 26, Correctas: 8, ID: 1, Genero: Varon, NE: terciario completo, Edad: 26, Correctas: 9, ID: 2]'
    assert str(p2)== '[]'
    
    
    

test_atributos()
test_repr()
test_eq()
test_str_a_bool()
test_lista_participantes()