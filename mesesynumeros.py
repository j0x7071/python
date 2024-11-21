
""""
    El programa debe recibir un numero
    
    Debe indicar a que mes del año pertenece

    Si no existe un mes relacionado al numero indicarlo

"""

nm= int(input("ingrese un número para saber a que mes del año corresponde: "))

while ( nm < 0 or nm > 12) :
    print("¡VALOR INCORRECTO!")
    print("Debe elegir un número entero mayor a 0 y menor a 13")

    nm= int(input("ingrese el numero de mes: "))
    
if (nm == 1) :
    print("El ",nm,"° mes del año es enero")
elif ( nm == 2) :
    print("El ",nm,"° mes del año es febrero")
elif ( nm == 3) :
    print("El ",nm,"° mes del año es marzo")
elif ( nm == 4) :
    print("El ",nm,"° mes del año es abril")
elif ( nm == 5) :
    print("El ",nm,"° mes del año es mayo")
elif ( nm == 6) :
    print("El ",nm,"° mes del año es junio")
elif ( nm == 7) :
    print("El ",nm,"° mes del año es julio")
elif ( nm == 8) :
    print("El ",nm,"° mes del año es agosto")
elif ( nm == 9) :
    print("El ",nm,"° mes del año es septiembre")
elif ( nm == 10) :
    print("El ",nm,"° mes del año es octubre")
elif ( nm == 11) :
    print("El ",nm,"° mes del año es noviembre")
else :
    print("El ",nm,"° mes del año es diciembre")
  
