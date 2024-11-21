def main():
    seguir="s"
    diccionario={}
    lista=[]
    while seguir=="s":
        partido=str(input("Ingrese el partido a sumarle votos: "))
        votos=int(input("Ingrese la cantidad de votos a sumarle: "))
        if partido not in diccionario:
            diccionario[partido]=votos
        else:
            diccionario[partido]+=votos
        seguir=str(input("Desea seguir ingesando?(s/n): "))

    for i in diccionario:
        lista+=[[i,diccionario[i]]]
    
    lista=sorted(lista, key=lambda x:x[1], reverse=True)
    print(lista)
    for i in range(0,len(lista)):
        print("El partido",lista[i][0],"obtuvo",lista[i][1])
    
main()
