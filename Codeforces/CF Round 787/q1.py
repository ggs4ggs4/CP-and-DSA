t=int(input())
for asdfghjkl in range (t):
    a,b,c,x,y=map(int,input().split())
    x-=a
    y-=b
    if x<=0 and y<=0:
        print("YES")
    elif x<=0 and y<=c:
        print("YES")
    elif y<=0 and x<=c:
        print("YES")
    elif x>0 and y>0 and x+y<=c:
        print("YES")
    else:
        print("NO")
