def binary(k,j):
    ans=15
    lower=1
    upper=31
    #print(k,j,end=" ")
    if j==0:
        return -1,-1
    while True:
        
        if k//(2**ans)<j and k//(2**(ans-1))>=j:
            break
        elif k//(2**ans)<j:
            upper=ans-1
            ans=(upper+lower)//2
        else:
            lower=ans+1
            ans=(upper+lower)//2
    #print(ans)        
    return ans,k//(2**ans)
t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    cost=0
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            continue
        else:
            res,arr[i]=binary(arr[i],arr[i+1])
            cost+=res
            if res==-1:
                print(-1)
                break
    else:
        print(cost)
