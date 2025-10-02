for var in range(0,10):
    if var < 5:
        pass    
        print(var)

#1.Determinar si es par
numero=12340.6
    #extraer último dígito
ult=str(numero)[-1]
if int(ult) in [0,2,4,6,8]: 
    print("es par")
else:
    print("es impar")

print(ord('a'))
print(chr(97))

#2.implementar capitalize
palabra="Hyuka"
inicial=palabra [0]
mayus=inicial.upper()
nueva=mayus+palabra[1:]
print(nueva)

    #pasar a mayúscula sin usar upper()
codigo=ord(inicial)-32
mayuscula=chr(codigo)
print(mayuscula)

#checar inicial es minúscula
Ascii=ord(inicial)
if Ascii in range(97,123):
    mayuscula=chr(codigo)
else:
    mayuscula=inicial


