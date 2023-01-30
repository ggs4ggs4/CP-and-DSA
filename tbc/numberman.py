n=int(input())
l=[]
c=[]
a=0
for i in range(n):
    l.append(int(input()))
l.sort()
c=0
co=0
lst=[]
for i in l:
    if c==0:
        c=i
        co+=1
    elif c==i:
        co+=1
    else:
        lst.append([co,c])
        c=i
        co=1
lst.append([co,c])
lst.sort()
for i in lst:
    for j in range(i[0]):
        print(i[1])
        
    
    
