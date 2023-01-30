import pdb

import sys
sys.setrecursionlimit(int(13000))
f1=open('second_second_friend_input.txt','r')
input = f1.readline
t=int(input())
painting={}
flag=[1]
print(sys. getrecursionlimit())
final=''
def isSafe(i,j,rm,cm):
    if i<0 or j<0 or i>=rm or j>=cm:
        return 0
    elif painting[i][j]=="#" or painting [i][j]=='-1':
        return 0
    return 1
def func(r,c,rm,cm,i):
    if i>2200:
        pdb.set_trace()
    #print(r,c)
    if painting[r][c]=='#' or painting[r][c]=='-1':
        return 0
    count=0
    safe=[]
    ans=isSafe(r+1,c,rm,cm)
    if ans:
        count+=1
        safe=[r+1,c]
    ans=isSafe(r-1,c,rm,cm)
    if ans:
        count+=1
        safe=[r-1,c]
    ans=isSafe(r,c+1,rm,cm)
    if ans:
        count+=1
        safe=[r,c+1]
    ans=isSafe(r,c-1,rm,cm)
    if ans:
        count+=1
        safe=[r,c-1]
    if count<=1 and painting[r][c]=='^':
        flag[0]=0
        #print("flagged")
        return
    if count==1:
        painting[r][c]='-1'
        #print("Safe",safe)
        func(safe[0],safe[1],rm,cm,i+1)

    elif count==0:
        painting[r][c]='-1'
for i in range(t):
    #print("Case #"+str(i+1),": ",end='')
    final+="Case #"+str(i+1)+": "
    r,c=map(int,input().split())
    #print(i)
    painting={}
    flag[0]=1
    for asdaw in range(r):
        painting[asdaw]=list(input())

    for row in range(r):
        for column in range(c):

            if flag:
                func(row,column,r,c,0)
            else:
                break
    #print (flag)
    if flag[0]==1:
        #print("Possible")
        final +="Possible\n"
        for row in range(r):
            ans=''
            for column in range(c):
                if painting[row][column]=='.' or painting[row][column]=='^':
                    #print('^',end='')
                    #f.write('^')
                    ans+='^'
                elif painting[row][column]=='-1':
                    #print(".",end='')
                    #f.write('.')
                    ans+='.'
                else:
                    #print("#",end='')
                    #f.write('#')
                    ans+='#'
            #print()
            final+=ans+'\n'
    else:
        #print("Impossible")
        final+="Impossible\n"
f=open('out.txt','w+')
f.write(final)
f.close()

