import sys
input = sys.stdin.readline
t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    sums=0
    prefix=[]
    tillend=[]
    for i in range(n):
        if i%2==0:
            sums+=arr[i]
        else:
            sums-=arr[i]
        prefix.append(sums)
    tillend.append(sums)
    
    for i in range(1,n):
        if i%2==0:
            tillend.append(sums-prefix[i-1])
        else:
            tillend.append(-sums+prefix[i-1])
    
    if sums%2==1:
        print(-1)
    else:
        if sums==0:
            print(1)
            print(1,n)
        else:
            cuts=[0]
            for i in range(n-2):
                #print(cuts)
                if i%2!=0:
                    new=sums
                else:
                    new=sums+2*tillend[i+1]
                if sums==0:
                    break
                elif abs(sums)>abs(new):
                    cuts.append(i)
                    sums=new
                elif i%2==1 and (arr[i]==1 and sums<0) or (arr[i]==-1 and sums>0):
                    if (i-1) != cuts[-1]:
                        cuts.append(i-1)
                    cust.append(i)
                    if sums>0:
                        sums-=2
                    else:
                        sums+=2
                if sums==0:
                    break
            else:
                print(-1)
                continue
            #print(cuts)
            print(len(cuts))
            print(1,cuts[1]+1)
            for i in range(1,len(cuts)-1):
                print(cuts[i]+2,cuts[i+1]+1)
            print(cuts[-1]+2,n)
