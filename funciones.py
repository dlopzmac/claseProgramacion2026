#minúsculas
palabra="HoLa"
minus=""
def minusc(palabra):
    minus=palabra.lower()
    return minus
print(minusc("hoLa MUunDO"))


#reemplazar
word= "hola Mundo"
busqueda="s"
reemplazo="$"
nueva="" 
def new(word):
    nueva=word.replace("s","$").replace("v","♡")
    return nueva
print(new("loser=lover"))


#reemplazar otra vez pero bien
def new(word1, busquedas, reemplazos):
    nueva="" 
    nueva=word1.replace(busquedas, reemplazos)
    return nueva
print(new("hola mundo","o","0"))


print(lower("hola"=="hola"))