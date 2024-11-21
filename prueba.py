def es_potencia_de_dos(numero):
    if 2**numero%numero==0:
        return True
    else:
        return False

numero=int(input("Ingrese numero"))
print(es_potencia_de_dos(numero))
