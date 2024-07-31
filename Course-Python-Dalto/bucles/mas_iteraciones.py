#creando las listas
frutas = ["banana", "manzana", "pera", "arandanos"]
cadena="Hola Santy"
numeros=[2,5,8,10]
#evitando que se coma una fruta usando el continue
for fruta in frutas:
    if fruta == "banana":
        continue
    print(f"Me voy a comer una {fruta}")
print("------------------")

#evitar que el bucle siga el else no se ejecuta tampoco
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "pera":
        break
else:
    print("terminado")
    
#recorrer una cadena

for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo
# numeros_duplicados= list()
# for numero in numeros:
#     numeros_duplicados.append(numero*2)
# print(numeros_duplicados)

#lo mismo que arriba en una linea
numeros_duplicados=[x*2 for x in numeros]
print(numeros_duplicados)