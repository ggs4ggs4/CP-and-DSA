t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    arr2=[arr[0]]
    for i in range(1,n):
        arr2.append(arr[i]-arr[i-1])
    print(max(arr2))
