from functools import lru_cache
@lru_cache(1000)
def solve(a,b,tup,prod):
    print(a,"||||||||||||||||",b)
    if sum(a)==prod:
        tup+= (sum(a),)
        return tup
    t=sum(a)/prod
    if t<2:
        return tup
    for i in range(len(a)-1,-1,-1):
        
        
        if a[i]>t:
            continue
        b+=(a[i],)
        prod*=a[i]
        tup=solve(a[:i]+a[i+1:],b[::],tup,prod)
        prod/=a[i]
        b=b[:-1]
    return tup

t = int(input())
for i in range(t):
    prime_arr = []
    m = int(input())
    for j in range(m):
        pi,mi = map(int,input().split())
        temp_arr = [pi for x in range(mi)]
        prime_arr.extend(temp_arr)
    tup=tuple()
    res = solve(tuple(sorted(prime_arr)),tuple(),tup,1)
    if res==tuple():
        print("Case #"+str(i+1)+": "+str(0))
    else:
        print("Case #"+str(i+1)+": "+str(max(res)))
