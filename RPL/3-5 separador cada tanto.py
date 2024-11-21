def insertar_separadores(cadena, separador, espaciado):
    cadena_nueva=""
    contador=0
    for i in cadena:        
        cadena_nueva+=i
        contador+=1
        if contador%espaciado==0:
            cadena_nueva+=separador
            print(cadena_nueva)
    if cadena_nueva[-1]==separador:
        cadena_nueva=cadena_nueva[:-1]
    return cadena_nueva
        
        
def main():
    print(insertar_separadores("holacomoestas", "|", 4))
    print(insertar_separadores("255255255255", ".", 3))
main()