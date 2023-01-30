# cook your dish here
import sys
input = sys.stdin.readline
t=int(input())

for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(n):
        if arr[i]<0:
            count+=1
        elif arr[i]==0:
            count=-1
            break
    if count<=0:
        print(0)
    elif count%2==0:
        print(0)
    else:
        print(1)
