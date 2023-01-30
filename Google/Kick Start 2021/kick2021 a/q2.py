t=int(input())
for iasadsd in range(t):
    r,c=map(int,list(input().split()))
    m=[]
    for i in range(r):
        m.append(list(map(int,input().split())))
    for i in range (r):
        for j in range (c):
            if (m[i][j]==1):
                if flag==1:
                    l+=1
                else:
                    l=1
                    flag = 1
            else :
                flag=0
            if flag ==1 and l!=0 and (j=c-1 or m[i][j+1]==0):
                #end case
                #up case
                if(l%2==0):
                    if(m[i+1][j]==m[i-1][j]):
                        continue
                    else:
                        
                #start case
                #up case
                #down case
                else:
                    continue
            
