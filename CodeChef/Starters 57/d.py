import sys
inf = int(1e9)+7#10^9 +7
INT_MAX = sys.maxsize
input = sys.stdin.readline
t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(input().strip())
    arr.sort(reverse=True)
    fmin=INT_MAX
    fplu=INT_MAX
    for i in range(n):
        if arr[i]=='-' and fmin==INT_MAX:
            fmin=i
        elif arr[i]=='+' and fplu==INT_MAX:
            fplu=i
    if fmin==INT_MAX and fplu==INT_MAX:
        print(''.join(arr))
    else:
        bp=min(fmin,fplu)
        nums=arr[:bp]
        signs=arr[bp::]
        signs.sort()
        for i in range(bp-len(signs)):
            print(arr[i],end='')
        for i in range(len(signs)):
            
            print(signs[i],end='')
            print(arr[i+bp-len(signs)],end='')
        print()
        
    
