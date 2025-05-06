import sys
from CargaDatos.VaciarBBDD import VaciarBBDD
from CargaDatos.CargarBBDD import CargarBBDD
from CargaDatos.GestionErrores import GestionErrores
from GestionAlumnos.FiltrarAlumnos import FiltrarAlumnos
from GestionAlumnos.Subcaso import Subcaso
from GestionPrestamos.GestionPrestamos import GestionPrestamos
from GestionListados.GestionListados import GestionListados
from Generales.Login import Login
from Generales.Logout import Logout


def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("2. Vaciar Base de Datos")
    print("3. Gestionar Errores")
    print("4. Cargar Base de Datos")
    print("5. Filtrar Alumnos")
    print("6. Modificar Datos de Alumnos")
    print("7. Ver datos alumno")
    print("8. Gestionar Préstamos")
    print("9. Generar Listados")
    print("10. Cerrar Sesión")
    print("0. Salir")
def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    login = Login(usuario, contraseña)
    if login.validate():
        print("Acceso concedido")
        return True
    else:
        print("Acceso denegado")
        return False

def main():
    logueado = False

    while True:
        while not logueado:
            logueado = login()
        if logueado:
            mostrar_menu()
        opcion = input("Seleccione una opción: ")


        if opcion == "2" and logueado:
            VaciarBBDD().ejecutar()
        elif opcion == "3" and logueado:
            GestionErrores().ejecutar()
        elif opcion == "4" and logueado:
            CargarBBDD().ejecutar()
        elif opcion == "5" and logueado:
            FiltrarAlumnos().ejecutar()
        elif opcion == "6" and logueado:
            Subcaso().ejecutar()
        elif opcion == "7" and logueado:
            Subcaso().ver_datos_alumno()
        elif opcion == "8" and logueado:
            GestionPrestamos().ejecutar()
        elif opcion == "9" and logueado:
            GestionListados().ejecutar()
        elif opcion == "10" and logueado:
            Logout().ejecutar()
            logueado = False
        elif opcion == "0":
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción no válida o no tiene permisos. Por favor seleccione nuevamente.")

if __name__ == "__main__":
    main()



