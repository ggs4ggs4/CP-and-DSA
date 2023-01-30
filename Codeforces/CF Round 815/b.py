t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr2=[]
    for i in range(n):
        arr2.append([arr[i],i])
    arr2.sort(reverse=True)
    maxi=-1
    mini=-1
    if (arr2[0][1]==0 or arr2[0][1]==n-1) and (arr2[-1][1]==0 or arr2[-1][1]==n-1):
        cost=arr2[0][0]-arr2[-1][0]
        print(max(cost+arr2[0][0]-arr2[-2][0],cost+arr2[1][0]-arr2[-1][0]))
    else:
        print(arr2[0][0]*2-arr2[-1][0]*2)
