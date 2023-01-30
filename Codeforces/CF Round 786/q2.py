t=int(input())
for asdfghjkl in range (t):
    word=input()
    a=ord(word[0])-97
    a*=25
    if word[1]<word[0]:
        a+=ord(word[1])-96
    else:
        a+=ord(word[1])-97

    print(a)
