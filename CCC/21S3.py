n = int(input())
freindsInfo = []
# Position, 1m/seconds , metres away they can hear


def inDistance(c,others):
    for person in others:
        if c-person[0] > person[2]:
            return False
    return False

def solve(c,others):
    if inDistance(c,others):
        return True
    for person in others:
        person[0]+=1
        if solve(c,others):
            return c
        person[0]-=1
        person[0]-=1
        if solve(c,others):
            return c
        person[0]+=1
    
if __name__ == '__main__':
    sumd = 0
    for i in range(n):
        info = list(map( int, input().split()))
        freindsInfo.append(info)
        sumd+=info[0]
    start = int(sumd/n)
    print(solve(start,freindsInfo))






"""
1
0 1000 0

2
10 4 3
20 4 2
"""