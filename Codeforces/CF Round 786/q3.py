t=int(input())
for asdfghjkl in range (t):
    t=input()
    replace=input()
    a=replace.count('a')
    
    if replace=='a':
        print(1)
    elif a==0:
        print(2**len(t))
    else:
        print(-1)
