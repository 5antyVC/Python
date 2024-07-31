#creamos una lista con list()
lista=list(["Hola","Santy",22])

#devuelve la cantidad de elementos de la lista
cantidad_elementos=len(lista)

#agregamos un elemento a la lista
lista.append(True)

#agregamos un elemento a la lista en un indice especifico
lista.insert(2,"Nuevo")

#agregamos varios elementos a la lista
lista.extend([False,30])

#eliminando elementos de la lista dependiendo de la lista 
lista.pop(0) #si ponemos -1 se elimina el ultimo de la lista -2 penultimo etc

#remove remueve por su valor, si lo encuentra manda excepcion
lista.remove(False)

#clear elimina todos los elementos de la lista
# lista.clear()

#sort ordena la lista pero solo con numeros y los booleanos False,True siempre van primero en caso de haberlos
# lista.sort() 

#reverse = True da la vuelta del orden
#   lista.reverse()

print(lista)

