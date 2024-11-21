#Metodos de clase


#Atributo de clase

class Persona:
    ultimo_dni=0 #Atributo de clase
    
    def __init__(self):
        self.dni = self.ultimo_dni + 1 #Atributo de instancia
        Persona.aumentar_ultimo_dni()
        # self.ultimo_dni = self.ultimo_dni + 1
        
    @classmethod
    def aumentar_ultimo_dni(cls):
        cls.ultimo_dni = cls.ultimo_dni + 1
    
    
    #METODOS DE INSTANCIA
    def mostrar_dni(self):
        print(self.dni)
    
    def mostrar_ultimo_dni(self):
        print(self.ultimo_dni)
        
        
def main():
    joaquin = Persona()
    
    print("Mi nombre es nicolas y m dni es",end="")
    joaquin.mostrar_dni()
        
main()