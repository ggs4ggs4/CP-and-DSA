import sys
input = sys.stdin.readline
read=open('txt.txt','r')
input = read.readline
out=open('out.txt','w')
print = out.write
t = int(input())
for case in  range(t):
    n=int(input())
    tx=[]
    ty=[]
    sum_oat_x=0
    sum_oat_x2=0
    sum_oat_y=0
    sum_oat_y2=0
    for i in range(n):
        a,b=map(int,input().split())
        tx.append(a)
        ty.append(b)
        sum_oat_x+=a
        sum_oat_x2+=a**2
        sum_oat_y+=b
        sum_oat_y2+=b**2
        sum_oat_x=sum_oat_x%1000000007
        sum_oat_x2=sum_oat_x2%1000000007
        sum_oat_y=sum_oat_y%1000000007
        sum_oat_y2=sum_oat_y2%1000000007
    q=int(input())
    wx=[]
    wy=[]
    for i in range(q):
        a,b=map(int,input().split())
        wx.append(a)
        wy.append(b)
    total=0
    for i in wx:
        total+= (i**2)*n
        total=total%1000000007
        total+= sum_oat_x2
        total=total%1000000007
        total-= 2*i*sum_oat_x
        total=total%1000000007
    for i in wy:
        total+= (i**2)*n
        total=total%1000000007
        total+= sum_oat_y2
        total=total%1000000007
        total-= 2*i*sum_oat_y
        total=total%1000000007
    print('Case #'+str(case+1)+': '+str(total)+'\n')
            
read.close()
out.close()

