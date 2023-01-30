t=int(input())

for asdfghjkl in range (t):
    n=int(input())
    arr=list(input())
    count=arr.count('0')
    count2=arr.count('1')
    if count==1 and count2==1 and arr[-1]=='0':
        print(''.join(arr))
    else:
        for i in range(count):
            print('0',end='')
        for i in range(count2):
            print('1',end='')
        print()
