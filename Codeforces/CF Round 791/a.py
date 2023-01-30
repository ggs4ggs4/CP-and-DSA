t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    if n%2 != 0:
        print(-1)
    else:
        a=n//4
        b=n//6
        if n%6==2 and n>=4:
            b+=1
        elif n%6==4:
            b+=1
        if b==0 and a==0:
            print(-1)
        else:
            print(b,a)
