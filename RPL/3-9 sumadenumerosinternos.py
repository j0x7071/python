def sumar_caracteres_numericos(cadena):
    suma=0
    for caracter in cadena:
        if caracter in "123456789":
            suma=suma+int(caracter)
    return suma

def main():
    print(sumar_caracteres_numericos("a1"))
main()