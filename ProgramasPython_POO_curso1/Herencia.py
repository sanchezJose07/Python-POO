class Animal: 
    def __init__(self): 
        print("Ha nacido un animal")
    def rugir(self): 
       print("Hace algun ruido")
      
        
class Leon(Animal):
    def __init__(self):
        print ("El leon se encuentra en la cima de la roca")
        
    def posicion(self):
        print("Rey de la selva")
        
class Gato(Animal):
    def __init__(self, Name):
        self.Name=Name
    def cat(self):
        print("My cat's name is ",self.Name)
        self.rugir()
        
            
#self.leon
leon=Leon()
leon.posicion()
print("\n\n")
gatito=Gato("Sebastian")
gatito.cat()