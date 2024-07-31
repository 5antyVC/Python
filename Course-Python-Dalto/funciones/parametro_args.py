#formna no optima de sumar valores
def suma(a,b):
    return  a+b

resultado = suma(5,3)
print(resultado)


#tampoco es optimo
def suma_optima(lista):
    numeros_sumados=0
    for numero in lista:
        numeros_sumados=numeros_sumados+numero
    return numeros_sumados

resultado1 = suma_optima([1,2,3])
print(resultado1)

#utilizando el operador args como argumento
def suma_args(nombre,*numeros):
    return f"{nombre}, la suma de los numeros es: {sum(numeros)}"

resultado2= suma_args("Santy",1,2,3)
print(resultado2)