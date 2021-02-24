l = int(input())
w = int(input())
grid = []
for i in range (l):
    temp = []
    for i2 in range (w):
        temp.append(0)
    grid.append(temp)
n = int(input())
brushes = []


def solve(grid,action):
    direction = action[0]
    index = action[1]-1
    if direction=='R':
        for i in range(w):
            grid[index][i]+=1
    else:   
        for i in range(l):
            grid[i][index]+=1
    return grid

if __name__ == '__main__':
    for i in range(n):
        direction, index = input().split()
        brushes.append([direction,int(index)])
    for brush in brushes:
        grid = solve(grid,brush)
    res = 0
    for row in grid:
        for col in row:
            if col%2!=0:
                res+=1
    print(res)