def ordenar_por_longitud_de_tuplas(tuplas):
    
    lista_listas = [list(tupla) for tupla in tuplas ]
    
    lista_listas.sort(key=lambda e:len(e), reverse=True)
    print(lista_listas)
    lista_listas = [tuple(lista) for lista in lista_listas ]
    return lista_listas

        
        


def main():
    tuplas=[(1,5,6), (1,2), (1,), (6,4,), ("asd", 9, 5.6, "l", "s"), (3,3,4), (2,2), ("aaaa","bbbb")]
    print(ordenar_por_longitud_de_tuplas(tuplas))

main()
