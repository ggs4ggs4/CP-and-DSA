f2=open("tes.txt","r")
i=int(f2.readline())
f=open("test.txt","w")
for i in range(i):
    a=f2.readline().strip("\n")
    b={}
    for ch in a:
        if ch in b:
            b[ch]+=1
        else:
            b[ch]=1
    vow=['U','O','I','E','A']
    vc=0
    cc=0
    vm=0
    cm=0
    for c in b.keys():
        if c in vow:
            vc+=b[c]
            if b[c]>vm:
                vm=b[c]
        else:
            cc+=b[c]
            if b[c]>cm:
                cm=b[c]
    c1=(vc-vm)*2+cc
    c2=(cc-cm)*2+vc
    f.write("Case #"+str(i+1)+": ")
    if c1>=c2:
        f.write(str(c2)+"\n")
    else:
        f.write(str(c1)+"\n")
f.close()
