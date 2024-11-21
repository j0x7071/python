def jugo_todos_los_partidos(torneo):
    #Si jugo todo los partidos True
    dictionary={}
    valores=['0', '0', '0']
    for lista in torneo:
        if lista[0] not in dictionary:
            dictionary.update({lista[0]:valores})
        else:
            dictionary{(lista[0])}-1)=+1
        if lista[1] not in dictionary:
            dictionary.update({lista[1]:valores})
        else:
            dictionary.update({lista[1]:[+1,0,0]})
        print(dictionary)
    return

def main():
    torneo_1 = [ ['Boca', 'Racing', 3, 1], ['River', 'Racing', 1, 1], ['River', 'Boca', 0, 6] ]
    jugo_todos_los_partidos(torneo_1)


main()