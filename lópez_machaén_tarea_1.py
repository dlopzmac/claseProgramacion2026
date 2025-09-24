
#)1.-¿Cómo podemos concatenar un string a un número?
a="CYJ"
cb=2
print(a+str(cb))
#)2.-¿De què tipo son las variables?
a="1"
print(type(a))
#str (al ponerle las comillas, se vuelve un str)
B=1.0
print(type(B))
#float (a python no le importa si el decimal es un 0, con tal de que aparezca el punto, lo marcará así)
c=1.5+True
print(type(c))
#float (da 2.5)
d=1.5+2.5
print(type(d))
#float (da 3.0; a python no le importa si el decimal es un 0, con tal de que aparezca el punto, lo marcará así)
e=1+True
print(type(e))
#int (da 2)
f=False+True
print(type(f))
#int (da 0)
g=True+0
print(type(g))
#int (da 1, ya que vuelve el bolean en int)
#3.-Manipulando la variable"palabra", convertirla:
palabra1="the killa"
print(palabra1.replace('e','3').replace('i','1').replace('a','4'))
palabra2=" casual"
print(palabra2.strip())
palabra3="cAsUaL"
print(palabra3.swapcase())
palabra="casual"
print(palabra.capitalize())
#4.-Explica qué hacen los métodos:
    # a. count() (para contar el número de veces que un elemento específico aparece) 
print(palabra.count('a'))
    #b. find() (se utiliza para devolver el índice de la string creada donde se encuentra la substring)
print(palabra.find('su'))
    # c. isdigit() (se utiliza para verificar si todos los caracteres presentes en la cadena son dígitos numéricos)
BlueHour='553'
print(BlueHour.isdigit())
    #d. replace() (reemplaza una frase específica con otra frase específica)
txt1="new rules"
print(txt1.replace('new','no'))
#5. ¿Qué problema tiene declarar estas variables?
#   oración larga = 'hola mundo'
oracionlarga="hola mundo"
        #(el nombre de la variable cuenta con espacios)
#   palabra = 'hola' 'mundo'
palabras="hola"
palabras2="mundo"
     #(se le está asignando dos valores, cuando sólo debería ser a uno)
#6.- fstrings (Es una función insertar el valor de variables y expresiones dentro de cadenas de texto;sirve para representar y manipular secuencias)
accion='leave'
who='Monster'
titulo=f'cant We Just {accion} the {who} Alive?'
print(titulo)