#tenemos 2 listas con nombres y apellidos, una tiene nombres y la otra apellidos
#hay que escribir los datos de forma optima en un archivo de texto con un for

#2 listas, una con nombre y otra con apellidos
nombres= ["Santy","Jorge","Juan","Juanma"]
apellidos= ["Velasquez","Sanchez","Gonzales","Garcia"]

#registrar esta informacion en un TXT de forma optima
with open("archivos_problemas_resueltos\\nombre_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son: \n\n")
    [arch.writelines(f"Nombres: {n} \nApellidos: {a}\n---------\n")for n,a in zip(nombres,apellidos)]        
    # igual que la linea de arriva
    # for n,a in zip(nombres,apellidos):
    #     [arch.writelines(f"Nombres: {n} \nApellidos: {a}\n---------\n")]