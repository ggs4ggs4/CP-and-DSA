x=[int(i) for i in input().split()]
Area=x[0]*x[1]

noc=0
while True:
    z=min(x)
    y=x.index(max(x))
    x[y]-=z
    noc+=1
    if 0 in x:
        break
print(noc)
