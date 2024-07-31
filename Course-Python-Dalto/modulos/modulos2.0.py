#si esta dentro de una carpeta en la misma ruta se importa asi
import funciones_buenas.saludar as saludo_carpeta
print(saludo_carpeta.Saludar("Santy"))

#en el caso que este afuera usamos sys
import sys
sys.path.append("C:\Users\Sonic\Desktop\Python\funciones_buenas")
print(sys.path)