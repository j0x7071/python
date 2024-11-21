def validar_contrasenia(contrasenia):
    valida=False
    prueba1=False
    prueba2=False
    prueba3=False
    prueba4=False
    if 7<len(contrasenia)<15:
        prueba1=True
    for caracter in contrasenia:
        if caracter.isnumeric():
            prueba2=True
        if caracter.isupper():
            prueba3=True
        if not caracter.isalpha() and not caracter.isnumeric():
            prueba4=True
    if prueba1 and prueba2 and prueba3 and prueba4:
        valida=True
    return valida
def main():
    print(validar_contrasenia("!!-.00i12"))

main()