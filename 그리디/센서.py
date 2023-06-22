import sys
input = sys.stdin.readline
num = int(input())
zip = int(input())
sensor = sorted(map(int, input().split()))
if zip >= num:
    print(0)
else:
    diff = [sensor[i+1]-sensor[i] for i in range(num-1)]
    diff.sort()
    for i in range(1, zip):
        diff.pop()
    print(sum(diff))
