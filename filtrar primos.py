def filtrar_primos (numeros, menor_numero):
    lista=[]
    for numero in numeros:
        if numero> menor_numero:
            lista.append(numero)
    return lista




def main():
    numeros=[2,3,5,7,11,13,17,19,23,29,31,37]
    menor_numero=int(input("Ingrese un numero para filtrar"))
    lista=filtrar_primos(numeros, menor_numero)
    print(lista)
main()
