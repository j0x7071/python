import os

#MUESTRA LA RUTA ACTUAL
print("Directorio actual: {} ".format(os.getcwd()))

#INDICA SI LA RUTA EXISTE
print(os.path.isdir("D:/Documentos/"))

#os.chdir("D:/Documentos/")

file = open("filename.txt", "w")
file. write("Primera línea" + os.linesep)
file. write("Segunda línea")
file. close()