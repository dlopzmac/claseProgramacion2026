fasta=open("Helicobacter pylori.fna","r")
print(fasta.read())
encabezado=fasta.readline()
primeralinea=fasta.readline()
print(encabezado)
print(primeralinea)

#for linea in fasta:
 #   print(linea)

salida=open("gene.fna", "w")
salida.write("hola mundo")
salida.write("hola de nuevo")
salida.close()
print(salida)

#para ponerle un salto de línea:
# salida.write("hola mundo!\n")