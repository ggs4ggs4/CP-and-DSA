t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr2=[]
    for i in range(n):
        if arr[i]%(i+2)!=0:
            arr2.append(i)
    l=len(arr2)
    while(arr!=[] and arr2!=[]):
        del(arr[arr2[-1]])
        temp=arr2.pop()
        l-=1
        n-=1
        for i in range(temp,n):
            if arr[i]%(i+2)!=0:
                arr2.append(i)           
    if arr == []:
        print("YES")
    else:
        print("NO")
