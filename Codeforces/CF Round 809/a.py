t=int(input())
for asajsdk in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    ans=["B"]*m
    for i in arr:
        if i-1<m-i:
            if ans[i-1]=="B":
                ans[i-1]="A"
            else:
                ans[m-i]="A"
        else:
            if ans[m-i]=="B":
                ans[m-i]="A"
            else:
                ans[i-1]="A"
    print("".join(ans))
