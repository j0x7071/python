def quien_gano():
    equipo1=input("Ingrese equipo local: ")
    goles_local=int(input("Ingrese goles equipo local: "))
    equipo2=input("Ingrese equipo visitante: ")
    goles_visitante=int(input("Ingrese goles equipo visitante: "))
    if goles_local > goles_visitante:
            ganador=equipo1
    elif (goles_local < goles_visitante):
            ganador=equipo2
    else :
        ganador="Empate"
    return ganador

def main():
    print(quien_gano())

main()
