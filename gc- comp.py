from Bio import SeqIO

filename = raw_input("File:")



def gc (some):
    print (float(some.count("G") + some.count("C")) / len(some)) * 100

for record in SeqIO.parse(filename, 'fasta'):
    print record.id,
    gc(record.seq)

