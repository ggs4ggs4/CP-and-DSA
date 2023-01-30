import sys
input = sys.stdin.readline
t=int(input())
for asdfghjkl in range (t):
    n,x,y=map(int,input().split())
    arr=sorted([x,y])
    n2=n
    if (0!=x and 0!=y) or (0==x and 0==y):
        print(-1)
    else:
        while n2>1:
            n2-=arr[1]
        if n2<=0:
            print(-1)
        else:
            ans=[]
            wins=0
            cur=1
            for i in range(n-1):
                ans.append(cur)
                wins+=1
                if wins==arr[1]:
                    #ans.pop()
                    cur=len(ans)+2
                    wins=0
            ans=list(map(str,ans))
            print(" ".join(ans)) 


