import pandas as pd


datos = pd.read_csv("sueldos.csv", index_col = "legajo")
#NUEVA COLUMNA EN BASE A VARIAS
def calcular_sueldo(fila):
    sueldo = fila["hs_trabajadas"] * fila["valor_hora"]
    return sueldo

datos["sueldo_bruto"] = datos.apply(calcular_sueldo, axis = 1)
print(datos)


#AGRUPAR
#Por promedio:
print(datos.groupby("categoria").mean())

#Por suma:
print(datos.groupby("categoria").sum())


#AGRUPACIÓN DISTINTA X COLUMNA
print(datos.groupby("categoria").agg({
    "hs_trabajadas" : "sum",
    "valor_hora" : "mean"
    }))



#PARA GRAFICAR:
import matplotlib.pyplot as plt

agrupado = datos.groupby("categoria").agg({
    "hs_trabajadas" : "sum",
    "valor_hora" : "mean"
    })

#Con líneas:
agrupado["hs_trabajadas"].plot()
plt.show()

#Con barras:
agrupado["hs_trabajadas"].plot(kind = "bar")
plt.show()


#Eje x y eje y:
datos.plot(kind = "scatter", x = "hs_trabajadas", y = "valor_hora")
plt.show()





