from Recursos.Configuracion import Conexion

class FiltrarAlumnos:
    def ejecutar(self):
        print("--- FILTRAR ALUMNOS ---")
        filtro = input("Introduce parte del nombre o NIE del alumno para filtrar: ").strip()

        conexion = Conexion().conectar()
        if not conexion:
            return
        cursor = conexion.cursor()

        try:
            sql = "SELECT nie, nombre, apellidos, tramo, bilingue FROM alumnos WHERE nombre LIKE %s OR nie LIKE %s"
            cursor.execute(sql, (f"%{filtro}%", f"%{filtro}%"))
            alumnos = cursor.fetchall()

            if not alumnos:
                print("No se encontraron alumnos con ese criterio.")
                return

            for alumno in alumnos:
                print(f"NIE: {alumno[0]} | Nombre: {alumno[1]} {alumno[2]} | Tramo: {alumno[3]} | Bilingüe: {'Sí' if alumno[4] == 0 else 'No'}")

        except Exception as e:
            print(f"❌ Error al filtrar alumnos: {e}")
        finally:
            cursor.close()
            conexion.close()
