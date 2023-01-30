t=int(input())
for asdfghjkl in range (t):
    n,m=map(int,input().split())
    arr=list()
    temp=[0]*n
    ls=[0]*n
    rs=[0]*n
    ks=[0]*n
    for i in range(m):
        l,r,k=map(int,input().split())
        if temp[l]==1:
            
        arr.append([r-l,l,r,k])
        ls[l]=1
        rs[r]=1
        ks[]=1
    ans=[0]*n
    arr.sort()
    for i in arr:
        













arr=[4,3,7,0,2]
s=0
def sum(x,i):
    global s
    if i==5:
        s+=x
    else:
        sum(x,i+1)
        sum(x^arr[i],i+1)
sum(0,0)
print(s)
