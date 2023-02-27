class Product: 
    def __init__(self):
        self.packingDateDay=0
        self.packingDateMonth=0
        self.packingDateYear=0
        self.countryOrigin=""
        self.lotNum=0
        self.dateExpiryDay=0
        self.dateExpiryMonth=0
        self.dateExpiryYear=0
class Fresh(Product):
    def __init__(self):
        self.s=0
class Refrigerated(Product):
    def __init__(self):
        self.FWcode=""
        self.RecHoldTemp=0.0
class Frozen(Product):
 def show():
     print()
class Air(Frozen): 
    def __init__(self):
        self.NiPercent=0.0
        self.O2Perc=0.0
        self.CO2Perc=0.0
        self.WaterPerc=0.0
class Water(Frozen):
    def __init__(self):
        self.grSaltLiter=0.0
class Nitrogen(Frozen):
    def __init__(self):
        self.FreezingMethod=""
        self.TimeNirogenSeg=0.0
        
def DATE(PX=Product()):    
    while True:
        PX.packingDateDay=int(input("Day: ") )
        if PX.packingDateDay>0 and PX.packingDateDay<=31:
            break
    while True:
        PX.packingDateMonth=int(input("Month: "))
        if PX.packingDateMonth>0 and PX.packingDateMonth<=12:
            break
    while True:
        PX.packingDateYear=int(input("Year: "))
        if PX.packingDateYear>=2000 and PX.packingDateYear<=2021:
            break
        
def DateEx(Pro=Product()):
    while True:
        Pro.dateExpiryDay=int(input("Day: ") )
        if Pro.dateExpiryDay>0 and Pro.dateExpiryDay<=31:
            break
    while True:
        Pro.dateExpiryMonth=int(input("Month: "))
        if Pro.dateExpiryMonth>0 and Pro.dateExpiryMonth<=12:
            break
    while True:
        Pro.dateExpiryYear=int(input("Year: "))
        if Pro.dateExpiryYear>=2000 and Pro.dateExpiryYear<=2021:
            break
    
def show(Fresh=Fresh()):
    print("\n\n\nINFORMATION")
    print("Date of expiry: ",Fresh.dateExpiryDay,"/",Fresh.dateExpiryMonth,"/",Fresh.dateExpiryYear)
    print("Lot Number: ",Fresh.lotNum)
    print("Packing date: ",Fresh.packingDateDay,"/",Fresh.packingDateMonth,"/",Fresh.packingDateYear)
    print("Country origin: ",Fresh.countryOrigin)
    
def showR(Ref=Refrigerated()):
    print("\n\n\nINFORMATION")
    print("Date of expiry: ",Ref.dateExpiryDay,"/",Ref.dateExpiryMonth,"/",Ref.dateExpiryYear)
    print("lot Number: ",Ref.lotNum)
    print("Packing date: ",Ref.packingDateDay,"/",Ref.packingDateMonth,"/",Ref.packingDateYear)
    print("Country origin: ",Ref.countryOrigin)
    print("Food watchdog code: ",Ref.FWcode)
    print("Holiding temperature recomended: ",Ref.RecHoldTemp)
    
def showA(air=Air()):
    print("\n\n\nINFORMATION")
    print("Date of expiry: ",air.dateExpiryDay,"/",air.dateExpiryMonth,"/",air.dateExpiryYear)
    print("Lot Number: ",air.lotNum)
    print("% Nitrogen: ",air.NiPercent)
    print("% Oxigen: ",air.O2Perc)    
    print("% Carbon dioxide: ",air.CO2Perc)
    print("% Water steam: ",air.WaterPerc)

def showW(water=Water()):
    print("\n\n\nINFORMATION")
    print("Date of expiry: ",water.dateExpiryDay,"/",water.dateExpiryMonth,"/",water.dateExpiryYear)
    print("\nLot Number: ",water.lotNum)
    print("Salinity of the water with which the freezing was carried out (in grams): ",water.grSaltLiter)
    
def showN(Ni=Nitrogen()):
    print("\n\n\nINFORMATION")
    print("Date of expiry: ",Ni.dateExpiryDay,"/",Ni.dateExpiryMonth,"/",Ni.dateExpiryYear)
    print("Lot Number: ",Ni.lotNum)
    print("Freezing method used",Ni.FreezingMethod)
    print("Exposure time to nitrogen (in seconds): ",Ni.TimeNirogenSeg)
    
def MENU():
    op=0
    while True:
        menu="""\n\n\n        
                MENU
        1. Fresh products
        2. Refrigerated products
        3. Frozen products
        0. exit"""
        print (menu)
        op=int(input("\tselect and option "))
        if op>=0 or op<=3:
            break
    return op
    
def SUBMENU():
    op=0
    while True:
        print("1. Air frozen")
        print("2. Frozen by water")
        print("3. Nitrogen frozen")  
        print("0. Back to MENU")
        op=int(input("\tselect and option "))
        if op>=0 or op<=3:
            break
    return op

#main()
pause=""
option=0,
option1=0,

Fresh1=Fresh()
Ref1=Refrigerated()
Air1=Air()
Water1=Water()
Ni=Nitrogen()

while True:
    option=MENU()
    if option == 1:   
        print("\n\n\nFRESH PRODUCTS")
        print("Date of expiry")
        DateEx(Fresh1)
        Fresh1.lotNum=int(input("Lot Number: "))
        print("\n\nPacking date")
        DATE(Fresh1)
        Fresh1.countryOrigin=input("Country Origin: ")
        show(Fresh1)
        pause=input("press any key to continue: ")
    elif option==2:
        print("\n\n\nREFRIGERATED PRODUTCS")
        print("Date of expiry")
        DateEx(Ref1)
        Ref1.lotNum=int(input("\nLot Number: "))
        Ref1.FWcode=input("Food watchdog code: ")
        print("\n\nPacking date")
        DATE(Ref1)
        Ref1.RecHoldTemp=float(input("Holding temperature recommended: "))
        Ref1.countryOrigin=input("Country Origin: ")
        showR(Ref1)
        pause=input("press any key to continue: ")
    elif option ==3:
        while True:
            print("\n\n\nFROZEN")
            option1=SUBMENU()
            if option1==1:
                print("\n\n\nAIR FROZEN")
                print("Date of expiry")
                DateEx(Air1)
                Air1.lotNum=int(input("Lot Number: "))
                Air1.NiPercent=float(input("% Nitrogen: "))
                Air1.O2Perc=float(input("% Oxigen: "))
                Air1.CO2Perc=float(input("% Carbon dioxide: "))
                Air1.WaterPerc=float(input("% water steam: "))
                showA(Air1)
                pause=input("press any key to continue: ")
            elif option1 ==2:
                print("\n\n\nWATER FROZEN")
                Water1.lotNum=int(input("Lot Number: "))
                print("Date of expiry")
                DateEx(Water1)
                Water1.grSaltLiter=float(input("Salinity of the water with which the freezing was carried out (in grams): "))
                showW(Water1)
                pause=input("press any key to continue: ")
            elif option1==3:
                print("\n\n\nNITROGEN FROZEN")
                Ni.lotNum=int(input("Lot Number: "))
                print("Date of expiry")
                DateEx(Ni)
                Ni.FreezingMethod=input("Freezing method used: ")
                Ni.TimeNirogenSeg=float(input("Exposure time to nitrogen (in seconds): "))
                showN(Ni)
                pause=input("press any key to continue: ")
            elif option1 ==0:
                break                
    elif option == 0:
        break