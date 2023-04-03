import itertools as it
a,b = input("Write the word and the number of permutations: ").split()
p = sorted(list(map("".join,list(it.permutations(a,int(b))))))
for i in p:
    print(i)

