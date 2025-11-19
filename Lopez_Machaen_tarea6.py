#1. Construye una lista que funcione como un conjunto (set). Esto es, construye una función a la que le pasas una lista y un elemento que agregar pero sólo lo agregue si no existe dentro de la lista, también hay que hacer una función que agregue valores (si la llave no existe hay que agregarla y si ya existe hay que sobre-escribir su valor).
lista=[1,2,3]
def conjunto(lista, elemento):
    if elemento not in lista:
        lista.append(elemento)
    else:
        if elemento in lista:
            pass
    return lista
print(conjunto(lista, 4))


#2. Construye dos listas que funcionen juntas como un diccionario. Por ejemplo, simular el diccionario 
    #d = {'uno':1, 'dos':2, 'tercero':3}
    #Utilizando las listas debe poder responder
    #"la llave uno, tiene valor 1"
    #Sugerencia, usar el método index de las listas para buscar la llave y luego el índice para buscar el valor correspondiente.

orden=["uno", "dos", "tres"]
num=[1,2,3]

def dictionary(llaves):
    di=""
    if llaves in orden:
        indice = orden.index(llaves) 
        valor = num[indice]  
        return f"La llave {llaves}, tiene valor {valor}"

    #return llaves, valor 
print(dictionary("dos"))


#3. Hacer una función que convierta un string con nucleótidos en la proteína correspondiente. Sugerencia, crea un diccionario del código genético. Nota: los codones de paro comunmente se sustituyen por un asterisco (*). Tener cuidado con qué pasa si la secuencia no tiene una longitud múltiplo de 3.
geneticCode={"UUU":"Phe", "UUC": "Phe", "UUA": "Leu", "UUG":"Leu", "CUU":"Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu", "AUU":"Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met", "GUU": "Val", "GUC":"Val", "GUA": "Val", "GUG": "Val", "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro", "ACU": "Thr", "ACC":"Thr", "ACA": "Thr", "ACG": "Thr", "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala", "UAU": "Tyr", "UAC": "Tyr", "UAA": "*", "UAG": "*", "CAU": "His", "CAC":"His", "CAA": "Gln", "CAG": "Gln", "AAU": "Asn", "AAC":"Asn", "AAA":"Lys","AAG":"Lys", "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu", "UGU":"Cys", "UGC": "Cys", "UGA": "*", "UGG": "Trp", "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg", "GGU": "Gly", "GGC": "Gly", "GGA":"Gly", "GGG": "Gly"}
def aminoacido(secuencia):
    proteina=""
    for i in range(0, len(secuencia), 3):
        codon=secuencia[i:i+3]
        if len(codon)%3==0:
            proteina+=geneticCode.get(codon,"")
    return proteina
print(aminoacido("AUGCUUAAGCCA"))


