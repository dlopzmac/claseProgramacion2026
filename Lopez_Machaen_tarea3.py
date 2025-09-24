#1. Investigar cómo se usa el operador módulo (modulus) en python, explicarlo con sus palabras y poner un ejemplo. (1 punto)
    #Te devuelve el residuo de una divisón.
print(8%6)
#2. Crear una lista vacía y llenarla con los números pares del 2 al 50 (2,4,6,8,...,48,50) utilizando un for y un condicional para controlar que sólo los pares se agreguen.  (2 puntos)
for l in range(1,51):
    if l % 2 == 0:
        print(l)
#3. Investigar para qué sirve el comando "break" en un for, explicarlo con sus palabras y hacer un ejemplo. (1 punto)
    #Es para terminar un ciclo de forma inmediata.
for cyj in range(20):
    if cyj ==11:
        break
    print(cyj)
#4. Programar el método find de los strings a mano. (2 puntos) Sugerencia: utilizar break cuando encuentren lo que buscan
palabra="banana"
for letra in palabra:
    if letra =="a":
        print("se encuentra en la posición: ",palabra.index(letra))
        break
#5. Imprimir todos los números de la siguiente lista utilizando ciclos: (4 puntos)
hk = [ [1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5] ]
for csb in hk:
    for kth in csb:
        print(kth)