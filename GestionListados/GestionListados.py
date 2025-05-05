from Recursos.Configuracion import Conexion
import csv

class GestionListados:
    def ejecutar(self):
        print("--- GENERACIÓN DE LISTADOS ---")
        print("1. Listado de alumnos")
        print("2. Listado personalizado")
        opcion = input("Seleccione una opción (1-2): ").strip()

        conexion = Conexion().conectar()
        if not conexion:
            return
        cursor = conexion.cursor()

        try:
            if opcion == "1":
                cursor.execute("SELECT nie, nombre, apellidos, tramo, bilingue FROM alumnos")
                alumnos = cursor.fetchall()
                self.exportar_csv(alumnos, ["NIE", "Nombre", "Apellidos", "Tramo", "Bilingüe"], "listado_alumnos.csv")
                print("✅ Listado de alumnos exportado como 'listado_alumnos.csv'")

            elif opcion == "2":
                print("Listados disponibles: cursos, materias, libros")
                tabla = input("¿Qué listado desea generar?: ").strip().lower()
                if tabla in ["cursos", "materias", "libros"]:
                    cursor.execute(f"SELECT * FROM {tabla}")
                    filas = cursor.fetchall()
                    columnas = [i[0] for i in cursor.description]
                    self.exportar_csv(filas, columnas, f"listado_{tabla}.csv")
                    print(f"✅ Listado de {tabla} exportado como 'listado_{tabla}.csv'")
                else:
                    print("❌ Tabla no válida para listado.")
            else:
                print("Opción inválida.")
        except Exception as e:
            print(f"❌ Error al generar listado: {e}")
        finally:
            cursor.close()
            conexion.close()

    def exportar_csv(self, datos, encabezados, nombre_archivo):
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(encabezados)
            for fila in datos:
                escritor.writerow(fila)
