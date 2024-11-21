nota=int(input("Ingrese nota o 0 para terminar: "))
base=0
contador=0
while nota>0 :
    contador +=1
    base=nota+base
    nota=int(input("Ingrese nota o 0 para terminar: "))
    
promedio=base/contador
print(promedio)

    
