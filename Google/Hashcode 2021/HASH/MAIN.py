from pprint import pprint
d,i,s,v,f = 0,0,0,0,0
street = []
cars = []
inter = {}
ans = []
with open('b.txt','r') as file:
    d,i,s,v,f = map(int,file.readline().split())
    for _ in range(s):
        a = file.readline().split()
        if a[1] not in inter.keys():
            inter[a[1]] = (a[2],)
        else:
            inter[a[1]] = inter[a[1]]+(a[2],)
        street.append((tuple(a[:-1]) + (int(a[-1]),)))
    for _ in range(v):
        a = file.readline().split()
        cars.append(tuple(a))
street = tuple(street)
cars = tuple(cars)
for k,v in inter.items():
    if len(v)==1:
        ans.append((1,(v[0],1)))
    if len(v)==2:
        ans.append((2,(v[0],1),(v[1],1)))

# pprint(street)
# pprint(cars)
# pprint(inter)
# pprint(ans)
print(len(ans))
for i in ans:
    print(i[0])
    for j in i[1:]:
        print(*j)
