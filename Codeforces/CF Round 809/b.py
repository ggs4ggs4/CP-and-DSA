import sys
x=10000000
sys.setrecursionlimit(x)
t=int(input())
def sol(arr,i,length,previ):
    if i>=len(arr):
        return length
    if (arr[i]-previ)%2!=1 and previ!=-1:
        return sol(arr,i+1,length,previ)
    if i in foreachindex:
        return max(foreachindex[i])
    else:
        ans1=sol(arr,i+1,length+1,arr[i])
        whenincluded=ans1-length
        ans2=sol(arr,i+1,length,previ)
        whennotincluded=ans2-length
        foreachindex[i]=[whenincluded,whennotincluded]
        return max(ans1,ans2)
for asajsdk in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    foreachindex={}
    prevr={}
    ind=0
    for i in arr:
        if i in prevr:
            prevr[i].append(ind)
        else:
            prevr[i]=[ind]
        ind+=1
    ans=[0]*n
    for i in prevr:
        foreachindex={}
        ans[i-1]=sol(prevr[i],0,0,-1)
    print(" ".join(list(map(str,ans))))
