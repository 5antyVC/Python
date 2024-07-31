#creando un conjunto con set())
conjunto = set(["dato1","dato2"]) #los sets no son modificables

#metiendo un conjunto dentro de otro conjunto
conjunto1=frozenset({"dato1","dato2"})#conjunto inmutable
conjunto2={conjunto1,"dato3"}

print(conjunto2)

#teoria de conjuntos
conjunto3={1,3,5,7}
conjunto4={1,3,5}

#verificando si es subconjunto
resultado= conjunto4.issubset(conjunto3)
resultado= conjunto3<=conjunto4

#verificando si es supeconjunto
resultado= conjunto4.issuperset(conjunto3)
resultado= conjunto3>conjunto4

#verificar si hay algun numero en comun
resultado= conjunto4.isdisjoint(conjunto3)



print(resultado)