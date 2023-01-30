t=int(input())
for asdfghjkl in range (t):
    a=input()
    l=len(a)
    ab=a.count("ab")
    ba=a.count("ba")
    do=0
    if ab>ba:
        do=1
    elif ab<ba:
        do=2
    if do==0:
        print(a)
    elif l==2:
        print('aa')
    elif do==1:
        if a[0]=='a' and a[1]=='a':
            a='b'+a[1::]
        elif a[-1]=='b' and a[-2]=='b':
            a=a[:-1]+'a'
        else:
            a=a[:-1]+'a'
        print(a)
    else:
        if a[0]=='b' and a[1]=='b':
            a='a'+a[1::]
        elif a[-1]=='a' and a[-2]=='a':
            a=a[:-1]+'b'
        else:
            a=a[:-1]+'b'
        print(a)
