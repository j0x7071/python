#Elaborado en Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06)
print("introduzca el numero")
numero = int(input()) #aquí se lee el número entero

total=0
divisores=[]
print("los divisores de ",numero)
for divisor in range(2,numero-1):
    if (numero % divisor) == 0 :
        print(divisor,"es divisor")
        divisores.append(divisor)
        total=total+divisor
        
print("el numero ",numero," tiene  divisores")
print(divisores)
print("La suma de sus divisores es", total)