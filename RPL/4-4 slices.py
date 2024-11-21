def ultimos_tres_elementos(lista):
    lista=lista[-3:]
    return lista

def ultimos_tres_elementos_concatenados(lista):
    lista=[lista[x][-3:] for x in range(0,len(lista))]
    lista2=[]
    for x in lista:
        lista2+=x
    return lista2

def indices_pares(lista):
    return lista[0::2]
    

def indices_impares(lista):
    return lista[1::2]

def invertir(lista):
    return lista[::-1]

def main():
    print(indices_pares([3,45,6,7,8,4,6,43]))

    print(indices_impares([3,45,6,7,8,4,6,43]))

    print(invertir([3,45,6,7,8,4,6,43]))
main()
