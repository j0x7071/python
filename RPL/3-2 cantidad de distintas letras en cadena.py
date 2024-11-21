def contar_caracteres(cadena, caracter_1, caracter_2):
    contador=0
    for caracter in cadena:
        print(caracter)
        if caracter==caracter_1 or caracter==caracter_2 in cadena:
            print("entre")
            contador+=1
    return contador

def main():
    cadena='algoritmos'
    c='o'
    a='a'
    print("salio?",contar_caracteres(cadena,c,a))


main()