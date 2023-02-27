import math

class FiguraRegular: 
    def __init__(self,lado = 3): 
        self.lado = lado 
        self.__area = 0 
    def verArea(self): 
        return self.__area
    def setArea(self,A):
        self.__area=A
    
class TriangleEq(FiguraRegular):
    def area(self):
        b=math.sqrt((self.lado**2)-((self.lado)/2)**2)
        Ar=((self.lado/2)*b)/2
        self.setArea(Ar)
        
class Square(FiguraRegular):
    def area(self):
        Area=self.lado*self.lado;
        self.setArea(Area)
        
Equilateral=TriangleEq(8)
Equilateral.area()
print("Equilateral triangle area: ",Equilateral.verArea())

square=Square(6)
square.area()
print("Square area: ",square.verArea())
