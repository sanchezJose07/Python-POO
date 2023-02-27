i = 0
cal = 0.0
lista1 = [] 
x = int(input("cuantos alumos tiene? "))
while i < x:
    j=0
    while j < 3:
        print("Alumno ",(i+1),", parcial ",(j+1),": ")
        cal = float(input())
        lista1.append(cal)
        j+=1
    i+=1

lista2 = []
for prom in lista1: 
    d = prom 
    if d<6: 
        lista2.append("Reprobado") 
    if d== 6 and d <= 6.4: 
        lista2.append("Aprobado con 6") 
    if d==7 and d<=7.4: 
        lista2.append("Aprobado con 7") 
    if d==8 and d<=8.4: 
        lista2.append("Aprobado con 8") 
    if d==9 and d<=9.4: 
        lista2.append("Aprobado con 9") 
    if d==10: 
        lista2.append("Aprobado con 10") 
    if d >=6.5 and d<=6.9: 
        lista2.append("Aprobado con 7") 
    if d>=7.5 and d<=7.9: 
        lista2.append("Aprobado con 8") 
    if d>=8.5 and d<=8.9: 
        lista2.append("Aprobado con 9") 
    if d>=9.5 and d<=9.9: 
        lista2.append("Aprobado con 10") 

print (lista1) 
print (lista2)