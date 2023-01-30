t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=[]
    l,r,c=map(int,input().split())
    print(c)
    prev=c
    updated=0
    lm=[l,r,c]
    rm=[l,r,c]
    for i in range(n-1):
        l,r,c=map(int,input().split())
        if r>rm[1]:
            rm=[l,r,c]
            updated=1
        elif r==rm[1]:
            if c<rm[2]:
                rm=[l,r,c]
                updated=1
        if l<lm[0]:
            lm=[l,r,c]
            updated=1
        elif l==lm[0]:
            if c<lm[2]:
                lm=[l,r,c]
                updated=1

        if not updated:
            print(prev)
            continue

        if lm==rm:
            prev=lm[2]
        elif lm[0]==rm[0] or lm[1]==rm[1]:
            temp={0:lm , 1:rm}
            prev=temp[lm[1]-lm[0]<rm[1]-rm[0]][2]
        else:
            prev=lm[2]+rm[2]
        print(prev)
