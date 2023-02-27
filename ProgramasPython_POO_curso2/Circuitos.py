import math

class Circuitos():
    def __init__(self,r,i):
        self.Im_r=r
        self.Im_i=i
class ImpedanciaBobina():
    def __init__(self):
        self.XL=0.0
        self.ZL=0.0
        self.w=0
    def show(self):
        print(self.w,"\n", self.XL,"\n", self.ZL)
class NumComplex():
    def __init__(self):
        self.i
        self.r
        
def Impedancia(f,L):
    r=ImpedanciaBobina()
    r.w=2*math.pi*f
    r.XL=r.w*L
    r.ZL=r.XL
    return r
def impe(Z1=NumComplex(),Z2=NumComplex()):
    imp=Circuitos()
    imp.Im_r=Z1.r+Z2.r
    imp.Im_i=Z1.i+Z2.i
    return imp
    
    
CE=Circuitos()      
ib = ImpedanciaBobina()

ib=Impedancia(60,0.15)
print("Impe bomina",ib.ZL)

Z1=NumComplex(20,ib.ZL)
Z2=NumComplex()

CE=impe(Z1,Z2)