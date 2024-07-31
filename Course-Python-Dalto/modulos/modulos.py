# import modulo_saludar as m_saludar si queremos importar todo el archivo
#si solo queremos importar una funcion
from modulo_saludar import Saludar as Saludo_normal, saludar 
import modulo_saludar as m_saludo
#tambien se puede importar como import * pero sobrecarga el programas
#las funciones con mayusculas
saludo =Saludo_normal("German")
# las variables en minusculas 
print(saludar)
print(saludo)

# print(type(modulo_saludar)) de tipo namespace o modulo y crea una carpeta pycache
#para ver todas las propiedades del modulo
# print(dir(Saludo_normal))

#accedemos al modulo del nombre llamado
print(m_saludo.__name__)

#accedemos al modulo del nombre
print(__name__)