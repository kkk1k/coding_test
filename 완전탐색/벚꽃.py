from itertools import combinations
import sys
input = sys.stdin.readline
num = int(input())
lst = list(map(int, input().split()))
lst_com = [i for i in range(1, num)]
com = list(combinations(lst_com, 3))
ans = []
for i in range(len(com)):
    summ = 0
    a = lst[:com[i][0]]
    b = lst[com[i][0]:com[i][1]]
    c = lst[com[i][1]:com[i][2]]
    d = lst[com[i][2]:]
    ans_a = 1
    ans_b = 1
    ans_c = 1
    ans_d = 1
    for j in range(len(a)):
        ans_a *= a[j]
    for k in range(len(b)):
        ans_b *= b[k]
    for m in range(len(c)):
        ans_c *= c[m]
    for l in range(len(d)):
        ans_d *= d[l]
    summ = ans_a + ans_b + ans_c+ans_d
    ans.append(summ)

print(max(ans))
