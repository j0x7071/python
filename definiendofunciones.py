import doctest

def minimo(a,b):
    """
    >>> minimo(5,3)
    3
    >>> minimo(-5,3)
    -5
    >>> minimo(29,-8)
    -8
    >>> minimo(-23,15)
    -23
    """
    m=b
    if (a < b):
        m=a
    return m

def saludar_nombre(nombre):
    print("hola ",nombre)
"""
saludar_nombre('agustina')
saludar_nombre('mariano')
x= int(input("Ingrese un entero: "))
y= int(input("Ingrese otro entero: "))

print("El minimo entre ",x, " e ",y, " es: ",minimo(x,y))
"""

print(doctest.testmod())
