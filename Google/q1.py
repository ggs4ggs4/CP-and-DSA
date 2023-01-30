def solve(arr,k):
    arr.sort()
    idx_arr = []
    tmp=sorted(list(set(arr)))
    tmp.insert(0,0)
    tmp.append(k+1)
    for i in range(len(tmp)-1):
        if (tmp[i]==tmp[i+1]-1):
            continue
        idx_arr.append([tmp[i],tmp[i+1]-1])
    lens=[]
    m=-1
    for i in idx_arr:
        d=i[1]-i[0]
        if i[0]==0:
            lens.append(i[1]-i[0])
        elif i[1]==k:
            lens.append(i[1]-i[0])
        else:
            if d%2==0:
                lens.append((i[1]-i[0])//2)
            else:
                lens.append(((i[1]-i[0])//2)+1)
        if d>m:
            m=d
    lens.sort()
    if len(lens)>=2 and lens[-1]+lens[-2]>m:
        return lens[-1]+lens[-2]
    else:
        if m==-1:
            return 0
        return m

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    v=solve(arr,k)
    print("Case #"+str(i+1)+": "+str(v/k))
