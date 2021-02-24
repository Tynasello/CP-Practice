g_grid = []

def isValid(xyz):
    if "X" in xyz:
        return False
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    d = y-x
    if y==x+d and z == x+2*d:
        return True
    return False

def getOne(i,xyz):
    if i == 0:
        y = int(xyz[1])
        z = int(xyz[2])
        diff = z-y
        x = y - diff
    elif i == 1:
        x = int(xyz[0])
        z = int(xyz[2])
        y=x+(z-x)/2
    else:
        x = int(xyz[0])
        y = int(xyz[1])
        z = x+2*(y-x)
    xyz = [int(x),int(y),int(z)]
    return xyz
        
def solve(grid):
    if isValid(grid[0]) and isValid(grid[1]) and isValid(grid[2]):
        return grid
    for rowi,row in enumerate(grid):
        x_count = 0
        x_i = 0
        for i,el in enumerate(row):
            if el == 'X':
                x_count+=1
                x_i=i
        if x_count==1:
            grid[rowi] = getOne(x_i,row)
    return grid

if __name__ == '__main__':
    for i in range(3):
        g_grid.append(input().split())
    grid = solve(g_grid)
    for i in range (3):
        for i2 in range (3):
            print(grid[i][i2],end=' ')
        print()
"""
8 9 10
16 X 20
24 X 30

8 9 10
16 18 20
24 27 30
"""
