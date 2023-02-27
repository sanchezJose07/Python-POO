import math
class Complex:
    def __init__(self):
        self.r=0
        self.i=0  
        self.m=0
        self.a=0

    def ShowArg(self):
        print("arg(z) = ",self.a)    
    def ShowModule(self):
        print("|z| = ",self.m)            
    def ShowComplex(self):
        print("z = (",self.r,") + (",self.i,")i")          
    def InsertComplex(self):
        self.r=float(input("Insert the real part: "))
        self.i=float(input("Insert the imagynary part: "))
        
#Numeros Complejos metodos
def addC(Zx=Complex(),Zy=Complex()):
    Zr=Complex()
    Zr.r=Zx.r+Zy.r
    Zr.i=Zx.i+Zy.i
    return Zr

def subC(Zx=Complex(),Zy=Complex()):
    Zres=Complex()
    Zres.r=Zx.r-Zy.r
    Zres.i=Zx.i-Zy.i
    return Zres
    
def multC(Zx=Complex(),Zy=Complex()):
    Zres=Complex()
    Zres.r=Zx.r*Zy.r-Zx.i*Zy.i;
    Zres.i=Zx.r*Zy.i+Zx.i*Zy.r;
    return Zres
    
def divC(Zx=Complex(),Zy=Complex()):
     Zres= Complex()
     Zres.r=(Zx.r*Zy.r+Zx.i*Zy.i)/((Zy.r*Zy.r)+(Zy.i*Zy.i))
     Zres.i=(Zx.i*Zy.r-Zx.r*Zy.i)/((Zy.r*Zy.r)+(Zy.i*Zy.i))
     return Zres
 
def exponent2(Zx=Complex()):
    Zres=Complex()
    Zres.r=(Zx.r**2)-(Zx.i**2)
    Zres.i=2*Zx.r*Zx.i
    return Zres

def Module(Zx=Complex()):
    m=0
    m=math.sqrt((Zx.r**2)+(Zx.i**2))
    return m

def Argument(Zx=Complex()):
    a=0
    a=math.atan((Zx.i)/(Zx.r))
    return a

def MENU():
    op=0
    while True:
        print("1. Capture")
        print("2. ADD")
        print("3. Subtraction")
        print("4. Multiplication")
        print("5. Divided")
        print("6. Exponent 2, both numbers")
        print("7. Module and argument of Z")
        print("0. exit")
        op=int(input("\tselect and option "))
        if op>=0 or op<=5:
            break
    return op

pause=""
option=0,

Z1=Complex()
Z2=Complex()
Zres=Complex()

while True:
    print("\n\n\nMenu Complex number")
    option=MENU()
    if option == 1:
        print("\n\n\nCapture the complex number")
        print("Enter first complex number")
        Z1.InsertComplex()
        print("\n\nEnter second complex number")
        Z2.InsertComplex()
        print("\nThe complex number are")
        Z1.ShowComplex()
        Z2.ShowComplex()
        pause=input("press any key to continue: ")
    elif option==2:
        print("\n\n\nADD")
        Zres=addC(Z1,Z2)
        print("The add is")
        Zres.ShowComplex()
        pause=input("press any key to continue: ")
    elif option ==3:
        print("\n\n\nSubtraction")
        Zres=subC(Z1,Z2)
        print("The subtraction is")
        Zres.ShowComplex()
        pause=input("press any key to continue: ")
    elif option ==4:
        print("\n\n\nMultiplication")
        Zres=multC(Z1,Z2)
        print("The multiplication is")
        Zres.ShowComplex()
        pause=input("press any key to continue: ")
    elif option==5:
        print("\n\n\nDivided")
        Zres=divC(Z1,Z2)
        print("The divided is")
        Zres.ShowComplex()
        pause=input("press any key to continue: ")
    elif option==6:
        print("\n\n\nExponent 2")    
        Zres=exponent2(Z1)
        Zres.ShowComplex()
        Zres=exponent2(Z2)
        Zres.ShowComplex()
        pause=input("press any key to continue: ")
    elif  option ==7:
        print("\n\n\nModules ")
        Z1.m=Module(Z1)
        Z1.a=Argument(Z1)
        Z2.m=Module(Z2)
        Z2.a=Argument(Z2)
        Z1.ShowModule()
        Z1.ShowArg()
        print("\n")
        Z2.ShowModule()
        Z2.ShowArg()
        pause=input("press any key to continue: ")
    elif option==0:
        break   
    elif option == 0:
        break
    
 