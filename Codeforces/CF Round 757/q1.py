t=int(input())
for asdfghjkl in range (t):
    n,l,r,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr2=[]
    le=0
    for i in arr:
        if i<l or i>r:
            continue
        else:
            arr2.append(i)
            le+=1
    arr2.sort()
    s=0
    ind=0
    while( le-ind>0 and s+arr2[ind]<=k):
        s+=arr2[ind]
        ind+=1
    print(ind)
