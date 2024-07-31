diccionario ={
    "Nombre":"Santy",
    "Apellido":"Velasquez",
    "Edad":22
}
#recorriendo un diccionario para obtener las claves
for key in diccionario.items():
    key
    print(f"la clave es: {key}")

#reccoriendo un diccionario con items() para obtener el clave:valor
for datos in diccionario.items():
     key=datos[0],
     value=datos[1]
     print(f"la clave es: {key} y el valor es: {value}")