from sys import setrecursionlimit
setrecursionlimit(3*100000)
t=int(input())

def paths(inputpath,length,node):
    if node not in ptoc:
        print(length)
        print(inputpath)
    else:
        paths(inputpath+" "+str(ptoc[node][0]),length+1,ptoc[node][0])
        if len(ptoc[node])>1:
            for each in ptoc[node][1::]:
                paths(str(each),1,each)
for asdfghjkl in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    ptoc={}
    haschild=dict(zip(list(range(1,n+1)),[0]*n))
    leafs=0
    for i in range (n):
        if a[i]==i+1:
            root=i+1
        elif a[i] in ptoc:
            ptoc[a[i]].append(i+1)
        else:
            ptoc[a[i]]=[i+1]

        haschild[a[i]]=1
    for each in haschild:
        if haschild[each]==0:
            leafs+=1
    
    if root not in ptoc:
        print(1)
        print(1)
        print(1)
    else:
        print(leafs)
        paths(str(root)+" "+ str(ptoc[root][0]),2,ptoc[root][0])
        if len(ptoc[root])>1:
            for each in ptoc[root][1::]:
                paths(str(each),1,each)
    print()
