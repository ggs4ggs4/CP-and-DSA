t=int(input())
for iasadsd in range(t):
    n,k=map(int,list(input().split()))
    s=input()
    mx=n//2
    sc=0
    for i in range(1,n//2+1):
        if s[i-1]!=s[n-i]:
            sc+=1
    if k<=sc:
        print("Case #"+str(iasadsd+1)+':',sc-k)
    else:
        print("Case #"+str(iasadsd+1)+':',k-sc)
