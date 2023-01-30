t=int(input())
for asdfghjkl in range (t):
    n,r=map(int,input().split())
    if n%2==0:
        maxi=n//2
    else:
        maxi=n//2+1
    if r>maxi:
        print(-1)
    else:
        for i in range(n):
            for j in range(n):
                if i==j and i%2==0 and r>0:
                    print("R",end='')
                    r-=1
                else:
                    print(".",end='')
            print()
            
