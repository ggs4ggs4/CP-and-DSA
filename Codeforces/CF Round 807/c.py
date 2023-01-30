t=int(input())

for inaj in range(t):
    n,c,q=map(int,input().split())
    originaln=n
    s=input()
    cutmap={}
    for i in range(c):
        start,end=map(int,input().split())
        cutmap[(n,n+(end-start))]=(start-1,end-1)
        n+=1+(end-start)
    #print(cutmap)
    for j in range(q):
        ind=int(input())-1
        while True:
            if ind>=0 and ind<originaln:
                break
            for i in cutmap.keys():
                if ind>=i[0] and ind<=i[1]:
                    #print(ind,", new ind=",end='')
                    ind=cutmap[i][0]+ind-i[0]
                    #print(ind)
                    break
            
        print(s[ind])
