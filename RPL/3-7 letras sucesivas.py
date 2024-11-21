def precendencia_de_caracteres(cadena, caracter_1, caracter_2):
    
    contador=0
    caracteres=""
    bandera=False
    
    for caracter in cadena:

        if bandera==True and caracter==caracter_2:
            contador+=1
            
        bandera=False
        
        if caracter==caracter_1 and bandera==False:
            bandera=True
    
    return contador
            
    

def main():
     print(precendencia_de_caracteres("la mejor verdura del universo es la pizza y el quediga lo contrario esta errado", "e", "r"))
           
main ()