#creando funcion que suma numeros
def sumar_dos():
   #iniciando un bucle
    while True:
        #pidiendo numeros
        a = (input("Numero 1: "))
        b = (input("Numero 2: "))
        try:
            resultado= int(a)+ int(b)
        #si lanza una excepcion, reintento de ingro de datos
        except ValueError as e:
            print("Por favor, introduzca numeros enteros")
            print(f"Error: {e}")
        #si todo salio bien termina el bucle
        else:
            break
        #rara vez usado el finally, pero se ejecuta siempre si es usado
        finally:
            print("Manejo de excepcion finalizado")
    #devolviendo el resultado
    return resultado

#mostrando el resultado
print(sumar_dos())