# Solve Avent of Code Day 4
# Lauryne Feuvrier _ 25.09.25

# Partie 1 
res = 0
grid = []
with open("input4.txt") as file:
    for line in file:
        grid.append(line.strip())

rows = len(grid)
cols = len(grid[0])
directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

for i in range(rows) : 
    for j in range(cols) : 
        if grid[i][j]=='X':
            for di,dj in directions :             
                if 0 <= i+3*di < rows and 0 <= j+3*dj < cols and(grid[i+di][j+dj]=='M') and (grid[i+2*di][j+2*dj]=='A') and (grid[i+3*di][j+3*dj]=='S'):
                    res += 1

print(res)

# Partie 2
res2 = 0

X_directions = [[1,1],[-1,-1],[1,-1],[-1,1]]

for i in range(1,rows-1) : 
    for j in range(1,cols-1) : 
        if grid[i][j]=='A' :
            if (grid[i+1][j+1]=='M' and grid[i-1][j-1]=='S')or(grid[i+1][j+1]=='S' and grid[i-1][j-1]=='M'):
                if (grid[i-1][j+1]=='M' and grid[i+1][j-1]=='S')or(grid[i-1][j+1]=='S' and grid[i+1][j-1]=='M'):
                    res2 += 1

print(res2)

