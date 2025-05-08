from CargaDatos.CargarBBDD import CargarBBDD


class GestionErrores:
    def ejecutar(self):
        print("--- GESTIÓN DE ERRORES ---")
        print("Actualmente no se han definido errores específicos para gestionar.")
        print("Esta sección puede usarse para validar estructuras de datos o revisar fallos de carga.")
        # Aquí podrías implementar revisión de claves duplicadas, formatos erróneos, etc.

    def contar_alumnos(self):
        print("No se encontraron alumnos con ese criterio.")
        volver = input("¿Deseas añadir algun dato o volver al menú principal? (A/V): ").strip().upper()
        if volver == 'N':
            return
        elif volver == 'A':
            from CargaDatos.CargarBBDD import CargarBBDD

            CargarBBDD().ejecutar()
        else:
            print("Operación cancelada.")
            return



