def solve(ar):
    min_append = 0
    for i in range(0,len(ar)-1):
        if (len(ar[i]) == len(ar[i+1]) and ar[i]>=ar[i+1]):
            min_append+=1
            ar[i+1] = ar[i+1]+'0'
        if (len(ar[i])>len(ar[i+1])):
            temp = ar[i+1]+"0"*(len(ar[i])-len(ar[i+1]))
            T = len(ar[i])-len(ar[i+1])
            D = int(ar[i])-int(temp)
            if (D<0):
                ar[i+1] = temp
                min_append+=T
                continue
            elif (len(str(D+1))<=T):
                temp = str(int(temp)+(D+1))
            else:
                temp = temp+"0"
                T+=1
            ar[i+1] = temp
            min_append+=T
    return min_append,ar
t = int(input())
for i in range(t):
    l = int(input())
    ar = input().split()
    res = solve(ar)
    print("Case #"+str(i+1)+": "+str(res))
