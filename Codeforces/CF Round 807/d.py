t=int(input())
def find_next_seg(string,index,length):
    for i in range(index,length):
        if string[i]=='1':
            for j in range(i,length):
                if string[j]=='0':
                    return (i,j-1)
            return (i,length-1)
    return (-1,-1)
for inhgjdj in range(t):
    n=int(input())
    start=input()
    end=input()
    if start[0]!=end[0] or start[-1]!=end[-1]:
        print(-1)
    else:
        i=0
        j=0
        cost=0
        while True :
            a1=find_next_seg(start,i,n)
            a2=find_next_seg(end,j,n)
            #print(a1,a2)
            if a2[0] == -1 and a1[0] == -1:
                print(cost)
                break
            elif a2[0] == -1 or a1[0] == -1:
                print(-1)
                break
            elif a2[1]==n-1 and a1[1]!=n-1 or a1[1]==n-1 and a2[1]!=n-1:
                print(-1)
                break
            else:
                cost+=abs(a1[0]-a2[0])+abs(a1[1]-a2[1])
                i=a1[1]+1
                j=a2[1]+1
