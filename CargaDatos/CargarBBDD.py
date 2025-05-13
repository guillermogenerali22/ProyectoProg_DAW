from Recursos.Configuracion import Conexion
import re
from CargaDatos.GestionErrores import GestionErrores


class CargarBBDD: #todo hay q mostrar los datos filtrados a la vez q se insertan los alumnos. sentencias de filtro para añadir las PK y FK
    def ejecutar(self):
        print("--- CARGA DE DATOS ---")
        config = Conexion()
        conexion = config.conectar()
        if not conexion:
            return
        cursor = conexion.cursor()

        # Compilar expresiones regulares
        val_nie = re.compile(r"^[XYZ]?\d{7}[A-Z]$")
        val_nombre = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$")
        val_isbn = re.compile(r"^(97(8|9))?\d{9}(\d|X)$")

        try:
            tabla = input("¿Qué tabla quieres cargar? (alumnos, cursos, materias, libros): ").strip().lower()

            #Cargando datos en alumnos
            if tabla == "alumnos":
                nie = input("NIE o DNI: ").strip().upper()
                if not val_nie.match(nie):
                    print("❌ NIE no válido.")
                    return
                nombre = input("Nombre: ").strip().title()
                if not val_nombre.match(nombre):
                    print("❌ Nombre no válido.")
                    return
                apellidos = input("Apellidos: ").strip().title()
                if not val_nombre.match(apellidos):
                    print("❌ Apellidos no válidos.")
                    return
                tramo = input("Tramo (0, I, II): ").strip().upper()
                bilingue = input("¿Es bilingüe? (0 = Sí, 1 = No): ").strip()
                sql = "INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) VALUES (%s, %s, %s, %s, %s)"
                datos = (nie, nombre, apellidos, tramo, bilingue)

            #Cargando datos en cursos
            elif tabla == "cursos":

                curso = input("Nombre del curso: ").strip()
                nivel = input("Nivel: ").strip()


                sql = "INSERT INTO cursos (curso, nivel) VALUES (%s, %s)"
                datos = (curso, nivel)

            #Cargando datos en materias
            elif tabla == "materias":
                id_materia = input("ID de la materia: ").strip()
                nombre_mat = input("Nombre: ").strip().title()

                departamento = input("Departamento: ").strip().title()
                if not val_nombre.match(departamento):
                    print("❌ Departamento no válido.")
                    return
                sql = "INSERT INTO materias (id, nombre, departamento) VALUES (%s, %s, %s)"
                datos = (id_materia, nombre_mat, departamento)



            #Cargando datos en libros
            elif tabla == "libros":
                hay_materias = "SELECT COUNT(*) FROM materias"
                cursor.execute(hay_materias)
                cantidad_materias = cursor.fetchone()
                hay_cursos = "SELECT COUNT(*) FROM cursos"
                cursor.execute(hay_cursos)
                cantidad_cursos = cursor.fetchone()
                if cantidad_materias[0] and cantidad_cursos[0] > 0:
                    isbn = input("ISBN: ").strip().replace('-', '').upper()
                    if not val_isbn.match(isbn):
                        print("❌ ISBN no válido.")
                        return
                    titulo = input("Título: ").strip()
                    autor = input("Autor: ").strip().title()
                    ejemplares = input("Número de ejemplares: ").strip()
                    id_materia = input("ID de materia: ").strip()
                    id_curso = input("ID de curso: ").strip()
                    sql = "INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) VALUES (%s, %s, %s, %s, %s, %s)"
                    datos = (isbn, titulo, autor, ejemplares, id_materia, id_curso)

                else:
                    GestionErrores.contar_materias(conexion)



            else:
                print("❌ Tabla no reconocida.")
                return

            cursor.execute(sql, datos)
            conexion.commit()
            print(f"✅ Datos insertados correctamente en la tabla '{tabla}'.")

        except Exception as e:
            print(f"❌ Error al insertar datos: {e}")
        finally:
            cursor.close()
            config.cerrar()

    def ver_datos(self):
        """
        Muestra los datos de la tabla seleccionada.
        """
        config = Conexion()
        conexion = config.conectar()
        if not conexion:
            return
        cursor = conexion.cursor()

        try:
            tablas = [
                "alumnoscrusoslibros",
                "alumnos",
                "libros",
                "materias",
                "cursos"
            ]
            for tabla in tablas:
                sql = f"SELECT * FROM {tabla}"
                cursor.execute(sql)
                datos = cursor.fetchall()
                print(f"\nDatos de la tabla '{tabla}':")
                for fila in datos:
                    print(fila)

        except Exception as e:
            print(f"❌ Error al mostrar datos: {e}")
        finally:
            cursor.close()
            config.cerrar()
