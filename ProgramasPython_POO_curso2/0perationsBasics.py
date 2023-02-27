# Jose Guadalupe Guerrero Sanchez

#clase numcomplejos
class Complex:
    def __init__(self):
        self.r=0
        self.i=0                
    def ShowComplex(self):
        print("z = (",self.r,") + (",self.i,")i")          
    def InsertComplex(self):
        self.r=float(input("Insert the real part: "))
        self.i=float(input("Insert the imagynary part: "))
class Poly:
    def __init__(self):
        self.a=0
        self.b=0
        self.c=0
    def ShowPoly(self):
        print("f(x) = (",self.a,")X^2 + (",self.b,")X + (",self.c,")")    
    def CapturePoly(self):
        self.a=float(input("Insert the coefficient a: "))
        self.b=float(input("Insert the coefficient b: "))
        self.c=float(input("Insert the coefficient c: "))
class Fraction:
    def __init__(self):
        self.num=0
        self.den=0
    def ShowFraction(self):
        print("Fraction: ",self.num,"/",self.den)
    def CaptureFration(self):
        self.num=int(input("Numerator? "))
        self.den=int(input("Denominator? "))
        
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
 
#Polinomios metodos
def addP(Px=Poly(),Py=Poly()):
    Pres=Poly()
    Pres.a=Px.a+Py.a;
    Pres.b=Px.b+Py.b;
    Pres.c=Px.c+Py.c;
    return Pres;

def subP(Px=Poly(),Py=Poly()):
    Pres=Poly()
    Pres.a=Px.a-Py.a;
    Pres.b=Px.b-Py.b;
    Pres.c=Px.c-Py.c;
    return Pres;
 
#Fracciones metodos 
def addF(fx=Fraction(),fy=Fraction()):
    fres=Fraction()
    fres.num=fx.num*fy.den+fx.den*fy.num
    fres.den=fx.den*fy.den
    return fres

def subF(fx=Fraction(),fy=Fraction()):
    fres=Fraction()
    fres.num=fx.num*fy.den-fx.den*fy.num
    fres.den=fx.den*fy.den
    return fres

def multF(fx=Fraction(),fy=Fraction()):
    fres=Fraction()
    fres.num=fx.num*fy.num
    fres.den=fx.den*fy.den
    return fres

def divF(fx=Fraction(),fy=Fraction()):
    fres=Fraction()
    fres.num=fx.num*fy.den
    fres.den=fx.den*fy.num
    return fres

#Funciones
def SUBMENU():
    op=0
    while True:
        print("1. Capture")
        print("2. ADD")
        print("3. Subtraction")
        print("4. Multiplication")
        print("5. Divided")
        print("0. Back to MENU")
        op=int(input("\tselect and option "))
        if op>=0 or op<=5:
            break
    return op

def SUBMENUP():
    op=0
    while True:
        print("\t\n\nMenu Polynomials")
        print("1. Capture")
        print("2. ADD")
        print("3. Subtraction")
        print("0. Back to MENU")
        op=int(input("\tselect and option "))
        if op>=0 or op<4:
            break
    return op
   
def MENU():
    op=0,
    while True:
        menu="""
        \n\n\tMAIN MENU
        1. MENU FRACTIONS
        2. MENU COMPLEX NUMBER
        3. MENU POLYNOMIAL
        0. Exit """
        print(menu)
        op=int(input("\tselect and option "))
        if (op>=0 or op<=3):
            break
    return op

#main()
pause=""
option=0,
option1=0,

Z1=Complex()
Z2=Complex()
Zres=Complex()
f1=Fraction()
f2=Fraction()
fres=Fraction()
P1=Poly()
P2=Poly()
Pres=Poly()

while True:
 #   cls()
    option=MENU()
    if option ==1:
        while True:
            print("\t\n\n\nMenu Fraction")
            option1=SUBMENU()
            if option1 == 1:
                print("\n\n\nCapture the fractions")
                print("Enter first fraction")
                f1.CaptureFration()
                print("\nEnter second fraction")
                f2.CaptureFration()
                print("\nThe fractions are")
                f1.ShowFraction()
                f2.ShowFraction()
                pause=input("press any key to continue: ")
            elif option1==2:
                print("\n\n\nADD")
                fres=addF(f1,f2)
                print("The add of f1+f2 is")
                fres.ShowFraction()
                pause=input("press any key to continue: ")
            elif option1 ==3:
                print("\n\n\nSubtraction")
                fres=subF(f1,f2)
                print("The Subtraction of f1-f2 is")
                fres.ShowFraction()
                pause=input("press any key to continue: ")
            elif option1 ==4:
                print("\n\n\nMultiplication")
                fres=multF(f1,f2)
                print("The multiplication is")
                fres.ShowFraction()
                pause=input("press any key to continue: ")
            elif option1==5:
                print("\n\n\nDivided")
                fres=divF(f1,f2)
                print("The divided is")
                fres.ShowFraction()
                pause=input("press any key to continue: ")
            elif option1==0:
                break
    elif option ==2:
        while True:
            print("\n\n\nMenu Complex number")
            option1=SUBMENU()
            if option1 == 1:
                print("\n\n\nCapture the complex number")
                print("Enter first complex number")
                Z1.InsertComplex()
                print("\n\nEnter second complex number")
                Z2.InsertComplex()
                print("\nThe complex number are")
                Z1.ShowComplex()
                Z2.ShowComplex()
                pause=input("press any key to continue: ")
            elif option1==2:
                print("\n\n\nADD")
                Zres=addC(Z1,Z2)
                print("The add is")
                Zres.ShowComplex()
                pause=input("press any key to continue: ")
            elif option1 ==3:
                print("\n\n\nSubtraction")
                Zres=subC(Z1,Z2)
                print("The subtraction is")
                Zres.ShowComplex()
                pause=input("press any key to continue: ")
            elif option1 ==4:
                print("\n\n\nMultiplication")
                Zres=multC(Z1,Z2)
                print("The multiplication is")
                Zres.ShowComplex()
                pause=input("press any key to continue: ")
            elif option1==5:
                print("\n\n\nDivided")
                Zres=divC(Z1,Z2)
                print("The divided is")
                Zres.ShowComplex()
                pause=input("press any key to continue: ")
            elif option1==0:
                break
    elif option==3:
        while True:
            option1=SUBMENUP()
            if option1 == 1:
                print("\n\n\nCapture the polinamials")
                print("Enter first polynomial")
                P1.CapturePoly()
                print("\n\nEnter second polinomial")
                P2.CapturePoly()
                print("\nThe polynomials are")
                P1.ShowPoly()
                P2.ShowPoly()
                pause=input("press any key to continue: ")
            elif option1==2:
                print("\n\n\nADD")
                Pres=addP(P1,P2)
                print("The add is")
                Pres.ShowPoly()
                pause=input("press any key to continue: ")
            elif option1 ==3:
                print("\n\n\nSubtraction")
                Pres=subP(P1,P2)
                print("The subtraction is")
                Pres.ShowPoly()
                pause=input("press any key to continue: ")
    elif option == 0:
        break
 #Fin programa 