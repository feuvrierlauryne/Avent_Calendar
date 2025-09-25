# Solve Avent of Code Day 1
# Lauryne Feuvrier _ 25.09.25

from collections import Counter

# Partie 1: 

Col_G = []
Col_D = []

with open("input1.txt") as file:
    for line in file:
        g, d = line.split()
        Col_G.append(int(g))
        Col_D.append(int(d))

Col_G.sort()
Col_D.sort()

res1 = sum(abs(a - b) for a, b in zip(Col_G, Col_D))
print(res1)

# Partie 2:

counter_D = Counter(Col_D)

res2 = 0

for a in Col_G :
    res2 += a * counter_D.get(a,0)

print(res2)