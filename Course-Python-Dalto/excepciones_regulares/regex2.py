import re

#la cadena en la que se buscan los patrones
text="la fecha es 23/06/2021 y el telefono es +1-555-555-5555"

#el patron a buscar
pattern= r"\d{2}/\d{2}/\d{4}"

#el texto con el que se reemplaza el patron en la cadena de texto
replacement = "Fecha oculta"

#reemplazar todas las apariciones del patron en la cadena
new_text=re.sub(pattern, replacement,text)

#impirimir nuevo texto
print("Texto modificado: ",new_text)