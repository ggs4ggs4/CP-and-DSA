n=int(input())
arr=list(map(int,input().split()))
mini=max(arr)
for i in range(n):
    if i != n-1:
        if arr[i]>=arr[i+1] and arr[i]<=2*arr[i+1] or arr[i]<=arr[i+1] and 2*arr[i]>=arr[i+1]:
            ans = (arr[i]+arr[i+1])//3
            if (arr[i]+arr[i+1])%3:
                ans+=1
        else:
            ans = max(arr[i],arr[i+1])//2
            if max(arr[i],arr[i+1])%2:
                ans+=1
        if ans<mini:
            mini=ans
        if len(arr)>=3 and i!=0:
            p1=max(arr[i-1],arr[i+1])-min(arr[i-1],arr[i+1])
            p2=min(arr[i-1],arr[i+1])
            p2+=p1//2
            if p1%2:
                p2+=1
            if p2<mini:
                mini=p2
min1=min(arr[:2])
min2=max(arr[:2])
for i in range(2,n):
    if arr[i]<=min1:
        min2=min1
        min1=arr[i]
    elif arr[i]<=min2:
        min2=arr[i]
ans=min1//2
if min1%2:
    ans+=1
ans+=min2//2
if min2%2:
    ans+=1
if ans<mini:
    mini=ans
print(mini)
            
