from math import pow
t=int(input())
for asdfghjkl in range (t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    suum=0
    for i in range(n-1):
        temp=pow(10,a[i+1]-a[i])
        temp=int(temp)
        suum=int(suum)
        if int(k-ans)<temp:
            suum+=int(k-ans)*int(pow(10,a[i]))
            ans=int(k)
            break
        else:
            if i==0:
                suum+=int(temp-2)*int(pow(10,a[i]))
                ans+=int(temp-2)
            else:
                suum+=int(temp-1)*int(pow(10,a[i]))
                ans+=int(temp-1)
    suum=int(suum)
    if k>ans:
        s=int((k-ans)*int(pow(10,a[-1])))
        suum+=s
    print(suum+1)
