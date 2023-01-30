n=int(input())
for i in range(n):
    l,d=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    flag=0
    for i in range(l):
        if arr[i]+d>arr[i+l]:
            print("NO")
            flag=1
            break
    if flag==1:
        continue
    print("YES")
