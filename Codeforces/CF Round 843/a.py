import sys
input = sys.stdin.readline
t=int(input())
for asdfghjkl in range (t):
    x=input()
    arr=list(x)
    a=x.count('a')
    b=x.count('b')
    if a==0 or b==0:
        l=len(arr)
        print(x[:l//3],x[l//3],x[l//3+1::])
    else:
        if arr[0]=='a':
            for i in range(len(arr)
