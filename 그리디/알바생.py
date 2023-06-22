num = int(input())
lst = []
for i in range(num):
    lst.append(int(input()))
lst.sort(reverse=True)
sum = 0
for i in range(len(lst)):
    tip= lst[i]-i
    if tip <=0:
        tip = 0
    sum += tip

print(sum)