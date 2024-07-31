#entrada del dato
frase=input("Decime algo y te calculo cual es tu tiempo estandar en hablar: ")

#separamos por espacios
palabras_separadas=frase.split(" ")

#usamos el len() para ver la cantiada de palabras
cantidad_de_palabras_separadas=len(palabras_separadas)

#en caso de tener mas de 120 le decimos que pare
if cantidad_de_palabras_separadas >120:
    print("Para flaco que es un toston")

#calculamos el tiempo que tarda
print(f"Dijiste {cantidad_de_palabras_separadas} palabras y tardarias {cantidad_de_palabras_separadas/2} segundos en decirlo")
print(f"Santy lo diria en {cantidad_de_palabras_separadas*100 //2*1.3/100} segundos mas rapido")

