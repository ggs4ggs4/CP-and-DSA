n=int(input())
for i in range(n):
    l=int(input())
    arr=list(map(int,input().split()))
    firstnon0=-1
    nozer=0
    for j in range(l-1):
        if arr[j]!=0 and firstnon0==-1:
            firstnon0=j
        elif arr[j]==0 and firstnon0!=-1:
            nozer+=1
        nozer+=arr[j]
    print(nozer)
