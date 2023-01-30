t=int(input())
for asdfghjkl in range (t):

    arr=list(map(int,input().split()))
    s=input()
    umax=0
    dmax=0
    lmax=0
    rmax=0
    lrpos=0
    udpos=0
    for i in s:
        if i=="U":
            udpos+=1
            if udpos>umax:
                umax=udpos
        elif i=="D":
            udpos-=1
            if udpos<dmax:
                dmax=udpos
        elif i=="L":
            lrpos-=1
            if lrpos<lmax:
                lmax=lrpos
        elif i=="R":
            lrpos+=1
            if lrpos>rmax:
                rmax=lrpos
        if umax-dmax+1>arr[0]:
            if i=="D":
                dmax+=1
            break
        elif rmax-lmax+1>arr[1]:
            if i=="L":
                lmax+=1
            break
        print(i,umax,dmax,lmax,rmax,udpos,lrpos)
    print(-dmax+1,-lmax+1)
