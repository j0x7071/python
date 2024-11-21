CODIGO=0
CANTIDAD=1
MODIFICACION=2

def leer(archivo):
    linea = archivo.readline()
    continuar=True
    registro="0"
    if linea:
        registro = linea.rstrip().split(",")
    else:
        continuar=False
    return [registro,continuar]

def aparear(maestro,novedades,apareado):
    stock, continuar_stock = leer(maestro)
    actualizar, continuar_actualizar = leer(novedades)
  
    while continuar_actualizar and continuar_stock:
        
        while int(stock[CODIGO])<int(actualizar[CODIGO]) and continuar_stock:
            apareado.write(f'{stock[CODIGO]},{stock[CANTIDAD]}\n')
            stock, continuar_stock = leer(maestro)
            
        while int(stock[CODIGO])>int(actualizar[CODIGO]) and continuar_actualizar:
            apareado.write(f'{actualizar[CODIGO]},{actualizar[CANTIDAD]}\n')
            actualizar, continuar_actualizar = leer(novedades)
           
        while int(stock[CODIGO])==int(actualizar[CODIGO]) and continuar_actualizar:
            cantidad=int(actualizar[CANTIDAD])+int(stock[CANTIDAD])
            apareado.write(f'{actualizar[CODIGO]},{cantidad}\n')
            actualizar, continuar_actualizar = leer(novedades)
            stock, continuar_stock = leer(maestro)
            
    while continuar_actualizar:
        apareado.write(f'{actualizar[CODIGO]},{actualizar[CANTIDAD]}\n')
        actualizar, continuar_actualizar = leer(novedades)
            
         
    while continuar_stock:
        apareado.write(f'{stock[CODIGO]},{stock[CANTIDAD]}\n')
        stock, continuar_stock = leer(maestro)
    
    
    return 

def main():  
    maestro = open("prueba_maestro.txt","r")
    novedades = open("prueba_act.txt","r")
    apareado = open("mezcla.txt","w")
    
    aparear(maestro,novedades,apareado)
    
    maestro.close()
    novedades.close()
    apareado.close()
    
main()