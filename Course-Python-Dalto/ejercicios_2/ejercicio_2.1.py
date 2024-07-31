#Un profesor falta y un alumno sera el profesor
#A) Pedir edad y nombre de los alumnos y ordenar de mayor a menor
#B) El mayor es el profesor y el menor el asistente

#funcion para obtener asistente y profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista de compañeros
    compañeros= []
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lista
        compañeros.append(compañero)
    
    #ordenamos de menor a mayor segun su edad   
    compañeros.sort(key= lambda x:x[1]) 
    
    #compañeros[x] devuelve una tupla con  (nombre,edad) y despues accedemos al nombre
    #para definir asistente y profesor
    asistente = compañeros[0][0]#el que sale por menor edad es el primero
    profesor = compañeros[-1][0]#el que tiene mas edad sale el ultimo por eso lo cogemos con -1
    
    #retornamos la tupla
    return asistente,profesor

#desempaquetamos lo que nos da la funcion
asistente,profesor = obtener_compañeros(5)

#mostramos resultado
print(f"El asistente es: {asistente} y el profesor es: {profesor}")
