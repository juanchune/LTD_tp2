from participante import Participante
from resumen import Resumen
from dataset import DataSet
import matplotlib.pyplot as plt

DT:DataSet = DataSet('rmet.csv')

promedios: list[float]  = []
errores: list[float] = []
edades: list[int] = []

for edad in range(100):
    parts:list[Participante] = DT.participantes_en_rango_etario(edad, edad)
    if len(parts) > 25:
        resumen_de_edad:Resumen = Resumen(parts)
        promedios.append(resumen_de_edad.correctas[0])
        errores.append(resumen_de_edad.correctas[1]/len(resumen_de_edad)**0.5)
        edades.append(edad)
    
# Gráfico
plt.figure(figsize=(10, 6))

plt.errorbar(
    edades,
    promedios,
    errores,
    fmt="o-",
    capsize=3
)

plt.xlabel("Edad", fontsize=18)
plt.ylabel("Desempeño promedio", fontsize=18)
plt.title("Correctas promedio por edad", fontsize=18)
plt.grid(True, alpha=0.3)
plt.show()
