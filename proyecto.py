with open("ecoli.fasta", "r") as f:
    seq=""
    for linea in f:
        if not linea.startswith(">"):
            seq+=linea.strip()
    rna=seq.replace("T","U")
geneticCode={"UUU":"F", "UUC": "F", "UUA": "L", "UUG":"L", "CUU":"L", "CUC": "L", "CUA": "L", "CUG": "L", "AUU":"I", "AUC": "I", "AUA": "I", "AUG": "M", "GUU": "V", "GUC":"V", "GUA": "V", "GUG": "V", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "ACU": "T", "ACC":"T", "ACA": "T", "ACG": "T", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*", "CAU": "H", "CAC":"H", "CAA": "Q", "CAG": "Q", "AAU": "N", "AAC":"N", "AAA":"K","AAG":"K", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "UGU":"C", "UGC": "C", "UGA": "*", "UGG": "W", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GGU": "G", "GGC": "G", "GGA":"G", "GGG": "G"}

#1. Inician con ATG
prot=[]
orfs=[]
for i in range(len(rna) - 2):
    if rna[i:i+3] == "AUG":
        for j in range(i + 3, len(rna) - 2, 3):
            if rna[j:j+3] in ["UAA", "UAG", "UGA"]:
                longitud = j + 3 - i
                if 30 <= longitud <= 90:
                    prot.append(rna[i:j+3])
                    orfs.append({"start": i+1, "end": j+3, "rna": rna[i:j+3], "strand": "+"})
                break

#proteínas traducidas
def traducir(rnam):
    prot = ""
    for i in range(0, len(rnam), 3):
        codon = rnam[i:i+3]
        aa = geneticCode.get(codon, "")
        prot += aa
    return prot
for rnam in prot:
    proteina = traducir(rnam)
    print(proteina)


with open("resultados.gff", "w") as gff:
    gff.write("##gff-version 3\n")
    for n, o in enumerate(orfs, 1):
        gff.write(
            f"ecoli\tORFfinder\tCDS\t{o['start']}\t{o['end']}\t.\t+\t0\tID=orf{n}\n"
        )
#b. Hacer una gráfica con el contenido GC del genoma en ventanas de 50bp
ventana = 50
gcontenido = []
posicion = []
for i in range(0, len(rna) - 50,50):
    contador= rna[i:i + 50]
    gc = contador.count("G") + contador.count("C")
    porcentaje = (gc / 50)*100
    gcontenido.append(porcentaje)
    posicion.append(i)

import matplotlib.pyplot as plt 
plt.plot(posicion, gcontenido)
plt.xlabel("Posición en el genoma (bp)")
plt.ylabel("Contenido GC (%)")
plt.title("Contenido GC del genoma en ventanas de 50bp")
plt.show()
