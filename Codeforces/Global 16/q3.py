t=int(input())
for i in range (t):
    l=int(input())
    s=input()
    s2=input()
    an=0
    j=0
    while(j<l):
        if(s[j]!=s2[j]):
            an+=2
            j+=1
        elif(s[j]=="0"):
            if(j+1==l):
                an+=1
                j+=1
            elif(s[j+1]=="0" and s2[j+1]=="0"):
                an+=1
                j+=1
            else:
                an+=2
                j+=2
        else:
            x=1
            while(j+x<l):
                if(s[j+x]=="1" and s2[j+x]=="1"):
                    x+=1
                    if j+x==l:
                        j+x
                        break
                else:
                    an+=2
                    j+=x+1
    print(an)
