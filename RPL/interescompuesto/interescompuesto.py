def interes_compuesto(capital_inicial, tiempo_de_inversion, porcentaje_de_rentabilidad):
    
    porcentaje=0
    #while capital_inicial<0:
    #    capital_inicial=int(input("Debe elegir un valor positivo para invertir"))
    
    #while tiempo_de_inversion<0:
    #    tiempo_de_inversion=int(input("Debe elegir un valor positivo para el tiempo en años años"))

    #while porcentaje_de_rentabilidad<0:
    #    porcentaje_de_rentabilidad=int(input("Debe elegir un valor positivo para el porcentaje de rentabilidad"))
        
    for i in range (tiempo_de_inversion):
        
        porcentaje =((capital_inicial/100)*porcentaje_de_rentabilidad )

        #print("AÑO N°", i+1," CAPITAL INICIAL:$",capital_inicial," - INTERESES:", porcentaje_de_rentabilidad ,"% - CAPITAL FINAL: $",capital_inicial+porcentaje)

        capital_inicial = capital_inicial + porcentaje
        
    capital_final=capital_inicial
    return capital_final
    pass

cap=float(input("Ingrese el capitál inicial: "))

tiempo=int(input("Ingrese el tiempo de inversion en años: "))

porc=float(input("Ingrese porcentaje de rentabilidad: "))

print(interes_compuesto(cap,tiempo,porc))
