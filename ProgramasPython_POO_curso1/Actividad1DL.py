# Jose Guadalupe Guerrero Sanchez
def segundero():
    i=j=0
    lista=[]
    while i<=6:
        while j<10:
            x= ":"+str(i)+str(j)
            j+=1
            lista.append(x)
        j=0
        i+=1
    return (lista)
variable =segundero()
print (variable)
