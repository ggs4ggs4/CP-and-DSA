t=int(input())
for asdfghjkl in range (t):
    x,y=map(int,input().split())
    if x>y:
        print(0,0)
    elif x==y:
        print(1,1)
    else:
        if y%x!=0:
            print(0,0)
        else:
            ap=y//x
            a=0
            print(1,ap)
            
