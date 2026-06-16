from resumen import Resumen
from resumen import promedio
from resumen import desvioestandar
from participante import Participante
from participante import crear_lista_participantes

def test_atributos():
    l1:list[Participante]= crear_lista_participantes('rmet_test.csv',2)
    r1:Resumen=Resumen(l1)
    assert r1.correctas == (8.5, 0.71)
    assert r1.edad == (26.0, 0.0)
    assert r1.politica== (65.0,28.28) 
    assert r1.religiosidad==(12.0, 16.97)
    
    l2:list[Participante]=crear_lista_participantes('rmet_test.csv',5)
    r2:Resumen=Resumen(l2)
    assert r2.correctas == (8.8, 0.84)
    assert r2.edad == (27.0, 5.48)
    assert r2.politica== (76.6, 21.2) 
    assert r2.religiosidad==(13.2, 18.62)
    
    l3:list[Participante]=(crear_lista_participantes('rmet_test.csv',10)[5:9])
    r3:Resumen=Resumen(l3)
    assert r3.correctas == (8.0, 2.16)
    assert r3.edad == (34.0, 9.42)
    assert r3.politica== (90.75, 15.95) 
    assert r3.religiosidad==(27.5, 32.93)
    
def test_len():
    l1:list[Participante]= crear_lista_participantes('rmet_test.csv',2)
    r1:Resumen=Resumen(l1)
    assert len(r1)==2
    
    l2:list[Participante]=crear_lista_participantes('rmet_test.csv',5)
    r2:Resumen=Resumen(l2)
    assert len(r2)==5
    
    l3:list[Participante]=(crear_lista_participantes('rmet_test.csv',10)[5:9])
    r3:Resumen=Resumen(l3)
    assert len(r3)==4


def test_repr():
    l1:list[Participante]= crear_lista_participantes('rmet_test.csv',2)
    r1=Resumen(l1)
    assert str(r1.participantes)== '[Genero: Varon, NE: posgrado completo, Edad: 26, Correctas: 8, ID: 1, Genero: Varon, NE: terciario completo, Edad: 26, Correctas: 9, ID: 2]'
    
    
def test_eq():
    l1:list[Participante]= crear_lista_participantes('rmet_test.csv',2)
    r1=Resumen(l1)
    l2:list[Participante]=crear_lista_participantes('rmet_test.csv',5)
    r2:Resumen=Resumen(l2)
    l3:list[Participante]=crear_lista_participantes('rmet_test.csv',2)
    r3:Resumen=Resumen(l3)
    assert not r1==r2
    assert r1==r3


def test_promedio():
    assert abs(promedio([1, 2, 3, 4, 5]) - 3.0) <= 0.001
    assert abs(promedio([10, 20]) - 15.0) <= 0.001
    
    
def test_desvioestandar():
    assert abs(desvioestandar([1, 2, 3]) - 1.0) <= 0.001
    assert abs(desvioestandar([10, 20]) - 7.07) <= 0.001
    
test_atributos()
test_len()
test_repr()
test_eq()
test_desvioestandar()
test_promedio()