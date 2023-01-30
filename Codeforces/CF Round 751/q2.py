t=int(input())
for asdfghjkl in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    queries=[]
    maxlevel=0
    q=int(input())
    for i in range(q):
        q1,q2=map(int,input().split())
        queries.append((q1,q2))
        if q2>maxlevel:
            maxlevel=q2
    base={}
    for i in range(n):
        if arr[i] in base:
            base[arr[i]][0]+=1
            base[arr[i]][1]+=[i+1]
        else:
            base[arr[i]]=[1,[i+1]]
    levels=[base]
    l=0
    for i in range(maxlevel+1):
        newdict={}
        for j in levels[i]:
            if levels[i][j][0] not in newdict:
                newdict[levels[i][j][0]]=(levels[i][j][0],levels[i][j][1])
            else:

                newdict[levels[i][j][0]]=(newdict[levels[i][j][0]][0]+levels[i][j][0],newdict[levels[i][j][0]][1]+levels[i][j][1])
        levels.append(newdict)
        l+=1
        if levels[-1]==levels[-2]:
            break
    for i in queries:
        q1,q2=i
        if q2>=l:
            ansdict=levels[-1]
        else:
            ansdict=levels[q2]
        for j in ansdict:
            if q1 in ansdict[j][1]:
                print(j)
                
