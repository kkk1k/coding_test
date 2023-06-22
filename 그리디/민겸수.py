import sys
input = sys.stdin.readline().rstrip()
lst = list(input)
mini = ""
maxi = ""
num = 0
for i in range(len(lst)):
    if lst[i] == 'M':
        num +=1
    else:
        if 