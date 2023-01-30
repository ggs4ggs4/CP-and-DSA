T=int(input())
for i in range(T):
    x=[int(j) for j in input().split()]
    l=x[0]
    y=[int(j) for j in input().split()]
    y.sort(reverse=True)
    print(y[l-1])
        
