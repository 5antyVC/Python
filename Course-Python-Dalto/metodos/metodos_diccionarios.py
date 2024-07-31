diccionario= {
    "nombre": "Santy",
    "apellido":"Velasquez",
    "edad":22,
    "mayor_edad":True
}

#devuelve las keys claves de un key : value
keys = diccionario.keys()

#devuelve el value de la key pedida, devuelve excepcion si no lo encuentra
get_dic=diccionario.get("nombre")

#elimina todo del diccionario
#cleardic=diccionario.clear()

#elimina un elemento del diccionario
elimina_un_elemento=diccionario.pop("mayor_edad")

#nos devuelve el diccionario iterado para que lo podamos recorrer
diccionario_iterable=diccionario.items()

print(diccionario_iterable)