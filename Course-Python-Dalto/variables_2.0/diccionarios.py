#creando diccionarios con dict()
diccionario= dict(nombre="Santy",apellido="Velasquez")

#las listas no pueden ser claves si usamos frozenset para meter conjunto
diccionario={frozenset(["Santy","VC"]):"nick"}

#creando diccionario con fromkeys por defecto con none
diccionario= dict.fromkeys(["nombre","apellido"])

#creando diccionario con fromkeys por defecto con por teclado
diccionario= dict.fromkeys(["nombre","apellido"],"introduzca")

print(diccionario)