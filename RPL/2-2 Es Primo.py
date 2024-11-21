def suma_de_numeros_primos(numero):
    esprimo = True
    total=0
    if numero==1 or numero==0:
        esprimo=False
    else:
        for i in range (2,numero+1):
            print("valor de i en el for:",i)
            print("valor de nuero en for",numero)
            print("Valor total antes del if",total)
            if numero%i!=0:
                total=total+i
            print("valor total despues del if",total)
            i+=1
    return total
    
def main():
    print(suma_de_numeros_primos(int(input("numero"))))
    
main()

