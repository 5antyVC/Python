#creando una excepcion custom
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"El error es {err}")
 
    
#Lanzando mi propia excepcion       
#raise MiExcepcion("Has cometido un error")

#manejandola        
try:
    raise MiExcepcion("Has cometido un error")
except:
    print("Lee bien el enunciado")
