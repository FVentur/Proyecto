import sqlite3
import re
def Conexion():
    global Aux
    loopex = True
    while loopex:
        try:
            miConexion = sqlite3.connect("Puntaje.sqlite")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM SCORE")
            num = miCursor.fetchall()
            num = "".join([str(x) for x in num])
            num = re.sub("[()',]", "", num)
            miConexion.commit()
            miConexion.close()
            return num
        except sqlite3.OperationalError:
            miCursor.execute("CREATE TABLE SCORE(PUNTOS INTEGER)")
            miCursor.execute("INSERT INTO SCORE (PUNTOS) VALUES (0)")
            miConexion.commit()
            miConexion.close()

def ActualizarMayor(numero,numeroAnterior):
    numero = str(numero)
    numeroAnterior = str(numeroAnterior)
    miConexion = sqlite3.connect("Puntaje.sqlite")
    miCursor = miConexion.cursor()
    SQL="UPDATE SCORE SET PUNTOS = " + numero + " WHERE PUNTOS = "+ numeroAnterior +";"
    miCursor.execute(SQL)
    miConexion.commit()
    miConexion.close()

