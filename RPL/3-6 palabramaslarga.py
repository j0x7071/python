def palabra_mas_larga(texto):
    texto=texto+" "
    palabra=""
    contador_1=0
    contador_2=0
    palabra_mas_larga=""

    for caracter in texto:
        palabra+=caracter
        contador_1=contador_1+1
        if caracter==" ":
            palabra=palabra[:-1]
            if contador_1>=contador_2:
                    palabra_mas_larga=palabra
                    contador_2=contador_1
                    contador_1=0
                    palabra=""
            else:
                contador_1=0
                palabra=""
    return palabra_mas_larga        
    

def main():
     print(palabra_mas_larga("Hola como estas este es un texto de prueba") )
main()