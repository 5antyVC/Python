#instalar pip si no lo tienes para usar pandas
import pandas as pd

#usando la funcion read_csv para leer un archivo csv
#usando names para el encabezado
# df = pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

# cadena="0123456789"
#si usamos 0:5 arranca en 0 hasta el 5 y si lo dejamos candena[:] recorre todo
# print(cadena[0:5] )

#obteniendo los datos por nombre
nombres=df["nombre"]

#ordenar el df(dataframe) por edad menor
df_ordenado_ascendente=df.sort_values("edad")

#ordenar el df(dataframe) por edad mayor
df_ordenado_descendente=df.sort_values("edad",ascending=False)

#concatenando daframes
df_contatenado = pd.concat([df,df2])

#accediendo a las primeras 3 filas con head()
primer_fila = df.head(2)

#accediendo a las ultimas 3 filas con tail()
ultima_fila = df.tail(2)

#accediendo a la cantidad de columnas y filas con shape
# filas_y_columnas_totales = df.shape 
# filas_totales = df.shape[0]
# columnas_totales = df.shape[1]

#lo mismo de arriba pero desempaquetado
filas_totales,columnas_totales=df.shape

#obteniendo data estadistica del dataframe
df_info=df.describe()

#accediendo a ña edad de la fila 2 
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a un elemento especifico con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todos los apellidos con loc
apellidos_loc= df.loc[:,"apellido"]

#accediendo a todos los apellidos con iloc
apellidos= df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3= df.loc[2,:]

#accediendo a la fila 3 con iloc, funciona igual porque se llama por indice en este caso
fila_3= df.iloc[2,:]

#accediendo a filas donde la edad>21
fila_mayor_30= df.loc[df["edad"]>21,:]

print(fila_mayor_30)



