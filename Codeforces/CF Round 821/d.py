import sys
input = sys.stdin.readline
t=int(input())
for asdfghjkl in range (t):
    n,x,y=map(int,input().split())
    a=input()
    b=input()
    count=0
    ans=0
    modi=[]

    for i in range (n):
        if b[i]!=a[i]:
            count+=1
            modi.append(i)
    if count%2==1:
        print(-1)
    elif x<y:
        for i in range(len(modi)-1):
            if modi[i]!=-1 and modi[i]+1==modi[i+1]:
                modi[i]=-1
                modi[i+1]=-1
                ans+=x
                count-=2
            elif modi[i]!=-1 and (modi[i+1]-modi[i])*x<y:
                modi[i]=-1
                modi[i+1]=-1
                ans+=(modi[i+1]-modi[i])*x
                count-=2
        ans+=(count//2)*y
        print(ans)
    else:
        if count==2 and modi[0]+1==modi[1]:
            if 2*y>x:
                ans=x
            else:
                ans=2*y
        else:
            ans=(count//2)*y
        print(ans)
