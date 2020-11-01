import sqlite3

miConexion = sqlite3.connect("PrimerBase")


miCursor = miConexion.cursor()

## miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")

## miCursor.execute("INSERT INTO PRODUCTOS VALUES('PELOTA',15,'Deportes')")

listaDeProductos = [
    ("Remera", 23, "Deportes"),
    ("Raqueta", 433, "Deportes"),
    ("Medias", 9, "Deportes")
    ("Zapatillas", 19, "Deportes")
]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",listaDeProductos)


# Lectura de datos
miCursor.execute("Select * from PRODUCTOS")

resultado = miCursor.fetchall()

print(resultado)

miConexion.commit()

miConexion.close()
