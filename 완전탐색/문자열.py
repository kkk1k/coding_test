import sys
input = sys.stdin.readline
a, b = map(str, input().split())
lst = []
minu = len(b)-len(a)
for j in range(minu+1):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i+j]:
            count += 1
    lst.append(count)
print(min(lst))
