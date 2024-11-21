def ordenar_lista_menor_a_mayor(lista):
    lista=sorted(lista)
    return lista
    

def ordenar_lista_mayor_a_menor(lista):
    lista[::-1]=sorted(lista)
    return lista
    

def ordenar_lista_alfabeticamente(lista):
    lista=sorted(lista)
    return lista

def ordenar_palabras_por_longitud(lista):
    lista_ordenada=sorted(lista, key=len, reverse=True)
    return lista_ordenada
    
def ordenar_lista_por_tupla(lista):
    lista.sort(key = lambda x: x[1],reverse=True)
    return lista

def ordenar_lista_por_suma_tupla(lista):
    lista.sort(key = lambda x: x[0]+x[1],reverse=True)
    return lista

def main():
    #print(ordenar_palabras_por_longitud(['fewr','rtg retgr','rerevteryv','yrevtv',]))
    print(ordenar_lista_por_suma_tupla([(1, 5), (7, 3), (5, 4), (4, 3)]))
main()