#1. Crear una lista vacía y llenarla con los números del 1 al 50 (1,2,3,...,48,49,50). 
lista=list()
for numero in range(1,51):
    lista.append(numero)
    print(lista)
#2. Crear una lista vacía y llenarla con los números múltiplos de 5 del 2 al 50 (5,10,15,...,40,45,50). 
lista1=list()
for i in range(1,11):
    lista1.append(i*5)
    print(lista1)
#3. Hacer un programa que imprima 
for f in range(0,10):
    print("*" * f)
#4. Investigar cómo se usa un ciclo while y hacer un programa que imprima los números del 1 al 10. 
    #Lo repite dependiendo si es verdadera.
x = 1
while x<7:
    x +=5
    print(x)
    

