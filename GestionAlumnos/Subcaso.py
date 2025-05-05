from Recursos.Configuracion import Conexion

class Subcaso:
    def ejecutar(self):
        print("--- MODIFICAR DATOS DE ALUMNOS ---")
        nie = input("Introduce el NIE del alumno que deseas modificar: ").strip()

        conexion = Conexion().conectar()
        if not conexion:
            return
        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT nombre, apellidos, tramo, bilingue FROM alumnos WHERE nie = %s", (nie,))
            alumno = cursor.fetchone()

            if not alumno:
                print("❌ Alumno no encontrado.")
                return

            print(f"Nombre: {alumno[0]} | Apellidos: {alumno[1]} | Tramo: {alumno[2]} | Bilingüe: {'Sí' if alumno[3] == 0 else 'No'}")

            confirmacion = input("¿Deseas modificar los datos de este alumno? (S/N): ").strip().upper()
            if confirmacion != 'S':
                print("Modificación cancelada.")
                return

            nuevo_nombre = input(f"Nuevo nombre [{alumno[0]}]: ") or alumno[0]
            nuevos_apellidos = input(f"Nuevos apellidos [{alumno[1]}]: ") or alumno[1]
            nuevo_tramo = input(f"Nuevo tramo [{alumno[2]}]: ") or alumno[2]
            nuevo_bilingue = input(f"¿Bilingüe? (0 = Sí, 1 = No) [{alumno[3]}]: ") or alumno[3]

            sql = "UPDATE alumnos SET nombre = %s, apellidos = %s, tramo = %s, bilingue = %s WHERE nie = %s"
            datos = (nuevo_nombre, nuevos_apellidos, nuevo_tramo, int(nuevo_bilingue), nie)
            cursor.execute(sql, datos)
            conexion.commit()

            print("✅ Datos del alumno actualizados correctamente.")
        except Exception as e:
            print(f"❌ Error al modificar los datos del alumno: {e}")
        finally:
            cursor.close()
            conexion.close()
