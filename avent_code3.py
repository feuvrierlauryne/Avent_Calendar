# Solve Avent of Code Day 3
# Lauryne Feuvrier _ 25.09.25

import re

file = open("input3.txt","r").read()

# Partie 1 :
res1 = 0
pattern = 'mul\([0-9]{1,3},[0-9]{1,3}\)'
all_mul = re.findall(pattern, file)

for mul in all_mul:
    n,m = re.findall('[0-9]{1,3}',mul)
    res1 += int(n) * int(m)

print(res1)

# Partie 2 
res2 = 0
i=0
active = True

while i<len(file):
    mul = re.match(pattern, file[i:])
    if file.startswith("do()",i):
        i+=4
        active = True
    elif file.startswith("don't()",i):
        i+=7
        active = False
    elif mul:
        if active:
            n,m = re.findall('[0-9]{1,3}',mul.group())
            res2 += int(n) * int(m)
        i += mul.end()
    else:
        i+=1
print(res2)
        