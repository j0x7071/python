def es_capicua(palabra):
    return palabra==palabra[::-1]

def main():
    print(es_capicua("neu"))

main()