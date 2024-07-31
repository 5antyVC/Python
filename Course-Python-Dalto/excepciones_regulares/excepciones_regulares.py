import re

texto= """Hola soy. Santy ESTA. es la linea 1.
esta es la linea 252552 ves tengo mas lineas.


Y aqui estamos en la linea 3 esto se acaba"""

#encuentra la primera coincidencia
# resultado= re.search("est",texto)

#encuentra todas las coincidencias
# resultado= re.findall("esta",texto,flags=re.IGNORECASE) #las flags ignoran las mayusculas en este caso

#\d -> busca digitos numeros del 0 - 9
# resultado= re.findall(r"\d",texto)

#\D -> busca TODO MENOS digitos numeros del 0 - 9
# resultado= re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [A-Z, a-z, 0-9, _]
# resultado= re.findall(r"\w",texto)    

#\W -> busca TODO MENOS caracteres alfanumericos [A-Z, a-z, 0-9, _]
# resultado= re.findall(r"\W",texto)

#\s -> busca espacios en blanco, tabs y saltos de linea
# resultado= re.findall(r"\s",texto) 

#\s -> busca TODO MENOS espacios en blanco, tabs y saltos de linea
# resultado= re.findall(r"\S",texto)

#. -> buscamos TODO MENOS saltos en linea
# resultado= re.findall(r".",texto)

#\n -> buscamos saltos en linea
# resultado= re.findall(r"\n",texto)

#\ -> cancelamos caracteres especiales,cancelamos la funcion del punto y buscando puntos
# resultado= re.findall(r"\.",texto)

#creando una cadena que busque un numero seguido de un punto y un espacio
# resultado=re.findall(r"\d.\s",texto)

#buscando el principio de una linea
#^ -> busca el principio de una linea, buscando si la palabra esta al principio de la linea
# resultado=re.findall(r"^esta",texto,flags=re.M) re.M hace que cada linea sea independiente

#buscando el final de una linea
#$ -> busca el final de una linea, buscando si la palabra esta al final de la linea
# resultado=re.findall(r"acaba$",texto,flags=re.M) re.M hace que cada linea sea independiente

#{n} -> busca n-cantidad de veces el valor de la izquierda
# resultado=re.findall(r"\d{3}\s",texto)

#{n,m} -> al menosn, como maximo m
# resultado=re.findall(r"\d{1,4}",texto)

# | -> busca una cosa o la otrea
resultado=re.findall(r"\d{1,4}|Hola",texto)

print(resultado)