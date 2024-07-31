#promedios de duracion
otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_promedio=4
dalto_curso=1.5

#duracion promedio
crudo_promedio=5
crudo_dalto=3.5



#diferecias con min
diferencias_con_min=100 - (dalto_curso / otros_cursos_min *100)
diferencias_con_max=100 - (dalto_curso *1000 // otros_cursos_max /10) # en estos casos para quitar todos los decimales si sale un 0.1052 se multiplica por 1000 que nos daria un 105.2% y se divide entre 10
diferencias_con_promedio=100 - (dalto_curso / otros_cursos_promedio *100)

#calculando el tiempo vacio promedio
diferencias_crudos_promedio=100 - (otros_cursos_promedio *1000 // crudo_promedio /10)
diferencias_crudos_dalto=100 - (dalto_curso *1000 // crudo_dalto /10)


#diferencias de duracion
print("--------------------")
print("el curso de dalto dura: ")
print(f" - un {diferencias_con_min}% menos que el mas rapido")
print(f" - un {diferencias_con_max}% menos que el mas rapido")
print(f" - un {diferencias_con_promedio}% menos que el mas rapido")
print("--------------------")

#mostrando las diferencias de crudos
print(f"un crudo promedio es {diferencias_crudos_promedio}% de tiempo vacio")
print(f"el crudo dalto es {diferencias_crudos_dalto}% de tiempo vacio")
print("--------------------")

#mostrando diferencias si el curso fuera de 10h
print(f"Ver 10h de este curso equivale a {otros_cursos_promedio*100 //dalto_curso /10} horas de otros cursos")
print(f"Ver 10h de otros cursos equivale a {dalto_curso*100 //otros_cursos_promedio /10} horas de otros cursos")
print("--------------------")


