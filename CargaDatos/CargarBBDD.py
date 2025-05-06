from Recursos.Configuracion import Conexion
import re

class CargarBBDD:
    def ejecutar(self):
        print("--- CARGA DE DATOS ---")
        config = Conexion()
        conexion = config.conectar()
        if not conexion:
            return
        cursor = conexion.cursor()

        # Compilar expresiones regulares
        val_dni = re.compile(r"^\d{8}[A-Z]$")
        val_nombre = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$")
        val_isbn = re.compile(r"^(97(8|9))?\d{9}(\d|X)$")

        try:
            tabla = input("¿Qué tabla quieres cargar? (alumnos, cursos, materias, libros): ").strip().lower()

            #Cargando datos en alumnos
            if tabla == "alumnos":
                dni = input("DNI: ").strip().upper()
                if not val_dni.match(dni):
                    print("❌ DNI no válido.")
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
                sql = "INSERT INTO alumnos (dni, nombre, apellidos, tramo, bilingue) VALUES (%s, %s, %s, %s, %s)"
                datos = (dni, nombre, apellidos, tramo, bilingue)

            #Cargando datos en cursos
            elif tabla == "cursos":
                curso = input("Nombre del curso: ").strip()
                nivel = input("Nivel: ").strip()
                # Validar texto
                if not val_nombre.match(curso) or not val_nombre.match(nivel):
                    print("❌ Curso o nivel no válidos.")
                    return
                sql = "INSERT INTO cursos (curso, nivel) VALUES (%s, %s)"
                datos = (curso, nivel)

            #Cargando datos en materias
            elif tabla == "materias":
                id_materia = input("ID de la materia: ").strip()
                nombre_mat = input("Nombre: ").strip().title()
                if not val_nombre.match(nombre_mat):
                    print("❌ Nombre de materia no válido.")
                    return
                departamento = input("Departamento: ").strip().title()
                if not val_nombre.match(departamento):
                    print("❌ Departamento no válido.")
                    return
                sql = "INSERT INTO materias (id, nombre, departamento) VALUES (%s, %s, %s)"
                datos = (id_materia, nombre_mat, departamento)

            #Cargando datos en libros
            elif tabla == "libros":
                isbn = input("ISBN: ").strip().replace('-', '')
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
