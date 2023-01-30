t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    tarr=sorted(arr)
    if(arr==tarr):
        print("YES")
    else:
        lind=n-1-x+1
        rind=x-1
        if lind>rind:
            print("YES")
        else:
            if(tarr[lind:rind+1]==arr[lind:rind+1]):
                print("YES")
            else:
                print("NO")
