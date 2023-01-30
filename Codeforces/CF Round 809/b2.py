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
for base in range(2,t+1):
    x=base**base
    print(x,base,"===========================")
    for asajsdk in range(x):
    
        arr1=[1]*base
        ind=base-1
        while asajsdk!=0:
            arr1[ind]+=asajsdk%base
            asajsdk//=base
            ind-=1
        n=base
        arr=arr1
        foreachindex={}
        prevr={}
        print(arr)
        for i in range(n):
            if arr[i] in prevr:
                prevr[arr[i]].append(i)
            else:
                prevr[arr[i]]=[i]
        ans=[0]*n
        for i in prevr:
            foreachindex={}
            ans[i-1]=sol(prevr[i],0,0,-1)
        print(" ".join(list(map(str,ans))))
