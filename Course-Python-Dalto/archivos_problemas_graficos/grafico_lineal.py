import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\entradas.csv")

#creando el grafico
sns.lineplot(x="fechas",y="entradas",data=df)

#creando un punto en el maximo
plt.plot("1 - 9",17,"o")

#mostrando el grafico
plt.show()

