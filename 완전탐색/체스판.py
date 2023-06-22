import sys
input = sys.stdin.readline
row, col = map(int, input().split())
ful_lst = [list(input().rstrip()) for i in range(row)]
ans = []
min1 = row-7
min2 = col-7
for k in range(min1):
    for m in range(min2):
        count1 = 0
        count2 = 0
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        if ful_lst[i+k][j+m] != 'B':
                            count1 += 1
                        if ful_lst[i+k][j+m] != 'W':
                            count2 += 1
                    else:
                        if ful_lst[i+k][j+m] != 'W':
                            count1 += 1
                        if ful_lst[i+k][j+m] != 'B':
                            count2 += 1
                else:
                    if j % 2 == 0:
                        if ful_lst[i+k][j+m] != 'W':
                            count1 += 1
                        if ful_lst[i+k][j+m] != 'B':
                            count2 += 1
                    else:
                        if ful_lst[i+k][j+m] != 'B':
                            count1 += 1
                        if ful_lst[i+k][j+m] != 'W':
                            count2 += 1
        ans.append(count1)
        ans.append(count2)

print(min(ans))
