#generate codon table

bases = ["A","C","U","G"]
codons = [a+b+c for a in bases for b in bases for c in bases]
aasymbols = 'KNNKTTTTIIIMRSSRQHHQPPPPLLLLRRRR*YY*SSSSLFFL*CCWEDDEAAAAVVVVGGGG'
codon_table = dict(zip(codons,aasymbols))

lines = [line.strip() for line in open("rosa.txt")]

f_o = open("prot.txt","a")

string = lines[0]
for i in ([string[i:i+3] for i in range (0, len(string),3)]):
    f_o.writelines(codon_table[i])

f_o.close()

