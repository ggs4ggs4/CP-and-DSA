def mini(list1):
    mx=max(list1[0],list1[1])
    secondmax=min(list1[0],list1[1])
    n =len(list1)
    for i in range(2,n):
        if list1[i]>mx:
            secondmax=mx
            mx=list1[i]
        elif list1[i]>secondmax:
            secondmax=list1[i]
    return (mx,secondmax)

t=int(input())
c=0
for i in range(t):
    n,h=map(int,input().split())
    dmg=list(map(int,input().split()))
    mx,secondmx=mini(dmg)
    if h<=mx:
        print(1)
    elif h%(mx+secondmx)==0:
        print(2*(h//(mx+secondmx)))
    else:
        q=2*(h//(mx+secondmx))
        r=h-q/2*(mx+secondmx)
        if(r<=mx):
            print(q+1)
        else:
            print(q+2)
