t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    m=0
    for i in range(n):
        if m<arr[i]-(i+1):
            m=arr[i]-(i+1)
    print(m)
