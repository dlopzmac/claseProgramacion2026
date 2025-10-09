#1. MiEsDigito
#Input: un string
#Output: Booleano indicando si el string se compone de puros números
def MiEsDigito(palabra1):
    new1=""
    new1=palabra1.isdigit()
    return new1
#MiEsDigito("1234") == True # probamos si funciona con puros números
print(MiEsDigito("1234") == True)
    #MiEsDigito("abcd") == False # probamos si funciona con puras letras
print(MiEsDigito("abcd") == False)
    #MiEsDigito("123a") == False # probamos si hay números y letras
print(MiEsDigito("123a") == False)
    #MiEsDigito("12a4") == False # probamos que la letra esté a la mitad de los números
print(MiEsDigito("12a4") == False)


#2. MiConteo
    #Input: dos strings, el segundo es sólo un caracter
    #Output: un entero con el número de veces que aparece el segundo string en el primer string
def MiConteo(palabra2,letra):
    new2=""
    new2=palabra2.count(letra)
    return new2
    #MiConteo("hola mundo","o") == 2
print(MiConteo("hola mundo","o") == 2)
    #MiConteo("hola mundo","h") == 1
print(MiConteo("hola mundo","h") == 1)
    #MiConteo("hola mundo"," ") == 1
print(MiConteo("hola mundo"," ") == 1)
    #MiConteo("hola mundo","r") == 0
print(MiConteo("hola mundo","r") == 0)
    #MiConteo("hola mundo","!") == 0
print(MiConteo("hola mundo","!") == 0)
    #MiConteo("hola mundo","") == 0
        #Sale 11 ya que son 11 carácteres
print(MiConteo("hola mundo","") == 0 )
    #MiConteo("","A") == 0
print(MiConteo("","A") == 0)


#3. GCcontent 
# Input: un string con una secuencia de ADN 
# Output: porcentaje de caracteres que son "G" ó "C" 
def GCcontent(bases):
    secuencia = bases.upper() 
    total = secuencia.count("G") + secuencia.count("C")+ secuencia.count("A")+ secuencia.count("T")
    if total == 0:
        return 0  
    basesRequeridas = secuencia.count("G") + secuencia.count("C")
    porcentaje = basesRequeridas / total 
    return porcentaje
# GCcontent("ATGC") == .5 
print(GCcontent("ATGC") == 0.5)
# GCcontent("") == 0 
print(GCcontent("") == 0)
# GCcontent("AAAA") == 0 
print(GCcontent("AAAA") == 0)
# GCcontent("ATgc") == .5 
print(GCcontent("ATgc") == 0.5)
# GCcontent("GGCC") == 1
print(GCcontent("GGCC") == 1)


#4. MiSwapCase
#Input: un string
#Output: un string que invierta las mayúsculas y minúsculas
def MiswapCase(palabra4):
    new4=palabra4.swapcase()
    return new4
print(MiswapCase("mayus")) 
        #Cambia todas a mayúsculas
print(MiswapCase("MINUS"))
        #cambia a minúsculas
print(MiswapCase("InTeRcAlAr"))
        #Intercala


#5. MiCapitalize
    #input:string
    #output:el string modificado para que inicie con mayus
def MiCapitalize(palabra5):
    new5=""
    new5=palabra5.capitalize()
    return new5
print(MiCapitalize("palabra")) 
        #Te cambia la primera a mayus
print(MiCapitalize("hola mundo"))
        #cambia la primera letra de la primera palabra
print(MiCapitalize("Cambia"))
        #Lo deja igual


#6. EsPar
    #Input: Un número entero
    #Output: Imprime si el número es par o impar, no debe regresar nada
def EsPar(número):
    if número % 2 == 0:
        return número
print(EsPar(2))
#Es número par
print(EsPar(7))
#No regresa valor porque no es número par
print(EsPar(553))
#No es número par, así que no regresa nada
print(EsPar(22))
#Es número par