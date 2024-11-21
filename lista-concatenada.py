def concatenar_primeros_elementos(lista):
    lista_concatenada = []
    for i in lista:
        print(i)
        lista_concatenada.append(i[0])
        lista_concatenada.append(i[1])
    return lista_concatenada

def main():
    lista = [[1,4,5,6], [2,3,4,5], [6,4,4,6,7,8], [5,6,7,3,5,6,4]]
    print(concatenar_primeros_elementos(lista))

main()
