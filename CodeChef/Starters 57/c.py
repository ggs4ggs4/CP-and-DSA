
t=int(input())
for asdfghjkl in range (t):
    a,b=map(int,input().split())
    if a%2==1 and b%2==1:
        print("No")
    else:
        if a==0 or b==0:
            print("No")
        elif a==1 or b==1:
            print("No")
        else:
            print("Yes")
