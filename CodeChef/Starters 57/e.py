import sys
input = sys.stdin.readline
t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    prefix=[arr[0]]
    for i in range(1,n):
        prefix.append(prefix[i-1]+arr[i])
    qn=int(input())
    for i in range(qn):
        tempded=0
        tc=0
        p,k=map(int,input().split())
        temp=[]
        for i in range(n):
            if arr[i]%p==0:
                temp.append(arr[i])
                if i<k:
                    tempded+=arr[i]
                    tc+=1
        temp.sort(reverse=True)
        print(prefix[k-1]+sum(temp[:tc])-tempded)
            
