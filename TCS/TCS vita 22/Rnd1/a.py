def recur(arr,sums,num,r):

    if num==2:

        ind=0
        for i in arr:
            if r<=i:
                anstup=([ind,],r)
                break
            else:
                r-=i
            ind+=1
        return anstup
    else:
        temparr=[]
        sums2=0
        for i in arr:
            sums-=i
            sums2+=sums
            if sums==0:
                break
            
            temparr.append(sums)
        
        ansarr,r=recur(temparr,sums2,num-1,r)
        for i in range(ansarr[-1]+1,len(arr)):
            if arr[i]>=r:
                ansarr.append(i)
                break
            else:
                r-=arr[i]

        return ansarr,r
#===================================================    
n=int(input())
r=int(input())
s=input().split(',')
ncr=1
sums=0
arr=[]
for i in range(n):
    sums+=int(ncr)
    arr.append(sums)
    ncr=(ncr*(n-i))/(i+1)
arr.append(arr[-1]+1)

number_of_str=0
while(r>arr[number_of_str]):
    number_of_str+=1
#===================================================
if r==1:
    print("",end="")
elif number_of_str==1:
    print(s[r-2],end="")
else:
    

    ansarr,r=recur(list(range(n-1,0,-1)),int(n*(n-1)/2),number_of_str,r-arr[number_of_str-1])
    ansarr.append(ansarr[-1]+r)
    ans=[]
    for i in ansarr:
        ans.append(s[i])
    print(",".join(ans),end="")
