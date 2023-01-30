import sys
input = sys.stdin.readline
t=int(input())
for asdfghjkl in range (t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    ans=0
    for i in range(k):
        ans+=max(arr[i::k])
    print(ans)
