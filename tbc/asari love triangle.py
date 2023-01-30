a=int(input())
b=[int(a) for a in input().split()]
v1,v2,v3=0,0,0
answer='NO'
for z in range(a):
    v1=b[z]
    v2=b[v1-1]
    v3=b[v2-1]
    v4=b[v3-1]
    if v1==v4:
        print('YES')
        break
else:
    print('NO')
