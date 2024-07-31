lista = ["Santiago","Velasquez", "Calderon", True, 1.76] #es dato tipo list que es una matriz de dimension 1x5
lista1 = ["Santiago","Velasquez", "Calderon", True, 1.76]
lista1[0]="Santy"
tupla = ("Santiago","Velasquez", "Calderon", True, 1.76) #es dato tipo tuple
#tupla[0]="Santy"  # la tupla no se puede modificar

print(lista)
print(tupla[0]) #la tupla aunque se haga con parentesis se muestra con corchetes
print(lista[1])
print(lista1[0])

#set, los set no se pueden modificar y tampoco se puede acceder por indice ademas de no repetir datos se va a imprimir de cualquier orden
conjunto = {"Santiago","Velasquez", "Calderon", True, 1.76,1.76,"Calderon"}
print(conjunto)
#conjunto[1] = "Hola"

#dict estructura key : value
diccionario= {
    'name' : 'Santiago' ,
    'surname' : 'Velasquez',
    'age' : 21.12,
    'emocionado' : True,
    'duname' : 'Santiago' ,
}

print(diccionario['age']+2)