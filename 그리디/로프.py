rope_num = int(input())
lst=[]
for i in range(rope_num):
    rope_pow = int(input())
    lst.append(rope_pow)
maxi = 0
lst.sort(reverse=True)
for i in range( rope_num,0,-1):
    maxi = max(lst.pop()*i,maxi)
print(maxi)