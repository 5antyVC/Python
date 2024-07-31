with open("archivos\\texto_python.txt","a", encoding="UTF-8") as archivo:
    #usando un bucle para agregar varias lineas
    
    #para que empiece en linea nueva
    archivo.write("\n") 
    for i in range(5):
        archivo.write(f"linea {i+1} agregada\n")