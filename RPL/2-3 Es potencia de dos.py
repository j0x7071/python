def es_potencia_de_dos(numero):
    resultado=False
    numero=numero*2
    while numero >= 2:
        numero = numero/2
        if numero == 1:
            resultado = True
    return resultado

def main():
    x=int(input("num="))
    print(es_potencia_de_dos(x))

main()
