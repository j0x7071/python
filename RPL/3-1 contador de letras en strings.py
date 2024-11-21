def longitud_cadenas(cadena_1, cadena_2, cadena_3):
    
    suma=len(cadena_1)+len(cadena_2)+len(cadena_3)
    return suma
    

def main():
    x="hola"
    y="como"
    z="estas"
    print(longitud_cadenas(x,y,z))

main()