t=int(input())
for i in range(t):
    b,a=map(int,input().split())
    b=b//2+1
    a=a//b
    print(a)
