t=int(input())
for i in range (t):
    s=input()
    l=len(s)
    j=0
    d={"0":1,"1":0}
    an=[]
    x=0
    while(j<l):        
        x=0
        an.append(d[s[j]])
        while(s[j]==s[j+x]):
            x+=1
            if x+j==l:
                break
        
        else:
            j+=x
            continue
        j+=x
    s=sum(an)
    if (s<2):
        print(s)
    else:
        print(2)
    
        
