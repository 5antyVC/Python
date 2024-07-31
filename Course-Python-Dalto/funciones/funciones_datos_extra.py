#creando una funcion con 3 parametros
def frase(nombre,apellido,adjetivo):
    return f"Hola, {nombre} {apellido}, {adjetivo}"

frase_resultante= frase("Santy","Velasquez","Capo")
print(frase_resultante)

#utilizando keywords arguments
def frase1(nombre,apellido,adjetivo):
    return f"Hola, {nombre} {apellido}, {adjetivo}"
frase_resultante1= frase(adjetivo="tonto",nombre="Santy",apellido="Velasquez")
print(frase_resultante1)
