#seleccion (selection sort)

def seleccion(l):
    n= len(l)
    for i in range(n):
        #Asumimos que el minimo está en la posicion i
        min=i
        
        #recorremos el resto de la lista
        for j in range(i+1,n):
            if (l[j] < l[min]):
                #Si encontramos un nuevo minimo, actualiza posicion
                min=j
            #Llevamos el minimo a la posicion i
        l[i], l[min] = l[min],l[i]
    return l

lista=[4,2,3,5,1]

print(seleccion(lista))