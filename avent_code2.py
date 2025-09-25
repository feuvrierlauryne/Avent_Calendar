# Solve Avent of Code Day 2
# Lauryne Feuvrier _ 25.09.25

res1 = 0
res2 = 0

def check(list):
    diff_niv = []
    for i in range (len(list)-1):
        diff_niv.append(list[i+1]-list[i])
    croissant = all(d > 0 for d in diff_niv)
    decroissant = all(d < 0 for d in diff_niv)
    ecarts_valides = all(1 <= abs(d) <= 3 for d in diff_niv)
    return ((croissant or decroissant) and ecarts_valides)

# Partie 1 & 2: 
with open("input2.txt") as file:
    for line in file:
        rapport = list(line.split())

        list_niv = []      

        for niveau in rapport: 
            list_niv.append(int(niveau))

        if check(list_niv): 
            res1 += 1
        
        # added for part 2
            res2 += 1
        else: 
            j=0
            for j in range(len(list_niv)):
                reduced_list = list_niv[:j] + list_niv[j+1:]
                if check(reduced_list):
                    res2+=1
                    break
                    
print(res1)
print(res2)