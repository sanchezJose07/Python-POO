def escritura(a,b,c,d,e):
    data=open('C:Users\lupea\python\data.py','w')
    data.write(a)
    data.write(b)
    data.write(c)
    data.write(d)
    data.write(e)
    print ("\ncomplet")
    data.close()
    
escritura("hola"," mundo","\nhoy"," martes"," noviembre")

def lectura():
    data=open('C:Users\lupea\python\data.py','r')
    print(data.read())
    data.close()

lectura()