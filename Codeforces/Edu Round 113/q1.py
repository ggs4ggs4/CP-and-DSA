t=int(input())
for i in range(t):
    a=input()
    b=input()
    if "ab" in b:
        a=b.find("ab")
        print(a+1,a+2)
    elif "ba" in b:
        a=b.find("ba")
        print(a+1,a+2)
    else:
        print(-1,-1)
