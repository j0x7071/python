

import pandas as pd
import matplotlib.pyplot as plt


datos = pd.read_csv("sueldos.csv", index_col = "legajo")
print("Antes del aumento")
print(datos[["categoria", "hs_trabajadas", "valor_hora"]])

tabla = datos[["nombre", "categoria", "valor_hora"]]

datos_reducidos = datos.loc[[108, 105], ["nombre", "hs_trabajadas", "valor_hora"]]
#print(datos_reducidos)
#print(datos[datos["hs_trabajadas"] < 40])
#print(datos[(datos["hs_trabajadas"] >= 40) & (datos["valor_hora"] >= 2100)])
#

#print(datos[datos["categoria"] == "DESARROLLADOR"])

def aumentar_sueldo(valor):
    return 1.2 * valor


datos["valor_hora"] = datos["valor_hora"].apply(aumentar_sueldo)
##print("\nDespues del aumento")
##print(datos[["nombre", "hs_trabajadas", "valor_hora"]])




def calcular_sueldo(fila):
    sueldo = fila["hs_trabajadas"] * fila["valor_hora"]
    return sueldo
##

datos["sueldo_bruto"] = datos.apply(calcular_sueldo, axis = 1)
##print(datos[["nombre", "hs_trabajadas", "valor_hora", "sueldo_bruto"]])
##print(datos)



tabla = datos.groupby("categoria").mean()
print(tabla)


##tabla["hs_trabajadas"].plot(kind = "bar")
##

datos.plot(kind = "scatter", x = "hs_trabajadas", y = "sueldo_bruto")
##
plt.show()
##
