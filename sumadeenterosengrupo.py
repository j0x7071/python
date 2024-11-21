"""
Escribir una función que reciba un valor n, entero, y devuelva la suma de los
valores entre 0 y n.
"""
def suma_enteros(num):
    suma=0
    for i in range(num+1):
        
        suma += i
        
        return suma

x=int(input("Ingrese un numero entero"))

print("la suma de los numeros es",suma_enteros(x))    

