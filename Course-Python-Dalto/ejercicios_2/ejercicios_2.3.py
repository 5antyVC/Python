#haz la serie de Fibonacci desde el 0 hasta el numero pedido

def fibonnacci(num):
    a,b=0,1
    fibonnacci_lista=[0,]
    for i in range(0,num):
        if b > num:
            return fibonnacci_lista
        else: 
            fibonnacci_lista.append(b)
            a,b = b, a+b

resultado=fibonnacci(34)
print(resultado)