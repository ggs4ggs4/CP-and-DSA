from pprint import pprint
d,i,s,v,f = 0,0,0,0,0
street = []
cars = []
inter = {}
ans = []
with open('c.txt','r') as file:
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
        ans.append((k,1,(v[0],str(1))))
    elif len(v)==2:
        ans.append((k,2,(v[0],str(1)),(v[1],str(1))))
    else:
        final = []
        ct = 0
        for i in v:
            final.append((v[ct],'1'))
            ct+=1
        ans.append((k,ct,*final))

with open('outputc.txt','w') as file:
    file.write(str(len(ans)))
    file.write('\n')
    for i in ans:
        file.write(str(i[0]))
        file.write('\n')
        file.write(str(i[1]))
        file.write('\n')
        for j in i[2:]:
            file.write(' '.join(j))
            # print(j)
            file.write('\n')