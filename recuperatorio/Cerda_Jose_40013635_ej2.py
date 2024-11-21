import doctest
"""
Escribi una función que devuelva verdadero si un alumno aprobó un curso virtual, o de lo contrario falso.
La función recibe dos listas: una de puntajes maximos por cada actividad y otra de puntajes otorgados por dicha actividad.
Para aprobar el curso se necesita que en cada actividad haya obtenido, por lo menos, un 60% del puntaje máximo.

Comproba el correcto funcionamiento, mediante los siguientes casos de prueba usando la librería doctest. 
Además, agrega DOS casos de prueba adicionales, en donde uno sea Falso y el otro Verdadero.

Casos de Prueba:

    >>> aprobo_cursada([10, 20, 15], [6, 15, 12])
    True
    >>> aprobo_cursada([10, 20, 15], [6, 8, 12])
    False
    >>> aprobo_cursada([10, 20, 15, 30],  [6, 12, 9, 12])
    True
"""

def aprobo_cursada(maximos,obtenidos):
    """
    >>> aprobo_cursada([10, 20, 15], [6, 15, 12])
    True
    >>> aprobo_cursada([10, 20, 15], [6, 8, 12])
    False
    >>> aprobo_cursada([10, 20, 15, 30],  [6, 12, 9, 12])
    False
    """
    aprueba=True
    for i in range(0,len(maximos)):
        if ((obtenidos[i]/maximos[i])*100<60.0):
            aprueba=False
    return aprueba
    
def main():
    doctest.testmod()
main()
