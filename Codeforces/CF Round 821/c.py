import sys
t=int(input())

for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    first=[]
    later=[]
    print(n-1)
    if (arr[0]+arr[-1])%2==0:
        for i in range(0,n-1):
            if (arr[i]+arr[-1])%2==0:
                first.append([i+1,n])
        for i in range(1,n-1):
            if (arr[-1]+arr[i])%2==1:
                later.append([1,i+1])
        for i in first:
            print(i[0],i[1])
        for i in later:
            print(i[0],i[1])
    else:
        
        for i in range(1,n):
            if (arr[0]+arr[i])%2==1:
                first.append([1,i+1])
        for i in range(1,n-1):
            if (arr[i]+arr[0])%2==0:
                later.append([i+1,n])
        for i in first:
            print(i[0],i[1])
        for i in later:
            print(i[0],i[1])
