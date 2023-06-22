num = int(input())
d = [-1]*5001
d[3] = 1
d[5] = 1
for i in range(6, num+1):
    if i == 7:
        continue
    if d[i-3] < 0 or d[i-5] < 0:
        d[i] = 1 + max(d[i-3], d[i-5])
        continue
    d[i] = 1 + min(d[i-3], d[i-5])

print(d[num])
