import math
def check(o):
    for i in range(2,int(math.sqrt(o)//1)+1) :
        if o%i==0:
            return 0
    return 1

t=int(input())
for i in range(t):
    j=int(input())
    s=math.floor(math.pow(j,1/2))
    a=s+1
    b=s
    while(1):
        if check(a):
            break
        a+=1
    while(1):
        if check(b):
            break
        b-=1
    if a*b<=j and a!=b:
        print("Case #"+str(i+1)+": "+str(a*b)+"\n" )
    else:
        a=b
        while(1):
            b-=1
            if check(b):
                break
        print("Case #"+str(i+1)+": "+str(a*b)+"\n" )
