import sys
input = sys.stdin.readline
read=open('txt.txt','r')
input = read.readline
out=open('out.txt','w')
print = out.write
t = int(input())
for case in  range(t):
    n,k=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    dict1={}
    dict2={}
    for i in range(n):
        dict1[arr1[i%n]]=arr1[(i+1)%n]
    for i in range(n):
        dict2[arr2[i%n]]=arr2[(i+1)%n]
    #print(dict1,dict2)
    if dict1!=dict2:
        print("Case #"+str(case+1)+": NO\n")
    elif k==0 and arr1!=arr2:
        print("Case #"+str(case+1)+": NO\n")
    elif k==1 and arr1==arr2:
        print("Case #"+str(case+1)+": NO\n")
    elif n==2 and arr1==arr2:
        if k%2==0:
            print("Case #"+str(case+1)+": YES\n")
        else:
            print("Case #"+str(case+1)+": NO\n")
    elif n==2 and arr1!=arr2:
        if k%2==0:
            print("Case #"+str(case+1)+": NO\n")
        else:
            print("Case #"+str(case+1)+": YES\n")
    else:
        print("Case #"+str(case+1)+": YES\n")
read.close()
out.close()
