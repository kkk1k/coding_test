num = int(input())
lst = [int(input()) for i in range(num)]
d = [1]*10001
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 4
d[5] = 5
for i in range(6, 10):
    d[i] += d[i-2]
for i in range(6, 10):
    d[i] += d[i-3]


