import sys
input = sys.stdin.readline
row, col = map(int, input().split())
ful_lst = [list(map(int, input().split())) for i in range(row)]
lst = []
for i in range(row):
    
