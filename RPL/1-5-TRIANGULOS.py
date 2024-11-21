# tu codigo
a=int(input("Ingrese la longitud del primer lado del triangulo: "))
b=int(input("Ingrese la longitud del segundo lado del triangulo: "))
c=int(input("Ingrese la longitud del tercer lado del triangulo: "))
if a == b and b == c :
    print("Es equilatero")
elif a != b and b!= c and a!= c :
    print("Es escaleno")
else :
    print("Es isosceles")
