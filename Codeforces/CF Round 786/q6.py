n,m,q=map(int,input().split())
matrix=[]
tot_col=[0]*m
for i in range(n):
    matrix.append(list(input()))
for j in range(m):
    for i in range(n):
        if matrix[i][j]=="*":
            tot_col[j]+=1

for asdfgh in range(q):
    
    i,j=map(int,input().split())
    i-=1
    j-=1
    if matrix[i][j]=='*':
        matrix[i][j]='.'
        tot_col[j]-=1
    else:
        matrix[i][j]='*'
        tot_col[j]+=1
    tempcol=tot_col[:]
    i=0
    j=m-1
    cost=0
    while True:
        if i>=j:
            break
        if tempcol[i]==n:
            i+=1
            continue
        if tempcol[j]==0:
            j-=1
            continue
        
        if tempcol[i]!=n:
            required=n-tempcol[i]
            if required < tempcol[j]:
                tempcol[i]+=required
                tempcol[j]-=required
                cost+=required
            else:
                tempcol[i]+=tempcol[j]
                cost+=tempcol[j]
                tempcol[j]-=tempcol[j]
    
    diff = tot_col[i]-tempcol[j]
    if tempcol[j]==n:
        print(cost)
    #in column traversal
    elif diff>=0:
        I=0
        J=n-1
        upar_se=0
        while True:
            
            if upar_se==tempcol[j]:
                break
            elif matrix[I][j]=="*":
                I+=1
                upar_se+=1
                continue
            elif matrix[J][j]==".":
                J-=1
                continue
            else:
                upar_se+=1
                cost+=1
                I+=1
                J-=1
        print(cost)
    else:
        I=0
        J=n-1
        upar_se=0
        diff=-diff
        while True:
            
            if upar_se==tempcol[j]:
                break
            elif matrix[I][j]=="*":
                I+=1
                upar_se+=1
                continue
            elif matrix[I][j]=="." and diff>0:
                diff-=1
                I+=1
                upar_se+=1
            elif matrix[J][j]==".":
                J-=1
                continue
            else:
                upar_se+=1
                cost+=1
                I+=1
                J-=1
        print(cost)






















        
