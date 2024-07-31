numeros=[4,7,1,42,15]

#encontrando el numero mayor de una lista
numero_mas_alto=max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de una lista
numero_mas_bajo=min(numeros)
print(numero_mas_bajo)


#reordenamos a 2 decimales
redondeo = round(12.3512554561,2)
print(redondeo)

#retorna False -> 0,vacio, False, None \ numero != 0, True, String
resultado_bool=bool("Hola")
print(resultado_bool)

#retorna True -> si todos los valores son verdaderos
resultado_all=all(["Hola",5,True,0])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)