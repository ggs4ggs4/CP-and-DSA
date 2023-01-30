t=int(input())
for i in range(t):
    n=int(input())
    b=input()
    first=b.find("2")
    ans={}
    if b.count("2")==1 or b.count("2")==2:
        print("NO")
    else:
        print("YES")
        for i in range (n):
            if b[i]=="1":
                pass
            else:
                j=i+1
                while(j<n):
                    if b[j]=="2":
                        ans[(i,j)],ans[(j,i)]="+","-"
                        break
                    j+=1
                else:
                    ans[(i,first)],ans[(first,i)]="+","-"
        for i in range(n):
            for j in range(n):
                if i==j:
                    print("X",end='')
                elif (i,j) in ans:
                    print(ans[(i,j)],end='')
                else:
                    print("=",end='')
            print()
