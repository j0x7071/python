"""
El diccionario "materias" tiene cargadas asignaturas como clave y una lista con tres números enteros: 
- cantidad de alumnos anotados (primer valor),
- cantidad de alumnos que regularizaron la materia (segundo valor),
- cantidad de alumnos que abandonaron: nunca rindieron el parcial en ninguna instancia (tercer valor).

 Se pide que hagas un programa en Python que:

Indique, sin listar los nombres de las materias, si hubo una o más materias en donde los recursantes (anotados – regularizaron) superen el 40% del total de los estudiantes anotados.
Liste de mayor a menor las materias teniendo en cuenta la cantidad de alumnos que desaprobaron (no computar a los que abandonaron).

Indicando

materia - cantidad desaprobados
"""
def obtener_diccionario():
    materias = {}
    materias["AM II"] = [2300, 1800, 250]
    materias["Algebra"] = [2100, 1300, 325]
    materias["Algoritmos I"] = [500, 220, 160]
    materias["Algoritmos II"] = [640, 200, 150]
    materias["Fisica"] = [1600, 900, 600]
    materias["Quimica"] = [950, 420, 380]
    materias["Computacion"] = [800, 330, 310]
    
    return materias

def superaron(materias):
    ANOTADOS=0
    REGULARES=1
    
    cantidad=0
    
    for key in materias.items():
        #40% de la materia = margen
        margen=(key[1][ANOTADOS]*40)/100
        
        if (key[1][REGULARES]>margen):
            cantidad+=1
    #Mensajes a presentar
    if cantidad>1:
        print("En",cantidad,"materias los alumnos regulares superaron el 40% de alumnos totales anotados")
        
    elif cantidad==1:
        print("Solo en una materia los alumnos regulares superaron el 40% de alumnos totales anotados")
    
    pass

def desaprobaron(materias):
    ANOTADOS=0
    REGULARES=1
    INACTIVOS=2
    
    lista=[]
    
    for key in materias.items():
        
        rindieron=key[1][ANOTADOS]-key[1][INACTIVOS]
        
        desaprobaron=rindieron-key[1][REGULARES]
        
        lista+=[[desaprobaron,key[0]]]
    
    lista=sorted(lista,reverse=True)
    for i in lista:
        print("Materia:", i[1]," - Cantidad de desaprobados: ",i[0])
    
    return lista

def main():
    materias=obtener_diccionario()
    superaron(materias)
    desaprobaron(materias)
    
main()