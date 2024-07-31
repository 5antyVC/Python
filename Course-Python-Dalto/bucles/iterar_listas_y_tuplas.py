#todo esto funciona igual para tuplas y en
# animales = {"perro","gato","loro", "cocodrilo"}
# numeros = {52,16,14,72}
animales = ["perro","gato","loro", "cocodrilo"]
numeros = [52,16,14,72]

#recorriendo la lista animales
for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")
    
#recorriendo la lista de numeros y multiplicando por 10
for numero in numeros:
    resultado=numero*10
    print(f"El numero multiplicado por 10 es {resultado}")
    
#iterando 2 listas del mismo tamaño al mismo tiempo 
for numero, animal in  zip(animales, numeros):
    print(f"recorriendo lista 1: {animal}")
    print(f"recorriendo lista 2: {numero}")
    
for num in range(5): #como un array
    print(num)
    
#forma no optima de recorrer listas (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer lista
for num in enumerate(numeros):
    indice=num[0]
    valor=num[1]
    print(f"El indice es {indice} y el valor es {valor}")
    
#usando el for/else 
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")