import CargaDatos.GestionErrores
from Recursos.Configuracion import Conexion

class FiltrarAlumnos:
    """
        Clase para filtrar y mostrar alumnos de la base de datos según nombre o NIE.
    """
    def ejecutar(self):
        print("--- FILTRAR ALUMNOS ---")
        filtro = input("Introduce parte del nombre o NIE del alumno para filtrar: ").strip()

        config = Conexion()
        conexion = config.conectar()
        if not conexion:
            return
        cursor = conexion.cursor()

        # Ejecutar consulta con parámetros.
        try:
            # Comprobar si hay alumnos en la base de datos.
            verificacion = "SELECT COUNT(*) FROM alumnos "
            cursor.execute(verificacion)
            cantidad_alumnos = cursor.fetchone()
            if cantidad_alumnos[0] > 0:
                sql = "SELECT nie, nombre, apellidos, tramo, bilingue FROM alumnos WHERE nombre LIKE %s OR nie LIKE %s or apellidos LIKE %s"
                cursor.execute(sql, (f"%{filtro}%", f"%{filtro}%", f"%{filtro}%"))
                alumnos = cursor.fetchall()

                if not alumnos:
                    print("No se encontraron alumnos con ese criterio.")
                    return

            #Mostrar resultados.
                for alumno in alumnos:
                    print(f"NIE: {alumno[0]} | Nombre: {alumno[1]} {alumno[2]} | Tramo: {alumno[3]} | Bilingüe: {'Sí' if alumno[4] == 0 else 'No'}")
            else:
                CargaDatos.GestionErrores.GestionErrores.contar_alumnos(conexion)

"""

        except Exception as e:
            print(f"❌ Error al filtrar alumnos: {e}")
        finally:
            cursor.close()
            config.cerrar()
