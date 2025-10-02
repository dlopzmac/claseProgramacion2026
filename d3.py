#HACER QUE THAT MAMADA QUEDE DEL OTRO PINCHE PERRO LADO 
palabrad="553a"
for letra in palabrad:
    if ord(letra) in range(0,54):
        print("es número")
    else:
        print("es letra")
for i in range(10):
    print(" "*(10-i)+"*" * i)


#SPLIT
oracion="welcome to the jungle"
p=oracion.split(" ")
print(p)

oraciones="Welcome to the jungle"
listapalabras=list()
palabra=" "
for letter in oraciones:
    if letter==" ":
        listapalabras.append(palabra)
        palabra=" "

    else:
        palabra+=letter
listapalabras.append(palabra)
print(listapalabras)


#LAS PUTAS MINÚSCULAS REVISAR
frase="hola Mundo"
esminuscula=True
for letras in frase:
    if ord(letras) in range(ord("A"),ord("Z")+1):
        print("True")
    else:
        esmayuscula=False
    print("False")
print(esminuscula)


#volverlo en minúsculas oh . . .
frase2="Hola Mundo"
minus=""
for i in frase2:
    if ord(i) in range(ord("A"),ord("Z")+1):
        i=chr(ord(i)-ord("A")+ord("a"))
    minus+=i
print(minus)


#volverlo en mayúscula :(
fr="arthur morgan"
mayus=""
for l in fr:
    if ord (l) in range(ord("a"), ord("z")+1):
        l=chr(ord(l)-ord("a")+ord("A"))
    mayus+=l
print(mayus)


#intercambiar esa madre
ayora="tOMORROWxtOGETHER?"
eso=""
for a in ayora:
    if ord(a) in range(ord("a"),ord("z")+1):
        a=chr(ord(a)-ord("a")+ord("A"))
    elif ord(a) in range(ord("A"),ord("Z")+1):
        a=chr(ord(a)-ord("A")+ord("a"))
    eso+=a
print(eso)


#reverso como el payaso del rodeo 
dilafrase="adios mundo"
    #generar buffer vacío
nueva=""
    #iterar sobre las letras de atrás hacia adelante
for numletra in range(-len(dilafrase)+1,1):
    nueva+=dilafrase[-numletra]
print(nueva)


#encuéntralo jaaaa
palabra="no te vayas chavo"
for pos in range(len(palabra)):
    if palabra[pos] == 'a':
        posicion = pos
        print(posicion)

#remove prq find no funcionó
for pos in range(len(palabra)):
    if not palabra[pos] == 'o':
        posicion = pos
        print(posicion)


#reemplazar :(
reem="a"
for pos in range(len(palabra)):
    if palabra[pos] == 'o':   

        posicion = pos
        print(posicion)

