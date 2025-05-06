from Recursos.Configuracion import Conexion
from datetime import date

class GestionPrestamos:
    def ejecutar(self):
        print("--- GESTIÓN DE PRÉSTAMOS ---")
        dni = input("Introduce el DNI del alumno para gestionar el préstamo: ").strip()

        config = Conexion()
        conexion = config().conectar()
        if not conexion:
            return
        cursor = conexion.cursor()

        try:
            # Verificar existencia del alumno
            cursor.execute("SELECT nombre, apellidos FROM alumnos WHERE dni = %s", (dni,))
            alumno = cursor.fetchone()

            if not alumno:
                print("❌ Alumno no encontrado.")
                return
            print(f"Alumno: {alumno[0]} {alumno[1]}")

            # Mostrar libros prestados
            cursor.execute("""
                SELECT isbn, fecha_entrega, fecha_devolucion, estado
                FROM alumnoscrusoslibros
                WHERE dni = %s
            """, (dni,))
            prestamos = cursor.fetchall()

            if not prestamos:
                print("Este alumno no tiene préstamos registrados.")
            else:
                print("Libros prestados:")
                for p in prestamos:
                    print(f"ISBN: {p[0]} | Entregado: {p[1]} | Devolver antes de: {p[2]} | Estado: {'Devuelto' if p[3] == 'D' else 'Prestado'}")

            # Gestionar nuevo préstamo o devolución
            opcion = input("¿Deseas (P)restar un libro nuevo o (D)evolver uno? (P/D): ").strip().upper()

            if opcion == 'P':
                isbn = input("Introduce el ISBN del libro a prestar: ")
                curso = input("Introduce el curso del alumno: ")
                fecha_entrega = date.today()
                fecha_devolucion = input("Introduce la fecha de devolución (YYYY-MM-DD): ")

                cursor.execute("""
                    INSERT INTO alumnoscrusoslibros (dni, curso, isbn, fecha_entrega, fecha_devolucion, estado)
                    VALUES (%s, %s, %s, %s, %s, 'P')
                """, (dni, curso, isbn, fecha_entrega, fecha_devolucion))
                conexion.commit()
                print("✅ Préstamo registrado correctamente.")

            elif opcion == 'D':
                isbn = input("Introduce el ISBN del libro a devolver: ")
                cursor.execute("""
                    UPDATE alumnoscrusoslibros
                    SET estado = 'D'
                    WHERE dni = %s AND isbn = %s AND estado = 'P'
                """, (dni, isbn))
                conexion.commit()
                print("✅ Libro marcado como devuelto.")

            else:
                print("Opción no válida.")

        except Exception as e:
            print(f"❌ Error en la gestión de préstamos: {e}")
        finally:
            cursor.close()
            config.cerrar()
