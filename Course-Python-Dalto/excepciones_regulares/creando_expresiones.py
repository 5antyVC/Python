import re
#detectando un numero CABA y lo ocultamos
texto="Mi numero es: +34 11 4321-4321"

#ocultando un numero con todas las experesiones
pattern=r"\+\d{1,3}\s\d{2}\s\d{4}-\d{4}"

replacement=re.sub(pattern,"(Numero Oculto)",texto)

print(replacement)