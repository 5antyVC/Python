cadena1="santiago"
cadena2="Velasquez"

dir(cadena1) #nos muestra todo lo que podemos hacer con ese dato ---> dir es una funcion

#Metodos
resultado= cadena1.upper() #pone todo en mayusculas
resultado2= 'aguacate'.upper() #pone todo en mayusculas
resultado3= cadena1.lower() #pone todo en minusculas

primer_letra_mayuscula=cadena1.capitalize()#pasa todo a lower y convierte la primera en mayuscula

busqueda_find=cadena1.find("ago")#busca en la cadena segun el indice, devuelve -1 si no encuentra un valor  

busqueda_index=cadena1.index("a")#busca en la cadena segun el indice, devuelve excepcion

es_numerico=cadena1.isnumeric()#nos dice si el dato es numerico osea si es un texto pero que contiene SOLO numeros

es_alfanumerico=cadena1.isalpha()#solamente son validos los caracteres de las A-Z ni caracteres especiales 

contar_coincidencias=cadena1.count('a')#cuenta la cantidad de veces que hay una cadena de caracteres

contar_caracteres=len(cadena1)#len es una funcion y cuenta los caracteres

empieza_con=cadena1.startswith("s")#mira si empieza con un caracter

terminaa_con=cadena1.endswith("o")#mira si termina con un caracter

cadena_nueva=cadena1.replace("a","e")#si encuentra el valor en la cadena original lo reemplaza en la copia
#muy util para reemplazar comas (,) por espacios ( )

cadena_separada=cadena1.split("a")#separa por caracter devolviendo una matriz(lista)
print(cadena_separada)