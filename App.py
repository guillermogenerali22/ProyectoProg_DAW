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
from Recursos.ui.Menu import Menu


def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    sesion = Login(usuario, contraseña)
    if sesion.validate():
        print("Acceso concedido")
        return True
    else:
        print("Acceso denegado 🙅")
        return False

def main():
    logueado = False

    while True:
        while not logueado:
            logueado = login()
        if logueado:
            Menu().mostrar_menu()
        opcion = input("🙈Seleccione una opción: ")

#todo crear  constantes en vez de numeros
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
        elif opcion == "1":
            CargarBBDD().ver_datos()
        elif opcion == "11" and logueado:
            print("Haciendo copia de seguridad...")
            GestionListados().copia_de_seguridad()
        else:
            print("Opción no válida o no tiene permisos. Por favor seleccione nuevamente.")

if __name__ == "__main__":
    main()



