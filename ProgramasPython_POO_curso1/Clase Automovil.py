class Automovil:
    def __init__(self,tipo):
        #Atributos
        self.marca
        self.color 
        self.km 
        
        #Metodos
        
        
        def ReadMarca(self):
            self.marca=input("Insert the marca: ")
            return self.marca
        def ReadColor(self):
            self.color=input("Insert the color: ")
            return self.color
        def ReadKm(self):
            self.km=input("Insert the marca: ")
            return self.km
        def Show(self,M,C,K):
            print("The marca is: "+M)
            print("The color is: "+C)
            print("The km is: "+K)
            
auto1=Automovil("A")
M=auto1.marca()
C=auto1.color()
K=auto1.km()
auto1.Show(M,C,K)


