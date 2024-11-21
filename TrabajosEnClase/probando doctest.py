import doctest

def validacion_numeros (tablero,opcion,test=False) :
    
    """
    >>> validacion_numeros([['A', False], ['Ab', False], ['B', False], ['Bb', False], ['C', False], ['Cb', False], ['D', False], ['Db', False]], 4, test=False)
    True
    
    >>> validacion_numeros([['A', False], ['Ab', False], ['B', False], ['Bb', False], ['C', False], ['Cb', False], ['D', False], ['Db', False]], "g", test=False)
    False
    >>> validacion_numeros([['A', False], ['Ab', False], ['B', False], ['Bb', False]], -15, test=False)
    False
    """
    
    
    valido = False
    while not valido :
            try  :
                #Si el número no corresponde a una posicion
                if  opcion > int(len(tablero))  or opcion <= 0  :
                    print ("\nEL numero no corresponde a una ficha")
                #Si el número pertenece a una ficha que ya fue seleccionada o adivinada. 
                elif tablero[(opcion)-1][1]==True:
                    print("\nEL numero ya no esta disponible")
                else :
                    valido=True
            #Si se trata de un caracter no numérico
            except : 
                print ( "\nNo se trata de un valor numerico")
    return valido

def main():
    print(validacion_numeros([['A', False], ['Ab', False], ['B', False], ['Bb', False], ['C', False], ['Cb', False], ['D', False], ['Db', False]], 4, test=False))
    doctest.testmod()

main()