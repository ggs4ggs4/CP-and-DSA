t=int(input())
for asdfghjkl in range (t):

    arr=list(input())
    n=len(arr)
    last1=-1
    last0=-1
    first0=-1
    ones_after=0
    lastzerobeforeone=-1
    update=1
    for i in range(n):
        if arr[i]=='1':
            last1=i
        if arr[i]=='0':
            last0=i    
        if first0==-1 and arr[i]=='0':
            first0=i
        if first0!=-1 and arr[i]=='1':
            ones_after+=1
        if first0!=-1 and update and arr[i]=='0':
            lastzerobeforeone=i
        if lastzerobeforeone!=-1 and arr[i]=='1':
            update = 0                                 
    if last1!=-1  and  first0!=-1:
        if last1<=first0:
            print(first0-last1+1)
        else:
            print(1)
    elif first0!=-1:
        print(first0+1)
    elif last1!=-1:
        print(n-last1)
    else:
        print(n)
