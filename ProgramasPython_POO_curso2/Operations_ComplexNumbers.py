class Fractions:
    def __init__(self):
        self.num=0
        self.den=0
    def show(self):
        print(self.num,"/",self.den)
    def capture(self):
        self.num=int(input("Insert the numerator: "))
        self.den=int(input("Insert the denominator: "))       
class Complex:
    def __init__(self):
        self.real=0
        self.imaginary=0
    def capture(self):
        self.real=float(input("Insert real part: "))
        self.imaginary=float(input("Insert the imaginary part: "))       
    def show(self):
        if self.imaginary<0:
            print(self.real,self.imaginary,"i")
        elif self.imaginary>=0:
            print(self.real,"+",self.imaginary,"i")
class Polynomial:
    def __init__(self):
        self.a0=0
        self.a1=0
        self.a2=0
    def capture(self):
        self.a2=float(input("Insert a2: "))
        self.a1=float(input("Insert a1: "))
        self.a0=float(input("Insert the a0: "))       
    def show(self):
        if self.a0<0 and self.a1<0:
            print(self.a2,"x^2",self.a1,"x",self.a0)
        elif self.a0>=0 and self.a1<0:
            print(self.a2,"x^2",self.a1,"x+",self.a0)
        elif self.a0<0 and self.a1>=0:
            print(self.a2,"x^2+",self.a1,"x",self.a0)
        elif self.a0>=0 and self.a1>=0:
            print(self.a2,"x^2+",self.a1,"x+",self.a0)
def fadd(fx=Fractions(),fy=Fractions()):
    faux=Fractions()
    faux.num=(fx.num*fy.den)+(fx.den*fy.num)
    faux.den=(fx.den*fy.den)
    return faux
def fsustract(fx=Fractions(),fy=Fractions()):
    faux=Fractions()
    faux.num=(fx.num*fy.den)-(fx.den*fy.num)
    faux.den=(fx.den*fy.den)
    return faux
def complex_add(comx=Complex(),comy=Complex()):
    com_aux=Complex()
    com_aux.real=(comx.real+comy.real)
    com_aux.imaginary=(comx.imaginary+comy.imaginary)
    return com_aux
def complex_sustract(comx=Complex(),comy=Complex()):
    com_aux=Complex()
    com_aux.real=(comx.real-comy.real)
    com_aux.imaginary=(comx.imaginary-comy.imaginary)
    return com_aux
def polynomial_add(polx=Polynomial(),poly=Polynomial()):
    pol_aux=Polynomial()
    pol_aux.a0=(polx.a0+poly.a0)
    pol_aux.a1=(polx.a1+poly.a1)
    pol_aux.a2=(polx.a2+poly.a2)
    return pol_aux
def polynomial_sustract(polx=Polynomial(),poly=Polynomial()):
    pol_aux=Polynomial()
    pol_aux.a0=(polx.a0-poly.a0)
    pol_aux.a1=(polx.a1-poly.a1)
    pol_aux.a2=(polx.a2-poly.a2)
    return pol_aux
def menu():
    opt=10
    while (opt<0 or opt>4):
        print("Welcome to the program that manipulates fractions polynomials and complex numbers")
        print("1) Capture")
        print("2) Add")
        print("3) Sustract")
        print("4) Show")
        print("0) Exit program")
        opt=int(input("Select an option: "))
        if (opt<0 or opt>4):
            print("Invalid option")
    return opt
def submenu():
    opt=10
    while (opt<0 or opt>3):
        print("Please select an element")
        print("1) Fractions")
        print("2) Complex")
        print("3) Polynomial")
        opt=int(input("Select an option: "))
        if (opt<0 or opt>3):
            print("Invalid option")
    return opt
option=10
option2=10
f1=Fractions()
f2=Fractions()
fres=Fractions()
com1=Complex()
com2=Complex()
com_res=Complex()
pol1=Polynomial()
pol2=Polynomial()
pol_res=Polynomial()
while (option!=0):
    option=menu()
    if option==1:
        print("Welcome to the method that captures elements")
        option2=submenu()
        if option2==1:
            f1.capture()
            f2.capture()
        elif option2==2:
            com1.capture()
            com2.capture()
        elif option2==3:
            pol1.capture()
            pol2.capture()
    elif option==2:
        print("Welcome to the method that add elements")
        option2=submenu()
        if option2==1:
            fres=fadd(f1,f2)
            print("The result of the sum is: ")
            fres.show()
        elif option2==2:
            com_res=complex_add(com1,com2)
            print("The result of the sum is: ")
            com_res.show()
        elif option2==3:
            pol_res=polynomial_add(pol1,pol2)
            print("The result of the sum is: ")
            pol_res.show()
    elif option==3:
        print("Welcome to the method that sustracts elements")
        option2=submenu()
        if option2==1:
            fres=fsustract(f1,f2)
            print("The result of the sustract is: ")
            fres.show()
        elif option2==2:
            com_res=complex_sustract(com1,com2)
            print("The result of the sustract is: ")
            com_res.show()
        elif option2==3:
            pol_res=polynomial_sustract(pol1,pol2)
            print("The result of the sustract is: ")
            pol_res.show()
    elif option==4:
        print("Welcome to the method that shows elements")
        option2=submenu()
        if option2==1:
            f1.show()
            f2.show()
        elif option2==2:
            com1.show()
            com2.show()
        elif option2==3:
            pol1.show()
            pol2.show()
    elif option==0:
        print("Ending program")