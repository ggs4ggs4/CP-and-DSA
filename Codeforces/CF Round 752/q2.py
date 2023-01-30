t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    if n%2==0:
        print("YES")
    else:
        lag=0
        for i in range(n-1):
            if arr[i]>=arr[i+1]:
                lag=1
                break
        if lag==1:
            print("YES")
        else:
            print("NO")            
    
