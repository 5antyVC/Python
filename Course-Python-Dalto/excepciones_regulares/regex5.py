import re
text="Esto es un ejemplo de una pagina web https://www.example.com y tambien podemos visitar"

pattern="https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result=re.findall(pattern,text)

print(result)