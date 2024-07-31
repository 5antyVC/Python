#cambiar el tipo de dato de una columna

import pandas as pd
df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")

#convertir a string los datos de la columna edad
# df["edad"] = df["edad"].astype(str)
# print(type(df["edad"][0]))

#reemplazando los datos por otro
df["nombre"].replace("Santy","Santiago",inplace=True)
# print(df["nombre"])

#no mostrando filas que tienen datos faltantes
df= df.dropna()

#no mostrando columnas que tienen datos faltantes
df= df.dropna(axis=1)

#no mostrando filas con datos repetidos
df = df.drop_duplicates()

#crando un CSV con el dataframe resultante(limpio)
df.to_csv("archivos_problemas_resueltos\\datos_limpio.csv")