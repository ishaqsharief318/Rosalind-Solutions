def generations(n, k):
    gens = []
    for i in range(n):
        if i < 2:
            gens.append(1)
        else:
            gens.append(gens[-1] + gens[-2]*k)
    return gens

print generations(int(30), int(3))[-1]
