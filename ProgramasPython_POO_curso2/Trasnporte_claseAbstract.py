#Crea dos implementaciones de la siguiente clase abstracta:

from abc import ABCMeta, abstractmethod 
class Transporte: 
    __metaclass__ = ABCMeta 
    def __init__(self, medio): 
        self.medio = medio 
    #Usar el atributo "medio" para definir como avanza 
    @abstractmethod 
    def avanzar(self, frase): pass 
    def giraIzquierda(self): 
        print ("Gira a la izquierda")
    def giraDerecha(self): print ("Gira a la derecha") 
    #De acuerdo al "medio" especificar que hace para frenar 
    @abstractmethod 
    def detener(self): pass

class Public(Transporte):
    def avanzar(self,*frase):
        for frase in frase:
            print (self.medio,frase)
            
    def detener(self,*word):
        for word in word:
            print(self.medio,word)
            
class Private(Transporte):
    def avanzar(self, *frase):
        for frase in frase:
            print (self.medio,frase)
            
    def detener(self, *commentary):
        for commentary in commentary:
            print(self.medio,commentary)
            
publico=Public("Autobus")
publico.avanzar("se esta evanzando por el pavimento")
publico.giraIzquierda()
publico.giraDerecha()
publico.detener("se ha detenido el autobus")

private=Private("Coche")
private.avanzar("avanzamos hacia el destino")
private.giraDerecha()
private.giraIzquierda()
private.detener("Nos detendremos en la gasolineria")
