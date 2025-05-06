from Recursos.Configuracion import Conexion
class VaciarBBDD:
    """
    Clase para vaciar completamente las tablas de la base de datos.
    """

    def ejecutar(self):
        print("--- VACIAR BASE DE DATOS ---")
        confirmar = input("¿Deseas vaciar completamente la base de datos? (S/N): ").strip().upper()
        if confirmar != 'S':
            print("Operación cancelada.")
            return

        # Lista de tablas a vaciar.
        tablas = [
            "alumnoscrusoslibros",
            "alumnos",
            "libros",
            "materias",
            "cursos"
        ]

        conexion = Conexion().conectar()
        if not conexion:
            return

        cursor = conexion.cursor()
        try:
            # Vaciar cada tabla en la lista.
            for tabla in tablas:
                cursor.execute(f"DELETE FROM {tabla};")
            conexion.commit()
            print("✅ Todas las tablas han sido vaciadas correctamente.")
        except Exception as e:
            print(f"❌ Error al vaciar la base de datos: {e}")
        finally:
            cursor.close()
            conexion.close()