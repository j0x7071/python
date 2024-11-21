def filtrador_de_vocales(cadena):
    palabra_sin_vocales=""
    for caracter in cadena:
        if caracter not in ["a","e","i","o","u"]:
            palabra_sin_vocales+=caracter
            
    return palabra_sin_vocales

def main():
    print(filtrador_de_vocales("algoritmos"))
main()