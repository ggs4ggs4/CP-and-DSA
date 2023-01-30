t=int(input())
for i in range(t):
    n=int(input())
    dic={}
    l=[]
    readc=0
    for j in range(1,1+n):
        a=list(map(int,input().split()))
        if (a[0]!=0):
            dic[j]=a[1::]
            l.append(j)
        else:
            dic[j]=[-1]
            l.append(j)
    for c in range(0,n):
        #print("##############",l,dic,readc)
        if set(l)=={-1}:
            break
        readc+=1
        for j in range(0,n):
            if (l[j]!=-1):
                for t in range(len(dic[j+1])):
                    i=dic[j+1][t]
                    if i!=-1:
                        if l[i-1]==-1:
                            dic[j+1][t]=-1
                            #print(i,l,dic,readc)
                if set(dic[j+1])=={-1}:
                    l[j]=-1
    if set(l)!={-1}:
        print(-1)
    else:
        print(readc)
