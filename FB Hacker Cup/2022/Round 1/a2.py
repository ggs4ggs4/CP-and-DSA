import sys
input = sys.stdin.readline
read=open('txt.txt','r')
input = read.readline
#out=open('out.txt','w')
#print = out.write
t = int(input())
for case in  range(t):
    n,k=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    isEqual=0
    if arr1==arr2:
        isEqual=1
    dict1={}
    dict2={}
   
    for i in range(n):
        if arr2[i] not in dict2:
            dict2[arr2[i]]=[i]
        else:
            dict2[arr2[i]].append(i)
    start=-1
    starts=[]
    for i in dict2[arr1[0]]:
        for j in range(n):
            if arr1[j]!=arr2[(j+i)%n]:
                break
        else:
            start = 1
            starts.append(i)
    if start == -1:
        print("Case #"+str(case+1)+": NO\n")
    else:
        for eachstart in starts:
            print(case)
            if n>2 and k>1:
                print("Case #"+str(case+1)+": YES\n")
                break
            elif n>2 and k==1:
                if eachstart!=0:
                    print("Case #"+str(case+1)+": YES\n")
                    break
            elif n==2 and len(starts)==2:
                print("Case #"+str(case+1)+": YES\n")
                break
            elif n==2 and eachstart ==0 and k%2==0:
                print("Case #"+str(case+1)+": YES\n")
                break
            elif n==2 and eachstart ==1 and k%2==1:
                print("Case #"+str(case+1)+": YES\n")
                break
            else:
                print("Case #"+str(case+1)+": NO\n")
                break
        else:
            print("Case #"+str(case+1)+": NO\n")
            
    
read.close()
#out.close()

