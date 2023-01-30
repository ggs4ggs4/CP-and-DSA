t=int(input())
for asdfghjkl in range (t):
    r,c=map(int,input().split())
    painting=[]
    for i in range(r):
        painting.append(list(input()))
    if r>1 and c>1:
        print("Case #"+str(asdfghjkl+1)+": Possible")
        for i in range(r):
            print("^"*c)
    else:
        count=0
        for i in painting:
            count+=i.count("^")
        if count:
            print("Case #"+str(asdfghjkl+1)+": Impossible")
        else:
            print("Case #"+str(asdfghjkl+1)+": Possible")
            for i in range(r):
                print("."*c)
