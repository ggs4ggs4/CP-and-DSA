def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
def printAllDivisors(arr):
    N=len(arr)
    g = arr[0]
    divisors = dict()
    for i in range(1, N):
        g = gcd(arr[i], g)
    for i in range(1, g + 1):
        if i*i > g:
            break
        if (g % i == 0):
            divisors[i] = 1
            if (g // i != i):
                divisors[g // i] = 1
    ans=''
    for it in sorted(divisors):
        ans+=str(it)+" "
    ans.strip()    
    print(ans)
def b(a):
    y=str(bin(int(a)))[2::]
    l=len(y)
    return '0'*(30-l)+y
t=int(input())
for iasdfc in range(t):
    n=int(input())
    ar=list(map(b,input().split()))
    ar2=[]
    for ind in range(30):
        count=0
        for bind in ar:
            if bind[ind]=='1':
                count+=1
        if count:
            ar2.append(count)
    if ar2==[]:
        print(" ".join(map(str,range(1,n+1))))
    else:
        printAllDivisors(ar2)
