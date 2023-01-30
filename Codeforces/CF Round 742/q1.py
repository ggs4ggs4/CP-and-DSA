a={"L":"L","R":"R","D":"U","U":"D"}
t=int(input())
for i in range(t):
    an=input()
    ba=input()
    b=[]
    for i in ba:
        b.append(a[i])
    print("".join(b))
    
