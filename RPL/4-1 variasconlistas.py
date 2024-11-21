import doctest

def filtrar_pares(lista):
    pares=[]
    for element in lista:
        if element%2==0:
            pares.append(element)
    return pares

def filtrar_primos(lista):
    filtro=[]
    
    for numero in lista:
        filtro.append(numero)
        for i in range(2,numero):
            if 1<numero and numero%i==0 and numero in filtro:
                filtro.remove(numero)
        if numero==0 or numero==1:
            filtro.remove(numero)
    return filtro 
    


def sumar_elementos(lista):
    suma=0
    for numero in lista:
        suma=suma+numero
    return suma


def esta_ordenada(lista):
    bandera=True
    contador=0
    for i in lista:
        if contador<=i:
            contador=i
        else:
            bandera=False
    return bandera
    

def producto_escalar(vector_1, vector_2):
    producto_punto=0

    for i in range(0,len(vector_1)):
        producto_punto=producto_punto+vector_1[i]*vector_2[i]    
    return producto_punto
    

def letras_en_palabra(letras, frase):
    bandera=False
    lista=[]
    contador=0
    for letra in frase:
        for i in letras:
            if letra==i and letra not in lista:
                contador+=1
                lista.append(letra)
    
    if contador==len(letras):
        bandera=True
    return bandera

def main():
    print(letras_en_palabra(["9","u"],"rt a sueyu'9'¿25¿93250"))
main()