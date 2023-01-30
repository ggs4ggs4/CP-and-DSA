import sys
input = sys.stdin.readline
t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(input())
    suffixq=0
    suffixa=0
    for i in range (n):
        if arr[n-1-i]=='A':
            suffixa+=1
        else:
            suffixq+=1
        if suffixq>suffixa:
            print("No")
            break
    else:
        print("Yes")
