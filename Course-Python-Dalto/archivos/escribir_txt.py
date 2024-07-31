#abrimos el archivo y le damos el permiso "W" de escribir por defecto viene el de lectura
#sino encuentra el archivo lo crea
with open("archivos\\texto_python.txt","w", encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    # archivo.write("Escribiendo")1
    
    #agregando lineas con writelines
    archivo.writelines(["Escribiendo con writelines\n","Espaciado"])