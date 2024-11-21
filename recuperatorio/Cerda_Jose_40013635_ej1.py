import doctest

"""
Escribir una funcion en Python, para validar una nueva clave de acceso.

La función debera recibir una cadena de caracteres, que contendra la clave candidata, previamente ingresada por el usuario.
Devolvera true o false, dependiendo de si cumple o no con las siguientes condiciones:

- La clave debe estar formada unicamente por, entre 4 y 8 caracteres numericos
- El caracter '0', a lo sumo puede estar una vez

Ejemplos a validar usando doctest:

validar("j2020") devuevle false
validar("2021a") devuevle false
validar("20X21") devuevle false
validar("2220") devuelve true
validar("23445776") devuelve true
validar("089") devuelve false
validar("027845321") devuelve false
validar("02784532") devuelve true
validar("303330") devuelve false
"""
def validar(string):
    """
    >>> validar("j2020")
    False
    >>> validar("2021a")
    False
    >>> validar("20X21")
    False
    >>> validar("2220")
    True
    >>> validar("23445776")
    True
    >>> validar("089")
    False
    >>> validar("027845321")
    False
    >>> validar("02784532")
    True
    >>> validar("303330")
    False
    """
    valida=True
    
    numeros="1234567890"
    
    control_cero=string.count("0")
    
    #Controla la longitud de la cadena y el cero opcional
    if (len(string)>= 4 and len(string)<= 8) and (control_cero<=1):
        for caracter in string:
            #Controla que todos los caracteres sean numeros
            if (caracter not in numeros):
                valida=False
    else:
        valida=False
    
    return valida


def main ():
    doctest.testmod()
main()