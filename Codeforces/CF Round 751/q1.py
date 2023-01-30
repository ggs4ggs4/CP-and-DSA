t=int(input())
for asdfghjkl in range(t):
    s=input()
    m=s[0]
    ind=[]
    for i in range(len(s)):
        if s[i]==m:
            ind.append(i)
        elif s[i]<m:
            m=s[i]
            ind=[i]
        
    i=ind[0]
    if i==0:
        print(s[0],s[1::])
    elif i==len(s)-1:
        print(s[i],s[0:i])
    else:
        print(s[i],s[0:i]+s[i+1::])
