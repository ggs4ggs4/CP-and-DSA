t=int(input())
for i in range(t):
    n=int(input())
    x=[]
    y=[]
    for i in range(n):
        b=list(map(int,input().split()))
        x.append(b[0])
        y.append(b[1])
    x.sort()
    y.sort()
    if n%2==1:
        print(1)
    else:
        print((x[n//2]-x[n//2-1]+1)*(y[n//2]-y[n//2-1]+1))
