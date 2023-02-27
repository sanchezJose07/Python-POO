# Jose Guadalupe Guerrero Sanchez


Fruta = input("Comes fruta? ")
if Fruta == False:
    print ('Nesecitas comer mas frutas')
elif Fruta == True:
    x=input("Cuantas veces a la semana comes frutas? ")
    if x>=5:
        print("Sigue asi")
        dia=input("Cuantas frutas comes al dia? ")
        if dia>2:
            print("Comes saludable")
        elif dia<2:
            print("Te recomedamos comer mas frutas")
    elif x<5 or x>2:
        print("Come mas frutas a la semana")
    elif x<=2:
        print("Necesitas comer mas frutas")
         
