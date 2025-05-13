from Recursos.Configuracion import Conexion
import csv
class GestionListados:
    """
    Clase para la generación de listados de alumnos y otros datos personalizados.
    """

    def ejecutar(self):
        print("--- GENERACIÓN DE LISTADOS ---")
        print("1. Listado de alumnos")
        print("2. Listado personalizado")
        print("3. Listado de todo")
        opcion = input("Seleccione una opción (1-2): ").strip()

        config = Conexion()
        conexion = config.conectar()
        if not conexion:
            return
        cursor = conexion.cursor()

        try:
            if opcion == "1":
                # Generar listado de alumnos
                cursor.execute("SELECT nie, nombre, apellidos, tramo, bilingue FROM alumnos")
                alumnos = cursor.fetchall()
                self.exportar_csv(
                    alumnos,
                    ["NIE", "Nombre", "Apellidos", "Tramo", "Bilingüe"],
                    "listado_alumnos.csv"
                )
                print("✅ Listado de alumnos exportado como 'listado_alumnos.csv'")

            elif opcion == "2":
                # Generar listado personalizado
                print("Listados disponibles: cursos, materias, libros")
                tabla = input("¿Qué listado desea generar?: ").strip().lower()
                if tabla in ["cursos", "materias", "libros"]:
                    cursor.execute(f"SELECT * FROM {tabla}")
                    filas = cursor.fetchall()
                    columnas = [i[0] for i in cursor.description]  # Obtener nombres de columnas
                    self.exportar_csv(filas, columnas, f"listado_{tabla}.csv")
                    print(f"✅ Listado de {tabla} exportado como 'listado_{tabla}.csv'")
                else:
                    print("❌ Tabla no válida para listado.")

            elif opcion == "3":
                tablas = {
                    "alumnos": ["nie", "nombre", "apellidos", "tramo", "bilingue"],
                    "cursos": None,
                    "materias": None,
                    "libros": None
                }

                for tabla, columnas in tablas.items():
                    cursor.execute(f"SELECT * FROM {tabla}")
                    filas = cursor.fetchall()
                    if columnas is None:
                        columnas = [desc[0] for desc in cursor.description]
                    self.exportar_csv(filas, columnas, f"listado_{tabla}.csv")
                    print(f"✅ Listado de {tabla} exportado como 'listado_{tabla}.csv'")
            else:
                print("Opción inválida.")
        except Exception as e:
            print(f"❌ Error al generar listado: {e}")
        finally:
            cursor.close()
            config.cerrar()

    def exportar_csv(self, datos, encabezados, nombre_archivo):
        """
        Exporta los datos proporcionados a un archivo CSV.

        """
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(encabezados)
            for fila in datos:
                escritor.writerow(fila)

    def copia_de_seguridad(self):
        """
        Crea un archivo CSV con todos los datos de todas las tablas de la base de datos.
        """
        config = Conexion()
        conexion = config.conectar()
        if not conexion:
            return
        cursor = conexion.cursor()

        try:
            tablas = ["alumnos", "cursos", "materias", "libros"]
            with open("copia_de_seguridad.csv", mode="w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)
                for tabla in tablas:
                    cursor.execute(f"SELECT * FROM {tabla}")
                    filas = cursor.fetchall()
                    columnas = [desc[0] for desc in cursor.description]
                    escritor.writerow([f"Tabla: {tabla}"])
                    escritor.writerow(columnas)
                    escritor.writerows(filas)
                    escritor.writerow([])  # Línea en blanco entre tablas
            print("✅ Copia de seguridad creada como 'copia_de_seguridad.csv'")
        except Exception as e:
            print(f"❌ Error al crear la copia de seguridad: {e}")
        finally:
            cursor.close()
            config.cerrar()