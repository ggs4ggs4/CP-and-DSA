lst=[]
for i in range(10):
    m=input()
    lst.append(m)
    if "R" in m:
        r=[i,m.index("R")]
    if "B" in m:
        b=[i,m.index("B")]
    if "L" in m:
        l=[i,m.index("L")]
c=len(r)
if (r[0]==b[0] and r[0]==l[0]):
    if r[1]>b[1] and r[1]<l[1] or r[1]<b[1] and r[1]>l[1]:
        print(int(((b[0]-l[0])**2)**(1/2)+((b[1]-l[1])**2)**(1/2)-1)+2)
    else:
        print(int(((b[0]-l[0])**2)**(1/2)+((b[1]-l[1])**2)**(1/2)-1))

elif(r[1]==b[1] and r[1]==l[1]):
    if r[0]>b[0] and r[0]<l[0] or r[0]<b[0] and r[0]>l[0]:
        
        print(int(((b[0]-l[0])**2)**(1/2)+((b[1]-l[1])**2)**(1/2)-1)+2)
    else:
        print(int(((b[0]-l[0])**2)**(1/2)+((b[1]-l[1])**2)**(1/2)-1))
else:
    print(int(((b[0]-l[0])**2)**(1/2)+((b[1]-l[1])**2)**(1/2)-1))
            
        
