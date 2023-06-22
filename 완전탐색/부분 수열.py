from itertools import combinations
N, S = map(int, input().split())
num = list(map(int, input().split()))
count = 0
for i in range(1, N+1):
    com = []
    com = list(combinations(num, i))
    for j in range(len(com)):
        if sum(com[j]) == S:
            count += 1

print(count)
