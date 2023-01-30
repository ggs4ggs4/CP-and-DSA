n=int(input())
lst=[int(i) for i in input().split()]
if lst==[]:
    lst=[int(i) for i in input().split()]
tr=lst[:]
m1=0
for i in range(n):
    for j in range(i,n):
        tr[j]=1-tr[j]
        if tr.count(1)>m1:
            m1=tr.count(1)
    tr=lst[::]
print(m1)

