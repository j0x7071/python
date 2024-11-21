def palabra_mas_larga(texto):
    texto=texto+" "
    s1=""
    s2=""
    contador_1=0
    contador_2=0
    palabra_mas_larga=""
    bandera=False
    
    for caracter in texto:
        if bandera==False:
            print("Soy el caracter del for bi bandera falsa==>",caracter)
            s1+=caracter
            print("Asi va el string 1==>",s1)
            contador_1=contador_1+1
            print("Soy el primer contador===>",contador_1)
            if caracter==" ":
                s1=s1[:-1]
                print("Hubo un espacio! lo dejo asi al s1===>",s1)
                bandera=True
                palabra_mas_larga=s1
        
        if bandera==True:
            print("Soy el caracter del for vi bandera abrida==>",caracter)
            s2+=caracter
            print("Asi va el S2====>",s2)
            contador_2=contador_2+1
            if caracter==" " and contador_2>1:
                print("Yo lleve la cuenta, y encontre espacio, soy contador 2===>",contador_2)
                s2=s2[1:-1]
                if contador_2>contador_1:
                    print("Ex palabra mas larga===>",palabra_mas_larga)
                    palabra_mas_larga=s2
                    print("Esta vez fui mas grande tomo lugar a la palabra mas larga",)
                    s2=""
                    s1=""
                    contador_1=0
                    contador2=0
                    bandera=False
                    print("SE REINICIA WEY")
                    print("Palabra mas larga==>")
    return palabra_mas_larga        
    

def main():
    print(palabra_mas_larga("Hola como estas este es un texto de prueba"))
    
main()