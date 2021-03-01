"""
find the minimal ammoung of operations needed to convert one string into another
you can replace, insert, or delete characters
"""


def solve(row, col):
    res = 0
    if col == 0 and row != 0:
        res = row
    elif row == 0 and col != 0:
        res = col
    if col == 0 or row == 0:
        res = 0
    else:
        if s2[row - 1] == s1[col - 1]:
            res = solve(row - 1, col - 1)
        else:
            delet = solve(row, col - 1)
            replace = solve(row - 1, col - 1)
            insert = solve(row - 1, col)
            res = min(delet, replace, insert) + 1
    dp[row][col] = res
    return res


s1 = " pairs"
s2 = " cars"

n1 = len(s1)
n2 = len(s2)
dp = [[0 for i in range(n1)] for i in range(n2)]
print(solve(n2 - 1, n1 - 1))
