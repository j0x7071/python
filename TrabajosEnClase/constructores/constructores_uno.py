class Persona:
    ultimo_dni=0
    
    def __init__(self,nombre):
        self.nombre=nombre
    
    def decirNombre(self):
        print("Me llamo" + self.nombre)
        
nicolas=Persona("Nicolas")
joaquin=Persona("pEDRO")

nicolas.decirNombre()
joaquin.decirNombre()
print(nicolas.nombre)
print(nicolas)