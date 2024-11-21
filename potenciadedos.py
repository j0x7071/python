def potencia_de_dos(x) :
    y=x
    for i in range (x):
        y=y/2
        if(y==1):
            return "true"
        elif(y<1):
            return "false"
        
    pass    

x=int(input("Ingreze el numero a saber si es potencia de 2"))

print(potencia_de_dos(x))
