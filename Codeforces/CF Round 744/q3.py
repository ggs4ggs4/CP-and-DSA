t=int(input())
for sdfghbjn in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    l=[1]
    l2=[]
    c=0
    ind=a.index(1)-1
    if(ind==-1):
        for i in a:
            print(i,end=" ")
        print()
        continue
    b=ind+2
    while(ind>0):
        m=a[0]
        prevind=ind
        for i in range(ind,-1,-1):
            if(a[i]<m):
                m=a[i]
                ind=i-1
        if(m==a[0]):
            if 1<=prevind:
                l2+=a[1:prevind+1]
            break
        l.append(m)
        if ind+2<=prevind:
            l2+=a[ind+2:prevind+1]
    l.append(a[0])
    for i in l:
        print(i,end=" ")
    if len(l2)!=0:
        for i in l2:
            print (i,end=" ")
    if len(a)>b:
        for i in a[b::]:
            print(i,end=" ")
    print()
