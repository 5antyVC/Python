import re

text="reemplazando todas las vocales por asterisco"

new_text=re.sub("[aeiou]","*",text)
print(new_text)