lines = [line.strip() for line in open("rosa.txt")]

s , t = lines

s_list =  ([s[i:i+len(t)] for i in range (0, len(s))])

for i in range(len(s_list)):
    if t == s_list[i]:
        print i+1,
print


