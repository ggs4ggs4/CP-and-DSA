from fractions import Fraction
t=int(input())
for asdfghjkl in range (t):
    a,b,c,d=map(int,input().split())

    if a%b!=0:
        a,b=map(int,str(Fraction(a,b)).split('/'))
    else:
        a,b=a//b,1
    if c%d!=0:
        c,d=map(int,str(Fraction(c,d)).split('/'))
    else:
        c,d=c//d,1
    print(a,b,c,d)
    if a==c and b==d:
        print(0)
    elif a==0 or c==0:
        print(1)
    elif b==d and (a%c==0 or b%c==0):
        print(1)
    elif a==c and (b%d==0 or d%b==0):
        print(1)
    else:
        print(2)
