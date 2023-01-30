import math 

def primeFactors(n): 
    l=[]  
    if n==1:
        l.append(1)
        return(l)
    while n % 2 == 0: 
        l.append(2), 
        n = n / 2

    for i in range(3,int(n+1),2): 
          
 
        while n % i== 0: 
            l.append(i) 
            n = n / i 

    if n > 2: 
        l.append(n) 
    
    
    return l
  
n = int(input())
x=primeFactors(n)
x=x+[0]
c=0
co=0
a=0
for i in x:
    if c==0:
        c=i
        co+=1
    else:
        if c==i:
            co+=1
        elif c!=i:
            a+=c*co
            c=i
            co=1
    
print(a)
