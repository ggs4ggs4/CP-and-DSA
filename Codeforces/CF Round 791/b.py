n,q=map(int,input().split())
arr=list(map(int,input().split()))
arrUpdates=[-1]*n
lastfull=-1
lastfullqnumber=-1
s=sum(arr)
for qnum in range (q):    
    query=list(map(int,input().split()))
    if query[0]==2:
        s=n*query[1]
        print(s)
        lastfull=query[1]
        lastfullqnumber=qnum
    else:
        s+=query[2]
        if arrUpdates[query[1]-1]<lastfullqnumber:
            s-=lastfull
        else:
            s-=arr[query[1]-1]
        arr[query[1]-1]=query[2]
        arrUpdates[query[1]-1]=qnum
        print(s)
