import sys
import itertools
import copy
sun = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
nPr = list(itertools.permutations(sun, 3))
remove_nPr = copy.deepcopy(nPr)
input = sys.stdin.readline
num = int(input())
lst = [list(map(str, input().split())) for i in range(num)]
for i in range(num):
    a = lst[i][0][0]
    b = lst[i][0][1]
    c = lst[i][0][2]

    for j in nPr:
        strike = 0
        ball = 0
        if a == j[0]:
            strike += 1
        if b == j[1]:
            strike += 1
        if c == j[2]:
            strike += 1
        if a == j[1] or a == j[2]:
            ball += 1
        if b == j[0] or b == j[2]:
            ball += 1
        if c == j[0] or c == j[1]:
            ball += 1

        if strike != int(lst[i][1]) or ball != int(lst[i][2]):
            if j not in remove_nPr:
                continue
            remove_nPr.remove(j)

print(len(remove_nPr))
