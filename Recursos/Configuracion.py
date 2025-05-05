import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='proyectobueno_copia'
            )
            return self.conexion
        except mysql.connector.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None

    def cerrar(self):
        if self.conexion:
            self.conexion.close()
