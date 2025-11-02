from Usuarios import CrearCuenta,IniciarSesion,VerificarRoleDeUsuario
from funciones_cine import CargarSucursales
from AdminsSettings import MenuAdmin,MenuSuperAdmin,MenuUser

def menuprincipal():
    while True:
        print("1. Crear Cuenta \n2. IniciarSesion")
        try:
            Opcion=int(input("ingrese el numero de la opcion que quiere:"))
            if Opcion < 1 or Opcion > 2 :
                raise ValueError

        except ValueError:
                print("ingrese un numero que este en las opciones")

        else:
            if Opcion == 1:
                CrearCuenta()
                continue
            else:
                Usuario=IniciarSesion()
                break
    Role=VerificarRoleDeUsuario(Usuario)
    print(Role)

    if Role == "User":
        MenuUser(Usuario)
    elif Role == "Admin":
        MenuAdmin(Usuario)
    elif Role == "superAdmin":
        MenuSuperAdmin(Usuario) 


def main():
    menuprincipal()
    


if __name__ == "__main__":
    sucursales = CargarSucursales()
    main()