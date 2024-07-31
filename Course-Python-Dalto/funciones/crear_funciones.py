#creando una funcion simple
def saludar():
    print("Hola master")
    
#ejecutando la funcion simple 
saludar()

#funcion con parametro

def saludar_nombre(nombre,sexo):
    sexo=sexo.lower()
    if (sexo == "mujer"):
       adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "titan"
    else: 
        adjetivo = "crack"
    print(f"Hola {nombre}, {adjetivo}")
    
saludar_nombre("Santy", "hOmbre")

#crear una funcion que devuelva valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1=num-2
    c2=num
    c3=num-5
    contraseña=f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
    
password =crear_contraseña_random(98)
frase=f"Tu contraseña nueva es: {password}"
print(frase)