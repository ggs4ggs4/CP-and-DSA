def sol():
    lenth = int(input())
    l = list(map(int, input().split()))
    t = 0
    for k in range(1,lenth):
        j = l.index(k) + 1
        l = l[:k-1]+ list(reversed(l[(k-1):(j)])) + l[j:]
        
        t = t + j - k + 1
    return t

x=int(input())
for k in range(x):
    print(f"Case #{k+1}: {sol()}")
