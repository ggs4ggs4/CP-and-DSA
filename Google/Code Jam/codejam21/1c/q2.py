def solve(year):
    ans=[]
    t=year
    if len(year)%2!=0 or len(year)==2:
        if int(year[0]) < int(year[1]):
            year = str(int(year[0])+1)+year[1::]
        for i in range(len(year)-1):
            year=year[0:i+1]+str(int(year[i])+1)+year[i+2::]
            print(year)
        ans.append(year)
    elif len(year)==6:
        if int(year[0:3]) < int(year[3::]):
            year = str(int(year[0:3])+1)+year[3::]
            year= year[0:3]+str(int(year[0:3])+1)
        else:
            year= year[0:3]+str(int(year[0:3])+1)
        ans.append(year)
        year=t
        if int(year[0]) < int(year[1]):
            year = str(int(year[0])+1)+year[1::]
        for i in range(len(year)-1):
            year=year[0:i+1]+str(int(year[i])+1)+year[i+2::]
        ans.append(year)
        year=t
        if int(year[0:2]) < int(year[2:4]):
            year = str(int(year[0:2])+1)+year[2::]
            year= year[0:2]+str(int(year[0:2])+1)+str(int(year[0:2])+2)
        else:
            year= year[0:2]+str(int(year[0:2])+1)+str(int(year[0:2])+2)
        ans.append(year)
    elif len(year)==4:
        if int(year[0]) < int(year[1]):
            year = str(int(year[0])+1)+year[1::]
        for i in range(len(year)-1):
            year=year[0:i+1]+str(int(year[i])+1)+year[i+2::]
        ans.append(year)
        year=t
    print(min(ans))
t=int(input())
for i in range(t):
    year =input()
    res = solve(year)
    print(f"Case #{i+1}: {res}")
