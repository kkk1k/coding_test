screen_length ,pocket= map(int,(input().split()))

lst_screen = []
lst_pocket = []
for i in range(1,screen_length+1):
    lst_screen.append(i)

for i in range(1, pocket+1):
    lst_pocket.append(i)

apple = int(input())
num = 0
for i in range(apple):
    spot = int(input())
    if spot >= lst_pocket[0] and spot <= lst_pocket[-1]:
        continue
    elif spot > lst_pocket[-1]:
        diff = spot-lst_pocket[-1]
        num += diff
        for i in range(len(lst_pocket)): 
            lst_pocket[i]+=diff  
    elif spot < lst_pocket[0]:
        diff = lst_pocket[0]-spot
        num += diff
        for i in range(len(lst_pocket)): 
            lst_pocket[i]-=diff

print(num)