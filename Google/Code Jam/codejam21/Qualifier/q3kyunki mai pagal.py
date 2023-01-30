tup=tuple()
def result(tupl,n,tc):
    ans=list(range(1,n+1))
    idx = n-2
    for i in tupl[::-1]:
        ans[idx:idx+i] = reversed(ans[idx:idx+i])
        idx -= 1
    print("Case #"+str(tc+1)+":",*ans)
def rec(index, cost, n,tup,tc):
    if (index==-1 or sum(tup)>cost):
        if sum(tup)==cost :
            result(tup,n,tc)
            return 'y'
        else:
            return 'x'
    if sum(tup)==cost and index!=-1:
        return 'x'
    else:
        for i in range (index,0):
            #print("#########",tup,end="$$$$$")
            if (index==-n):
                tup=tuple()
            tup+=(-i,)
            #print("#########",tup)
            ret=rec(index+1,cost,n,tup,tc)
            #print("//////////")
            if ret=='x':
                tup=tup[:-1]
            if  ret=='y':   
                return "y"
        return "x"
        
            
t=int(input())
for i in range(t):
    n,c=map(int,list(input().split()))
    if c<(n-1) or c>(n*(n+1)/2)-1:
        print("Case #"+str(i+1)+": IMPOSSIBLE")
    else:
        rec(-n,c,n,tup,i)
