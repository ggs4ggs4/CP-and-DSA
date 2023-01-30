t=int(input())
for sdfghbjn in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    l=[]
    c=0
    for i in range(n):
        ind=a[i::].index(b[i])+i
        if ind!=i:
            c+=1
            l.append((i+1,ind+1,ind-i))
            a.pop(ind)
            a.insert(i,b[i])
    print(c)
    for i in range(c):
        print(l[i][0],l[i][1],l[i][2])
