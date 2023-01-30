t=int(input())

for inaj in range(t):
    n,c,q=map(int,input().split())
    s=input()
    cutmap={}
    for i in range(c):
        start,end=map(int,input().split())
        s+=s[start-1:end]
    for i in range(q):
        print(s[int(input())-1])
