"""
Programa que debe convertir de Celcius a Frenheit y viceversa
"""

esc=int(input("Opcion 1 ) de FAHRENHEIT a CELSIUS Opcion 2 ) de CELSIUS a FAHRENHEIT: "))
while(esc<1 or esc>2) :
    print("Opcion incorrecta. Intente nuevamente.")
    esc=int(input("Opcion 1 ) de FAHRENHEIT a CELSIUS Opcion 2 ) de CELSIUS a FAHRENHEIT: "))


temp=int(input("Ingrese la temperatura: "))

if (esc==1):
    tempfinal = (temp - 32)*5/9
    print("Su temperatura en celcius es: ",tempfinal)
else :
    tempfinal = (temp * 9/5) + 32
    print("Su temperatura en fahrenheit es: ",tempfinal)
