t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    br=input()
    dic={}
    out=[]
    #0 is for blue 1 is for red
    for i in range(n):
        if arr[i] in dic:
            if br[i]=='B':
                dic[arr[i]][0]+=1
            else:
                dic[arr[i]][1]+=1
        else:
            if arr[i]>n or arr[i]<1:
                out.append(arr[i])
            if br[i]=='B':
                dic[arr[i]]=[1,0]
            else:
                dic[arr[i]]=[0,1]
    bsum=0
    flag=1
    for i in range(1,n+1):
        if i in dic:
            bsum+=dic[i][0]
        if bsum>i:
            flag=0
            break
    bsum=0
    if flag==1:
        for i in range(n,0,-1):
            if i in dic:
                bsum+=dic[i][1]
            if bsum>n-i+1:
                flag=0
                break
    if flag==1:
        for i in out:
            if i>n and dic[i][1]!=0:

                flag=0
                break
            elif i<1 and dic[i][0]!=0:
                flag=0
                break
    if flag==1:
        print("YES")
    else:
        print("NO")
