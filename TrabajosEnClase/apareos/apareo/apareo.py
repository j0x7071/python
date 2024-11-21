CODIGO=0
CANTIDAD=1
MODIFICACION=2

def leer(archivo):
    linea = archivo.readline()
    registro=""
    continuar=True
    if (linea):
        registro = linea.rstrip().split(",")
    else:
        continuar=False
        print("ESFALSO")
    return [registro,continuar]

def def_menor(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2


def aparear(maestro,novedades,apareado):
    stock, continuar_stock = leer(maestro)
    actualizar, continuar_actualizar = leer(novedades)
    #print(continuar_actualizar,continuar_stock)
    #print(stock) 
    #print(actualizar)
    while continuar_actualizar and continuar_stock:
        cod_min = def_menor(stock[CODIGO],actualizar[CODIGO])
        #print(stock[CODIGO],actualizar[CODIGO])
        #print(cod_min,"fsfdfd")
        while cod_min==actualizar[CODIGO] and cod_min==stock[CODIGO] and continuar_actualizar and continuar_stok
        while cod_min== actualizar[CODIGO] and continuar_actualizar:
            
            
            if actualizar[MODIFICACION] == M:
                nueva_cantidad = stock[CANTIDAD] + actualizar[CANTIDAD]
                apareado.write(f'{stock[CODIGO]},{nueva_cantidad},\n')
            if actualizar[MODIFICACION] == A:
                apareado.write(f'{actualizar[CODIGO]},{stock[CANTIDAD]},\n')
            
                
        stock, continuar_stock = leer(maestro)
            
            print(stock,stock[CODIGO],continuar_stock,cod_min)
        while cod_min == actualizar[CODIGO] and continuar_actualizar:
            apareado.write(f'{actualizar[CODIGO]},{actualizar[CANTIDAD]},\n')
            print("STOCK ACTUALIZADOO")
            print(actualizar,actualizar[CODIGO])
            actualizar, continuar_actualizar = leer(novedades)
            
            #print(actualizar,actualizar[CODIGO],continuar_actualizar,cod_min)

    return stock[cod_min]

def main():  
    maestro = open("stock.txt","r")
    novedades = open("novedades.txt","r")
    apareado = open("apareados.txt","w")
    
    aparear(maestro,novedades,apareado)
    
    maestro.close()
    novedades.close()
    apareado.close()
    
main()