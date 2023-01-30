t=int(input())

for asdfghjkl in range (t):
    n=int(input())
    arr=list(input().split())

    arr2=[]
    #each has building visits then building number then index it is to be place at
    for i in range(n):
        arr2.append([int(arr[i]),i+1,0])
    arr2.sort(reverse=True)
    pos=1
    done=0
    time=0
    for i in range(n):
        arr2[i]=arr2[i][0:2]+[pos]
        pos*=-1
        done+=1
        if pos>0:
            time+=2*pos*arr2[i][0]
        else:
            time-=2*pos*arr2[i][0]
        if done==2:
            done=0
            pos+=1
    ans=list(range(n+1))
    for i in range(n):
        ans[arr2[i][1]]=arr2[i][2]
        
    ans=' '.join(map(str,ans))
    
    print(time)
    print(ans.strip())
        
        
