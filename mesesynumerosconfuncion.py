def numero_de_mes(nm):
        while ( nm < 0 or nm > 12) :
            nm=int(input("¡VALOR INCORRECTO! Debe elegir un número entero mayor a 0 y menor a 13: "))
        if (nm == 1) :
            valor='El 1° mes del año es enero'
        elif ( nm == 2) :
            valor='El 1° mes del año es febrero'
        elif ( nm == 3) :
            valor='El 3° mes del año es marzo'
        elif ( nm == 4) :
            valor='El 4° mes del año es abril'
        elif ( nm == 5) :
            valor='El 5° mes del año es mayo'
        elif ( nm == 6) :
            valor='El 6° mes del año es junio'
        elif ( nm == 7) :
            valor='El 7° mes del año es julio'
        elif ( nm == 8) :
            valor='El 8° mes del año es agosto'
        elif ( nm == 9) :
            valor='El 9° mes del año es septiembre'
        elif ( nm == 10) :
            valor='El 10° mes del año es octubre'
        elif ( nm == 11) :
            valor='El 11° mes del año es noviembre'
        else :
            valor='El 12° mes del año es diciembre'
        return valor 

print(numero_de_mes(int(input("Ingrese un numero: "))))


  
