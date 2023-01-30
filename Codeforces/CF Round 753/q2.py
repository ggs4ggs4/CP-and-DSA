t=int(input())
for asdfghjkl in range (t):
    x0,n=map(int,input().split())
    s=(n)//4
    sub=(n)%4
    arr=[0,-1,1,4]
    arr[1]-=s*4
    arr[3]+=s*4
    if n==0:
        print(x0)
    elif x0%2==0:
        print(x0+arr[sub])
    else:
        print(x0-arr[sub])
