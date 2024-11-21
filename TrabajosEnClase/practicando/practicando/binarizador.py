def binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        #print(decimal,"!=2")
        binario = str(decimal % 2) + binario
        #print(binario, "<== binario")
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input("Numero a binarizar: "))
print(binario(numero))
