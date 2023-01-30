import sys
input = sys.stdin.readline
read=open('txt.txt','r')
input = read.readline
out=open('out.txt','w')
print = out.write
t = int(input())
for case in  range(t):
    n=int(input())
    tx={}
    ty={}
    for i in range(n):
        a,b=map(int,input().split())
        if a in tx:
            tx[a]+=1
        else:
            tx[a]=1
        if b in ty:
            ty[b]+=1
        else:
            ty[b]=1
    q=int(input())
    qx={}
    qy={}
    for i in range(q):
        a,b=map(int,input().split())
        if a in qx:
            qx[a]+=1
        else:
            qx[a]=1
        if b in qy:
            qy[b]+=1
        else:
            qy[b]=1
    total=0
    for i in tx:
        for j in qx:
            total+= ((i-j)**2 )*tx[i]*qx[j]
            total=total% 1000000007
    for i in ty:
        for j in qy:
            total+= ((i-j)**2 )*ty[i]*qy[j]
            total=total% 1000000007
    print('Case #'+str(case+1)+': '+str(total)+'\n')
            
read.close()
out.close()

