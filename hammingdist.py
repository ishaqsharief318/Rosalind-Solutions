filename = raw_input("file:")
fo = open(filename,"r")
filecontents = fo.readlines()
string1 = filecontents[0]
string2 = filecontents[1]
count = 0
hamm = 0
while True :
    if string1[count] != string2[count]:
        hamm +=1
    count+=1
    if count == len(string1):
        break
print hamm
