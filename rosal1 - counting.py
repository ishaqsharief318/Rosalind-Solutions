f_o = open("rosa.txt", "r")
for line in f_o:
    print line.count("A")
    print line.count("C")
    print line.count("G")
    print line.count("T")
