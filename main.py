import sqlite3
import datetime

try:
    con = sqlite3.connect('Diccionario.db')
    cursor = con.cursor()
    print("Conectado a la Base de Datos...")

    #---CREACION DE TABLA---

    qry = '''CREATE TABLE diccionario (
    id INTEGER PRIMARY KEY,
          palabra TEXT NOT NULL,
          significado TEXT NOT NULL,
          eventTime TIMESTAMP)
          '''
    cursor.execute(qry)

    #---DATOS A INTRODUCIR---

    id = input("Id: ")
    plb = input("Palabra: ")
    sig = input("Significado: ")
    z = datetime.datetime.now()

    qry = ''' INSERT INTO diccionario
              ('id', 'palabra', 'significado', 'eventTime')
              VALUES (?, ?, ?, ?);
          '''

    ipsz = (id, plb, sig, z)
    cursor.execute(qry, ipsz)
    con.commit()

    #---DATOS A MOSTRAR EN PANTALLA---

    qry = '''SELECT id, palabra, significado, eventTime FROM diccionario'''
    cursor.execute(qry)


    registro = cursor.fetchall()

    for registro in registro:
        print(registro)

    #---DATOS A ACTUALIZAR---

    #qry = '''UPDATE diccionario SET palabra = "Bro" WHERE significado = "Amigo" '''
    #cursor.execute(qry)
    #con.commit()

    #---DATOS A ELIMINAR---

    #qry = '''DELETE FROM diccionario WHERE palabra = "Chantin" '''
    #cursor.execute(qry)
    #con.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Error al conectar al SQLite", error)

finally:
    if con:
        con.close()
        print("Conexion terminada...")
