num = int(input())
lst = sorted(map(int,input().split()))
lst2 = []
if num % 2 ==0: # 짝수일 경우은 가장 큰것하고 작은것의 합을 구함
    for i in range(num//2):
        mus = lst[i]+lst[-(i+1)] #mus는 근손실 머신들의 합
        lst2.append(mus)

else: 
    lst2.append(lst[-1])
    for i in range(num//2):
        mus = lst[i]+lst[-(i+2)] #mus는 근손실 머신들의 합
        lst2.append(mus)


print(max(lst2))