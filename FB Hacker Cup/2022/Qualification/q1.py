t=int(input())
for asdfghjkl in range (t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    freq={}
    flag=0
    for i in arr:
        if i in freq:
            freq[i]+=1
            if freq[i]==3:
                print("Case #"+str(asdfghjkl+1)+": NO")
                flag=1
                break
        else:
            freq[i]=1
    if flag==1:
        continue
    elif n>2*k:
        
        print("Case #"+str(asdfghjkl+1)+": NO")
    else:
        print("Case #"+str(asdfghjkl+1)+": YES")
