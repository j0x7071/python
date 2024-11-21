def numeros_positivos(numero):
    positivos=[x for x in range(1,numero+1)]
    return positivos
    
def numeros_positivos_pares(numero):
    pares=[x for x in range(1,numero+1) if x%2==0]
    return pares


def numeros_positivos_pares_cuadrado(numero):
    pares=[x**2 for x in range(1,numero+1) if x%2==0]
    return pares

def impares_al_cuadrado(lista):
    modificados=[x**2 if (x%2!=0) else x for x in lista]
    return modificados

def filtrar_tuplas_por_suma(lista_de_tuplas):
    positivas=[x for x in lista_de_tuplas if x[1]+x[0]>=0]
    return positivas
    
def filtrar_tupla_elemento_par(lista_de_tuplas):
    con_pares=[x for x in lista_de_tuplas if x[1]%2==0 or x[0]%2==0]
    return con_pares
    

def main():
    #print(numeros_positivos_pares_cuadrado(7))
    print(filtrar_tupla_elemento_par([(7, -5), (4, 5), (1, 2), (1, -3), (4, 2)]))
    #=> [(7, -5),(1, 2)]
    print(impares_al_cuadrado([1,2,3,4,5,6,7]))    
main()