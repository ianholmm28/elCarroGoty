from logs import log

def reinicioDeContraseña():
    print("para poder autentificar que la cuenta es suya vamos a pedir los siguientes datos")
    arch = open("cuentas.cvs", mode="rt")
    Cuenta = False
    try:
        Usuario = input("ingrese el numero de usuario")
        for linea in arch:
            CuentaAux = linea.strip().split("/")
            if Usuario == CuentaAux[0]:
                Cuenta = CuentaAux
        if Cuenta == False:
            raise ValueError
    except ValueError:
        print("ese nombre de usuario no pertenece a ninguna cuenta")
    else:
        UsuarioNom = Cuenta[0]
        Errores = 3    
        try:
            if Errores == 0:
                print("se a quedado sin intentos mande un mensaje a atencion al cliente")
                print("1. Si 2. No")
                try:
                    op=int(input("seleccione la opcion que quiere"))
                    if op < 1 and op > 2:
                        raise ValueError
                except ValueError:
                    print("ingrese Un numero que este en las opciones")
                    if op == 1:
                        # op=EnviarMensajeAAC()
                        print("debig")
                    if op == 2:
                        return   
            Dni = input("ingrese su Dni")
            if Dni == Cuenta [2] :
                print("el Dni es valido")
            else:
                raise ValueError
            
        except ValueError:
            print("el Dni no es valido")
            Errores -= 1
        else:
            arch.close()

            NuevaContraseña = SeguridadDeContraseña()
            Cuenta[1] = NuevaContraseña
        
            arch = open("cuentas.cvs", mode="r", encoding="utf-8")
            LineasActualizadas = [] 

            for linea in arch:
                datos = linea.strip().split("/")
            
                if datos[0] == Usuario:
                    nueva_linea = "/".join(Cuenta) + "\n"
                    LineasActualizadas.append(nueva_linea)
            
                else:    
                    LineasActualizadas.append(linea)
            arch.close()

            arch = open("cuentas.cvs", mode="w", encoding="utf-8")

            for linea in LineasActualizadas:
                arch.write(linea)

            arch.close()
            print("Contraseña actualizada correctamente.")
                
            log("reiniciodecontraseña",3,UsuarioNom)
            return 

def SeguridadDeContraseña():
    while True:
        Contraseña=input("ingrese la contraseña:")
        try:
            if len(Contraseña)<8:
                raise IndexError
        except IndexError:
            print("la Contraseña es demasiado corta")
            continue
        else:
            try:
                SimbolosEspeciales=["@", "!", "?", "#", "$", "¿", "¡", "&", "%", "(", ")", "=",".",",",";",":"]
                Comprobacion={"Simbolos Especiales":False,"Numeros":False,"Letras":False,"Mayusculas":False}
                for Caracter in range(len(Contraseña)):
                    aux=Contraseña[Caracter]
                    
                    if aux in SimbolosEspeciales:
                        Comprobacion["Simbolos Especiales"]=True
                    if aux.isdigit() == True:
                        Comprobacion["Numeros"]=True

                    if aux.isalpha() == True:
                        Comprobacion["Letras"]=True

                    if aux.isupper() == True:
                        Comprobacion["Mayusculas"]=True
                
                ErrorCount=0
                for Claves in Comprobacion:    
                    if Comprobacion[Claves] == False:
                        if ErrorCount==1:
                            Falta+=(f",{Claves}")
                        else:
                            Falta=(f"{Claves}")
                            ErrorCount=1
                    
                if ErrorCount == 1:
                    raise ValueError
            
            except ValueError:
                print(f"la contraseña no es suficientemente segura le faltan {Falta}")
            else:
                print("la contraseña es segura")
                break
    return Contraseña
