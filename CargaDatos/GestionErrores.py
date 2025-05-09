class GestionErrores:
    def ejecutar(self):
        print("--- GESTIÓN DE ERRORES ---")
        print("Actualmente no se han definido errores específicos para gestionar.")
        print("Esta sección puede usarse para validar estructuras de datos o revisar fallos de carga.")
        # Aquí podrías implementar revisión de claves duplicadas, formatos erróneos, etc.

    def contar_datos(self):
        from CargaDatos.CargarBBDD import CargarBBDD #hago lazy import para evitar un error de import circular
        print("No se encontraron datos con ese criterio.")
        volver = input("¿Deseas añadir algun dato o volver al menú principal? (A/V): ").strip().upper()
        if volver == 'N':
            return
        elif volver == 'A':
            CargarBBDD().ejecutar()
        else:
            print("Operación cancelada.")
            return
    def contar_materias(self):
        from CargaDatos.CargarBBDD import CargarBBDD #hago lazy import para evitar un error de import circular

        print("Antes de cargar libros tiene que haber materias y cursos en la BBDD.")
        volver = input("¿Deseas añadir alguna materia o volver al menú principal? (A/V): ").strip().upper()
        if volver == 'N':
                return
        elif volver == 'A':

            CargarBBDD().ejecutar()
        else:
            print("Operación cancelada.")
            return

