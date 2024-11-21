import hashlib

encontrada=0
input_hash = input("Inserte la contraseña hasheada: ")
pass_doc = input("Inserte el diccionario: ")

try:
    pass_file = open(pass_doc, 'r')
except:
    print("Error:"+ pass_doc + "no ha sido encontrada")
    
for palabra in pass_file:
    palabra_cifrada = palabra.encode('utf-8')
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    digest = palabra_hasheada.hexdigest
    
    if digest == input==hash:
        print("FIND ===> "+ palabra)
        encontrada = 1
        break
    
if not encontrada:
    print("NOT FINDED")