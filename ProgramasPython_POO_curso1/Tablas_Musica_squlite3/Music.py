import sqlite3

def Insert():
    db1 = sqlite3.connect("musica.db")
    consulta = db1.cursor()
    print("\n\nInsert information")

    artist = input("Artist's name: ")
    album = input("Album: ")
    song = input("Song: ")
    
    
    
    strConsulta = "INSERT INTO Music (Artista, Album, Cancion) VALUES \
    ('"+artist+"','"+album+"','"+song+"')"
    
    #print (strConsulta)
     
    consulta.execute(strConsulta)
    print("consulta")
    consulta.close()
    db1.commit()
    db1.close()
     
def Consult():
    db2 = sqlite3.connect("musica.db")
    #print("Consult Funtion")
    db2.row_factory = sqlite3.Row
    consulta = db2.cursor()
    consulta.execute("select * from Music")
    filas = consulta.fetchall()
    lista=[]
    for fila in filas:
        s={}
        s["Artista"] = str(fila["Artista"])
        s["Album"] = str(fila ["Album"])
        s["Cancion"] = str(fila["Cancion"])
        lista.append(s)
    consulta.close()
    db2.close()
    return (lista)

def Menu():
    option = int (input("\n 1. Insert data \n 2. Consult data \
                   \n 0. exit \n\t select and option "))
    if option == 1:
        Insert()
        Menu()
    elif option == 2:
        listSongs = Consult()
        for songs in listSongs:
            print("\n\nArtist:  ",songs["Artista"])
            print("Album:    ",songs["Album"])
            print("Song:     ",songs["Cancion"] )
    elif option == 0:
        print("End")
        
Menu()