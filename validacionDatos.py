def estaEntre(minimo,maximo,mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num>maximo or num<minimo:
                raise ValueError
            break
        except ValueError:
            print("Dato invalido. Intentelo de nuevo.")
    return num

def validarString(opciones, mensaje):
    while True:
        try:
            texto = input(mensaje).lower().strip()
            if texto not in opciones:
                raise ValueError
            break
        except ValueError:
            print("Dato invalido. Intentelo de nuevo.")
    return texto