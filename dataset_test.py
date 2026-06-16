from dataset import DataSet
import os


def test_atributos():
    d1:DataSet=DataSet('rmet_test.csv')
    
    assert len(d1.participantes) > 1 #comprueba que se cargaron los participantes
    
    assert 'primario incompleto' in d1.niveles
    assert 'primario completo' in d1.niveles
    assert 'secundario completo' in d1.niveles
    assert 'terciario incompleto' in d1.niveles
    assert 'terciario completo' in d1.niveles
    assert 'posgrado completo' in d1.niveles

def test_len():
    d1:DataSet=DataSet('rmet_test.csv')
    assert len(d1.participantes) == 27
    assert len(d1.participantes) == len(d1)
    

def test_participantes_rango_etario():
    d1:DataSet=DataSet('rmet_test.csv')
    assert len(d1.participantes_en_rango_etario(20, 30)) == 15
    
    r1:list[d1.Participante]= d1.participantes_en_rango_etario(86,88)
    assert str(r1)== '[Genero: Varon, NE: posgrado completo, Edad: 86, Correctas: 9, ID: 12]'
    #ejemplo específico
    
    r2= d1.participantes_en_rango_etario(20, 30)
    for par in r2:
        assert 20 <= par.edad <= 30  #todos los devueltos deben tener edad dentro del rango
    
    r3 = d1.participantes_en_rango_etario(26, 26)
    for par in r3:
        assert par.edad == 26
    #los extremos deben estar incluidos
    
    r4 = d1.participantes_en_rango_etario(200, 300)
    assert r4 == []
    #rango donde no hay nadie
    
    
def test_resumenesNE():
    d1:DataSet=DataSet('rmet_test.csv')
    r1= d1.resumenes_NE()
    assert set(r1.keys())== d1.niveles
    
    for clave in r1:
        assert clave == str(clave) #las claves deben ser string
    
    for nivel, resumen in r1.items():
        assert resumen.cantidad >= 2 
    #Sólo se incluirá como clave un NE si existen dos o más participantes con ese NE.
    
    assert r1['terciario completo'].cantidad == 10
    assert r1['posgrado completo'].cantidad == 6
    assert r1['primario completo'].cantidad == 2
    
def test_participantes_mayores_notas():
    d1:DataSet=DataSet('rmet_test.csv')
    r1 = d1.participantes_mayores_notas('primario incompleto')
    assert len(r1) == 1
    r2 = d1.participantes_mayores_notas('primario completo')
    assert len(r2) == 1
    r3 = d1.participantes_mayores_notas('secundario completo')
    assert len(r3) == 2
    r4 = d1.participantes_mayores_notas('terciario incompleto')
    assert len(r4) == 2
    r5 = d1.participantes_mayores_notas('terciario completo')
    assert len(r5) == 5
    r6 = d1.participantes_mayores_notas('posgrado completo')
    assert len(r6) == 3
    
    r7 = d1.participantes_mayores_notas('posgrado completo')
    for par in r7:
        assert par.nivel == 'posgrado completo'

def test_exportar_edad():
    d1:DataSet=DataSet('rmet_test.csv')
    d1.exportar_por_edad('test_salida.csv', 25, 30)
    
    f = open('test_salida.csv')
    lineas = f.readlines()
    f.close()
    
    # el archivo no está vacío y tiene 1 encabezado + 6 edades
    assert lineas != []
    assert len(lineas) == 7
    
    # encabezado correcto
    assert lineas[0].strip() == 'edad,cantidad_participantes,promedio_correctas,promedio_religiosidad,promedio_politica'
       
    # valores concretos de las primeras dos filas
    edad25 = lineas[1].strip().split(',')
    assert edad25[1] == '3'
    assert edad25[2] == '5.67'
    
    edad26 = lineas[2].strip().split(',')
    assert edad26[1] == '6'
    assert edad26[2] == '7.17'
    
    os.remove('test_salida.csv')

test_atributos()
test_len()
test_participantes_rango_etario()
test_resumenesNE()
test_participantes_mayores_notas()
test_exportar_edad()
