t=int(input())
for i in range (t):
    a=input()
    if len(a)%2==1:
        print("no")
    else:
        if a.count("B")==a.count("A")+a.count("C"):
            print("yes")
        else:
            print("no")
