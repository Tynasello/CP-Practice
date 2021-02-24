# needle permutations and haystack
n = str(input())
h = str(input())
res = 0


def permutate(s):
    if len(s) == 0:
        return [[]]
    first = s[0]
    rest = s[1:]
    withoutFirst = permutate(rest)
    all_permutations = []
    for perm in withoutFirst:
        for i in range(len(perm) + 1):
            withFirst = perm[:i] + [first] + perm[i:]
            if withFirst in all_permutations:
                continue
            all_permutations.append(withFirst)
    return all_permutations


if __name__ == "__main__":
    res = 0
    all_permutations = permutate(n)
    for perm in all_permutations:
        s = ""
        if s.join(perm) in h:
            res += 1
    print(res)

"""
aab
abacabaa
"""