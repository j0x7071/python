def numeros_al_cuadrado(numero):
    diccionario={}
    for i in range(1,numero+1):
        diccionario[i]=i**2
    return diccionario

def mezclar_diccionarios(dicc_uno, dicc_dos):
    dicc_tres={}
    for i in dicc_uno:
        dicc_tres[i]=dicc_uno[i]
    for i in dicc_dos:
        dicc_tres[i]=dicc_dos[i]
    return dicc_tres

def filtrar_por_sumar_diez(diccionario):
    diccionario_dos={}
    for i in diccionario:
        if i+diccionario[i]>=10:
            diccionario_dos[i]=diccionario[i]
    return diccionario_dos

def ordenar_valores_por_longitud(diccionario):
    lista=sorted([diccionario[x] for x in diccionario], key=len, reverse=True)
    return lista
        

def main():
    #dic1={'clave1':1,'clave3':3}
    #dic2={'clave2':2,'clave4':4}
    diccionario={8:3,9:3,5:2,6:8,1:3,4:5,2:9}
    dicstrings={'hola':'pablo','gonza':'hermanos','daropoopo':'azul'}

    print(numeros_al_cuadrado(7))
    #print(mezclar_diccionarios(dic1,dic2))
    #print(filtrar_por_sumar_diez(diccionario))
    #print(ordenar_valores_por_longitud(dicstrings))
main()
