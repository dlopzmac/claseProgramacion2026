
fasta=open("ejemplo.fasta","r")



#1. Para todos los encabezados, lo imprima en el formato
#"Organismo <el nombre del fasta>, contig <el contenido del encabezado, sin el ">""

#2. Para cada línea de secuencia genómica, imprima su contenido de GC en el formato "GC línea <número de línea>: <GC"

#3. Para la primera secuencia de cada segmento, imprima su secuencia complementaria

#4. Imprima el número de línea donde encuentre el codón "ATG" en el formato "ATG en línea <número de línea>"

#5. Calcule el contenido GC total del archivo y lo imprima al final en formato "GC total del archivo: <GC>"
#ejemplo:
#fasta se usa para representar secuencias genómicas
#puede contener las secuencias de muchos organismos, cada una separada con un encabezado que comienza con ">"
#después del encabezado puede haber cualquier número de líneas con secuencias que pueden ser de nucleótidos o de aminoácidos

#Ejemplo:
#Archivo fasta: "humano.fasta"
#>chr 1
#AAAAATGTTTT
##AAAAAAAAAAA
#>chr 2
#GGGGGGGGGGG
#AAAAAACCCCC
#atgCCCCCCCC
#AAAAAACCCCC
#atgCCCCCCCC

#nos debe de imprimir:
#Organismo humano, contig chr1
#GC línea 2: .09
#TTTTTACAAAA
#ATG en línea 2
#GC línea 3: 0
#Organismo humano, contig chr2
#GC línea 5: 1
#CCCCCCCCCCC
#GC línea 6: .81
#ATG en línea 6
#GC línea 7: .45
#GC línea 8: .81
#ATG en línea 8
#GC total del archivo: .53

#(2 a 8 puntos según la dificultad)
#6. Para el formato que te toca, explicar el nombre, extensión del archivo, para qué se usa, en qué consiste (qué reglas debe seguir el archivo para cumplir el formato) y un ejemplo. 

#(2) fna
#(2) faa
#(3) genbank
#(4) fastq
#(4) gff3
#(6) Multiple Alignment Format
#(6) Newick
#(6) ClustalW
#(6) sam
#(8) json
#(8) xml