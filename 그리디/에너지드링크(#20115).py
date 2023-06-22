num = int(input())
lst = list(map(int, input().split()))
lst.sort()
sum = 0
sum = lst.pop()
for i in range(len(lst)):
    sum += lst.pop()/2

print(sum)
