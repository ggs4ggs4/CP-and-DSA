import sys
input = sys.stdin.readline
t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    j=n//2+1
    l=[]
    for i in range (n//2):
        l.append(i+j)
        l.append(i+1)
    if n%2==1:
        l.append(n)
    
    print(" ".join(list(map(str,l))))
