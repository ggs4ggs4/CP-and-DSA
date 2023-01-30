t=int(input())
for asdfghjkl in range (t):
    n,k=map(int,input().split())
    h=0
    done=1
    while done<n and done<=k:
        h+=1
        done*=2
    if done>=n:
        print(h)
    else:
        if (n-done)%k==0:
            print(h+(n-done)//k)
        else:
            print(h+1+(n-done)//k)
