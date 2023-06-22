import sys
input = sys.stdin.readline
num = int(input())
lst = [list(map(int, input().split())) for i in range(num)]
# lst2 = sorted(lst, key=lambda x: (x[0], x[1]), reverse=True)
count = []
for i in range(len(lst)):
    keey = 1
    for j in range(len(lst)):
        if lst[j][0] > lst[i][0] and lst[j][1] > lst[i][1]:
            keey += 1
    count.append(keey)

print(*count)
