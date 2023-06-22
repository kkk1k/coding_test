import sys
input = sys.stdin.readline
test = int(input())
for i in range(test):
    num = int(input())
    lst = [list(map(int, input().split())) for i in range(num)]
    lst.sort(key=lambda x: x[0])
    ans = 1 #1등을 재껴질 일이 없다.
    ind = 0
    for i in range(1,len(lst)):
        if lst[i][1] < lst[ind][1]:
            ans+=1
            ind=i

    print(ans)
    