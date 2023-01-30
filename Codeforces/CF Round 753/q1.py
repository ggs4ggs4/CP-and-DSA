t=int(input())
for asdfghjkl in range (t):
    board=input()
    s=input()
    dic={}
    key=1
    for i in board:
        dic[i]=key
        key+=1
    time=0
    l=len(s)
    if l>1:
        for i in range(l-1):
            td=dic[s[i]]-dic[s[i+1]]
            if td>0:
                time+=td
            else:
                time-=td
    print(time)
