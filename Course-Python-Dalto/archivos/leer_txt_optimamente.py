with open("archivos\\texto_python.txt", encoding="UTF-8") as archivo:
    
    contenido=archivo.read()
    
    #mostramos contenido
    print(contenido)
#no es necesario cerrarlo con with open