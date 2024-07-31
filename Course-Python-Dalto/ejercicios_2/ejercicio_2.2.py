#creando una funcion que nos devuelva los numeros primos
#entre 0 y el argumento que le pasemos

#crear un funcion que verifique si un numero es primo
def es_primo(num):
    #verificamos que el numero pasado no sea divisible entre 2 y el mismo numero -1
    for i in range(2,num-1):
        if (num%2==0): 
            #si es divisible por alguno retorna false y termina el bucle 
            return False
        # si termina el bucle significa que no es divisible por lo tanto es primo
    return True

#creamos una funcion que devuelve toda la lista con los primos
def primos_hasta(num):
    #creamos la lista
    primos=[]
    for i in range(3,num+1):
        #verificamos si es primo
        resultado=es_primo(i)
        if(resultado==True):
            #en caso de serlo se agrega a la lista
            primos.append(i)
    #devolvemos la lista de los primos
    return primos 

#desempaquetamos
resultado= primos_hasta(5)
#mostramos resultados
print(resultado)
            
    