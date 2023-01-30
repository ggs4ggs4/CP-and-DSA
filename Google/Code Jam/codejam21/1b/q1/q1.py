def eqn(v1,v2,v3):
    res = []    
    for n in range(0,40):
        x = (n*360*12*10**10+v2-v1)/11
        b = v1-x
        res.append([x,b,v3])
    return res

def solve(v1,v2,v3):
    xb = []
    xb.append(eqn(v1,v2,v3))
    xb.append(eqn(v1,v3,v2))
    xb.append(eqn(v2,v3,v1))
    xb.append(eqn(v2,v1,v3))
    xb.append(eqn(v3,v2,v1))
    xb.append(eqn(v3,v1,v2))
    for j in xb:
        for i in j:
            if i[0]<0:
                continue
            else:
                if (720*i[0]+i[1])%(360*12*10**10) == i[2] or (720*i[0]-i[1])%(360*12*10**10) == i[2]:
                    return i
    return [0,0]
a=open("txt.txt","w")
t = int(input())
for i in range(t):
    v1,v2,v3 = list(map(int,input().split()))
    res = solve(v1,v2,v3)
    h,m,s,n,th,tm,ts,tn = 0,0,0,0,0,0,0,0
    tn=res[0]
    n=tn%10**9
    ts=tn//10**9
    s=ts%60
    tm=ts//60
    m=tm%60
    h=tm//60
    a.write(f"Case #{i+1}: {int(h)} {int(m)} {int(s)} {int(n)}\n")
a.close()
