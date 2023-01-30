t=int(input())
def factorial( n) :
    M = 1000000007
    f = 1
 
    for i in range(3, n + 1):
        f = (f * i) % M 
    return f
for i in range (t):
    a=int(input())
    a*=2
    print(factorial(a))
