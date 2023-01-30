x=[int(i) for i in input().split()]
a=x[0]
b=x[1]

count=0
for i in range(min(a,b)):
    count+=(a-i)*(b-i)
    
print(count)
