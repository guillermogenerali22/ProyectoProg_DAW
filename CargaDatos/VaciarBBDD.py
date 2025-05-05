from Recursos.Configuracion import Conexion
class VaciarBBDD:
    def ejecutar(self):
        confirmar = input("¿Deseas vaciar completamente la base de datos? (S/N): ").strip().upper()
        if confirmar != 'S':
            print("Operación cancelada.")
            return

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
            for tabla in tablas:
                cursor.execute(f"DELETE FROM {tabla};")
            conexion.commit()
            print("✅ Todas las tablas han sido vaciadas correctamente.")
        except Exception as e:
            print(f"❌ Error al vaciar la base de datos: {e}")
        finally:
            cursor.close()
            conexion.close()
