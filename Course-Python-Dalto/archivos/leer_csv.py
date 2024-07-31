#importamos csv para que pueda leer csv
import csv

with open("archivos\\datos.csv") as archivo:
    # print(archivo.read())
    reader = csv.reader(archivo)
    print(reader)
    for row in reader:
        print(row)