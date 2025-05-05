from Recursos.Configuracion import Conexion

class CargarBBDD:
    def ejecutar(self):
        print("--- CARGA DE DATOS ---")
        conexion = Conexion().conectar()
        if not conexion:
            return

        cursor = conexion.cursor()
        try:
            tabla = input("¿Qué tabla quieres cargar? (alumnos, cursos, materias, libros): ").strip().lower()
            if tabla == "alumnos":
                nie = input("NIE: ")
                nombre = input("Nombre: ")
                apellidos = input("Apellidos: ")
                tramo = input("Tramo (0, I, II): ")
                bilingue = input("¿Es bilingüe? (0 = Sí, 1 = No): ")
                sql = "INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) VALUES (%s, %s, %s, %s, %s)"
                datos = (nie, nombre, apellidos, tramo, bilingue)

            elif tabla == "cursos":
                curso = input("Nombre del curso: ")
                nivel = input("Nivel: ")
                sql = "INSERT INTO cursos (curso, nivel) VALUES (%s, %s)"
                datos = (curso, nivel)

            elif tabla == "materias":
                id_materia = input("ID de la materia: ")
                nombre = input("Nombre: ")
                departamento = input("Departamento: ")
                sql = "INSERT INTO materias (id, nombre, departamento) VALUES (%s, %s, %s)"
                datos = (id_materia, nombre, departamento)

            elif tabla == "libros":
                isbn = input("ISBN: ")
                titulo = input("Título: ")
                autor = input("Autor: ")
                ejemplares = input("Número de ejemplares: ")
                id_materia = input("ID de materia: ")
                id_curso = input("Nombre del curso: ")
                sql = "INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) VALUES (%s, %s, %s, %s, %s, %s)"
                datos = (isbn, titulo, autor, ejemplares, id_materia, id_curso)

            else:
                print("Tabla no reconocida.")
                return

            cursor.execute(sql, datos)
            conexion.commit()
            print(f"✅ Datos insertados correctamente en la tabla '{tabla}'.")
        except Exception as e:
            print(f"❌ Error al insertar datos: {e}")
        finally:
            cursor.close()
            conexion.close()

    def guargar_BBDD(self):
        print("Guardando BBDD...")

