import doctest

def validar_password(password)
    valida=False
    while valida==False:
        if 8<= len(password) <= 12 and isalpha(password) and islower(password)
            contraseña=password
            valida=True
    return valida
def main():
    contraseña=none
    validar_password(input("Elija una contraseña"))



doctest.testmod()

