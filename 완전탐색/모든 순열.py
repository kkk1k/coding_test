n = int(input())
lst = []
chk = [False]*(n+1)


def recur(num):
    if num == n:
        print(*lst)
        return
    for i in range(1, n+1):
        if chk[i] == False:
            lst.append(i)
            chk[i] = True
            recur(num+1)
            lst.pop()
            chk[i] = False


recur(0)
