import sqlite3

conexion = sqlite3.connect("musica.db")
consulta=conexion.cursor()

tabla = "CREATE TABLE Music (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"\
    "Artista VARCHAR (30) NOT NULL,"\
    "Album VARCHAR (40) NOT NULL,"\
    "Cancion VARCHAR (29) NOT NULL);"\

print (tabla)

if(consulta.execute(tabla)): 
    print ("La tabla fue creada")
else: print ("La tabla no fue creada")

consulta.close()
conexion.commit()
conexion.close()


