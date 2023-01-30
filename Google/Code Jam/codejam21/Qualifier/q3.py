tup=tuple()
def result(tupl,n,tc):
    ans=list(range(1,n+1))
    idx = n-2
    for i in tupl[::-1]:
        ans[idx:idx+i] = reversed(ans[idx:idx+i])
        idx -= 1
    print("Case #"+str(tc+1)+":",*ans)

            
t=int(input())
for i in range(t):
    n,c=map(int,list(input().split()))
    if c<(n-1) or c>(n*(n+1)/2)-1:
        print("Case #"+str(i+1)+": IMPOSSIBLE")
    else:
        ans=[1]*(n-1)
        ans[0]=n
        index=0
        while(sum(ans)!=c):
            if sum(ans)<c:
                index+=1
                ans[index]=n-index
            else:
                extra=sum(ans)-c
                ans[index]-=extra
        else:
            result(ans,n,i)
