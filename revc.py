from string import maketrans

##f_o = open("rrevc.txt","r")
line = "CGCTCTGGCACTATTCCCTGCCTCATTCCATTACCGGATCTCTTTCCGCCAT"
print line
print "|" * len(line)
print line[::-1].translate(maketrans("ACGT","TGCA"))

