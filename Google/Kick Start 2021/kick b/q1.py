def solve(s,l):
    a=[]
    i=l-1
    j=l-1
    while(j!=0):
        if (s[i-1]<s[i] and i!=0):
            i-=1
        elif (i!=j):
            a.append(j-i+1)
            j-=1
        else:
            a.append(j-i+1)
            i-=1
            j-=1
    return map(str,a[::-1])

a=open("txt.txt","w")
t=int(input())
for i in range (t):
    l=int(input())
    s=list(input())
    q=solve(s,l)
    a.write(("Case #"+str(i+1)+": 1"+" " +" ".join(q)).strip())
    a.write("\n")
a.close()
