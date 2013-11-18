f_o = open("rosalind_dna.txt","r")
for line in f_o:
    line = line.replace("T","U")
print line
