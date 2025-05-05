import sys
from CargaDatos.VaciarBBDD import VaciarBBDD
from CargaDatos.CargarBBDD import CargarBBDD
from CargaDatos.GestionErrores import GestionErrores
from GestionAlumnos.FiltrarAlumnos import FiltrarAlumnos
from GestionAlumnos.Subcaso import Subcaso
from GestionPrestamos.GestionPrestamos import GestionPrestamos
from GestionListados.GestionListados import GestionListados


def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Vaciar Base de Datos")
    print("2. Cargar Datos en Base de Datos")
    print("3. Gestionar Errores")
    print("4. Filtrar Alumnos")
    print("5. Modificar Datos de Alumnos")
    print("6. Gestión de Préstamos")
    print("7. Gestión de Listados")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            VaciarBBDD().ejecutar()
        elif opcion == "2":
            CargarBBDD().ejecutar()
        elif opcion == "3":
            GestionErrores().ejecutar()
        elif opcion == "4":
            FiltrarAlumnos().ejecutar()
        elif opcion == "5":
            Subcaso().ejecutar()
        elif opcion == "6":
            GestionPrestamos().ejecutar()
        elif opcion == "7":
            GestionListados().ejecutar()
        elif opcion == "0":
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
