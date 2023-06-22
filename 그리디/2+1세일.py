import sys
input = sys.stdin.readline
num = int(input())
lst = []
for i in range(num):
    lst.append(int(input()))
lst.sort(reverse=True)
sum = 0
for i in range(len(lst)):
    if i % 3 == 2:
        continue
    sum += lst[i]

print(sum)
