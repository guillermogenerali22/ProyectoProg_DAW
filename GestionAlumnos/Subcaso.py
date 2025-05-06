from Recursos.Configuracion import Conexion

class Subcaso:
    def ejecutar(self):
        print("--- MODIFICAR DATOS DE ALUMNOS ---")
        dni = input("Introduce el DNI del alumno que deseas modificar: ").strip()

        # Antes de modificar, mostrar datos completos
        self.ver_datos_alumno(dni)

        config = Conexion()
        conexion = config.conectar()
        if not conexion:
            return
        cursor = conexion.cursor()

        try:
            cursor.execute(
                "SELECT nombre, apellidos, tramo, bilingue FROM alumnos WHERE dni = %s", (dni,)
            )
            alumno = cursor.fetchone()

            if not alumno:
                print("❌ Alumno no encontrado.")
                return

            confirmacion = input(
                f"¿Deseas modificar los datos de este alumno? (S/N): "
            ).strip().upper()
            if confirmacion != 'S':
                print("Modificación cancelada.")
                return

            nuevo_nombre = input(f"Nuevo nombre [{alumno[0]}]: ") or alumno[0]
            nuevos_apellidos = input(f"Nuevos apellidos [{alumno[1]}]: ") or alumno[1]
            nuevo_tramo = input(f"Nuevo tramo [{alumno[2]}]: ") or alumno[2]
            nuevo_bilingue = input(f"¿Bilingüe? (0 = Sí, 1 = No) [{alumno[3]}]: ") or alumno[3]

            sql = (
                "UPDATE alumnos SET nombre = %s, apellidos = %s, tramo = %s, bilingue = %s "
                "WHERE dni = %s"
            )
            datos = (
                nuevo_nombre,
                nuevos_apellidos,
                nuevo_tramo,
                int(nuevo_bilingue),
                dni
            )
            cursor.execute(sql, datos)
            conexion.commit()

            print("✅ Datos del alumno actualizados correctamente.")
            # Volver a mostrar datos actualizados
            self.ver_datos_alumno(dni)
        except Exception as e:
            print(f"❌ Error al modificar los datos del alumno: {e}")
        finally:
            cursor.close()
            config.cerrar()

    def ver_datos_alumno(self, dni):
        """
        Muestra datos del alumno y sus préstamos.
        """
        config = Conexion()
        conexion = config.conectar()
        if not conexion:
            return
        cursor = conexion.cursor()
        try:
            # Datos personales
            cursor.execute(
                "SELECT nombre, apellidos, tramo, bilingue FROM alumnos WHERE dni = %s", (dni,)
            )
            alumno = cursor.fetchone()
            if not alumno:
                print("❌ Alumno no encontrado.")
                return
            print(f"\nDatos del alumno {dni}:")
            print(f"- Nombre: {alumno[0]}")
            print(f"- Apellidos: {alumno[1]}")
            print(f"- Tramo: {alumno[2]}")
            print(f"- Bilingüe: {'Sí' if alumno[3] == 0 else 'No'}")

            # Préstamos asociados
            cursor.execute(
                "SELECT isbn, fecha_entrega, fecha_devolucion, estado "
                "FROM alumnoscrusoslibros WHERE dni = %s", (dni,)
            )
            prestamos = cursor.fetchall()
            if prestamos:
                print("- Préstamos:")
                for prest in prestamos:
                    estado = 'Devuelto' if prest[3] == 'D' else 'Prestado'
                    print(
                        f"  * ISBN: {prest[0]} | Entrega: {prest[1]} | Devolución: {prest[2]} | Estado: {estado}"
                    )
            else:
                print("- No tiene préstamos registrados.")
            print()
        except Exception as e:
            print(f"❌ Error al obtener datos del alumno: {e}")
        finally:
            cursor.close()
            config.cerrar()
