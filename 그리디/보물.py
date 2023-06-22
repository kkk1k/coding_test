num = int(input())
A = sorted(map(int, input().split()))
B = list(map(int, input().split()))
sum = 0

for i in range(num):
    maxi = max(B)
    sum += A[i]*maxi
    B.remove(maxi)

print(sum)
