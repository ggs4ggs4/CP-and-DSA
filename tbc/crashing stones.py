x=int(input())
y=[]
c=0
for i in range(x):
    y.append(int(input()))
y.sort(reverse=True)
for i in y:
    if c<=0:
        c+=i
    else:
        c-=i
print(int((c**2)**(1/2)))
