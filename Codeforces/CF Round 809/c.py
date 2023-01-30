t=int(input())
for asd in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if n%2==1:
        i=1
        cost=0
        while i<n-1:
            if max(arr[i-1],arr[i+1])>=arr[i]:
                cost+=max(arr[i-1],arr[i+1])-arr[i]+1
            i+=2
        print(cost)
    else:
        i=1
        cost1={}
        cost=0
        while i<n-1:
            if max(arr[i-1],arr[i+1])>=arr[i]:
                cost+=max(arr[i-1],arr[i+1])-arr[i]+1
            cost1[i]=cost
            i+=2
        i=n-2
        cost2={}
        cost=0
        while i>0:
            if max(arr[i-1],arr[i+1])>=arr[i]:
                cost+=max(arr[i-1],arr[i+1])-arr[i]+1
            cost2[i]=cost
            i-=2
        final=max(cost2.values())
        for i in cost1:
            if i+3 in cost2:
                final=min(final,cost1[i]+cost2[i+3])
            else:
                final=min(final,cost1[i])
        print(final)
