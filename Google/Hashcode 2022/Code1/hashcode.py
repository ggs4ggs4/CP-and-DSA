f = open('f_find_great_mentors.txt','r')
c,p=map(int,(f.readline().strip('\n')).split())
#==============================================================================================================
personmap={}#key=person name, value=all other details [[skill,lvl],]
skillmap={}#key=skill, value=person and their skill level 
busy={}#key=person name, value=[start,period,end]
for i in range(c):
    name,skillcount=(f.readline().strip('\n')).split()
    personmap[name]=[]
    busy[name]=[0,0,0]
    for j in range(int(skillcount)):
        skill,skilllvl=(f.readline().strip('\n')).split()
        skilllvl=int(skilllvl)
        personmap[name].append([skill,skilllvl])
        if skill not in skillmap:
            skillmap[skill]=[[skilllvl,name]]
        else:
            skillmap[skill].append([skilllvl,name])
#print(personmap)
#print(skillmap)
for i in skillmap:
    skillmap[i].sort()
#==============================================================================================================
projectmap={}#key=project name, value=all other details
bbforemap={}#key=bestbeforedate, value=project name
manpowermap={}#key=role_count, value=project name
levelmap={}#key=rolelvlsum, value=project name

for i in range(p):
    rolesum=0
    inp=(f.readline().strip('\n')).split()
    name=inp[0]
    period,scoreawarded,bbfore,role_count=map(int,inp[1::])
    projectmap[name]=[[period,scoreawarded,bbfore,role_count]]
    if role_count not in manpowermap:
        manpowermap[role_count]=[name]
    else:
        manpowermap[role_count].append(name)
    for j in range(role_count):
        role,rolelvl=(f.readline().strip('\n')).split()
        rolelvl=int(rolelvl)
        projectmap[name].append([role,rolelvl])
        rolesum+=rolelvl
    if bbfore not in bbforemap:
        bbforemap[bbfore]=[name]
    else:
        bbforemap[bbfore].append(name)
    levelmap[name]=rolesum

#print(projectmap)
#print(bbforemap)
#print(manpowermap)
#print(levelmap)
#==============================================================================================================
day=0
queue=[]
levelupqueue=[]
working_on={}
ans1=[]
ans2=[]
for i in sorted(bbforemap.keys()):
    queue=[]
    for j in bbforemap[i]:
        if projectmap[j][0][2]-projectmap[j][0][0]-day>0:
            queue.append([levelmap[j],projectmap[j][0][3],j])
    queue.sort()
    for item in queue:
        consider=item[2]
        temp=[]
        temp2=[]
        busymax=0
        skillarr={}
        for skill,skilllvl in projectmap[consider][1::]:
            for person in skillmap[skill]:
                if person[1] in temp2:
                    continue
                if person[0]>=skilllvl and (busy[person[1]][2]==0 or projectmap[consider][0][1]-(busy[person[1]][2]+projectmap[consider][0][0]-projectmap[consider][0][2])>0):
                    if person[0]==skilllvl:
                        skillarr[person[1]]=1
                    else:
                        skillarr[person[1]]=0
                    temp.append([person[1],skill])
                    temp2.append(person[1])

                    if busy[person[1]][2]+projectmap[consider][0][0]>busymax:
                        busymax=busy[person[1]][2]+projectmap[consider][0][0]
                    break
        if len(temp)==projectmap[consider][0][3]:
            ans1.append(consider)
            temp2=[]
            for person in temp:
                temp2.append(person[0])
                busy[person[0]]=[0,0,busymax]
                #in skillmap
                abcdefg=0
                for i in skillmap[person[1]]:
                    if i[1]==person[0]:
                        break
                    abcdefg+=1
                skillmap[person[1]][abcdefg][0]+=skillarr[person[0]]
                #in personmap
                abcdefg=0
                for i in personmap[person[0]]:
                    if i[0]==person[1]:
                        break
                    abcdefg+=1
                personmap[person[0]][abcdefg][1]+=skillarr[person[0]]
            ans2.append(temp2)
f.close()
f2=open('f_find_great_mentorsout.txt','w')
l=len(ans1)
f2.write(str(l)+'\n')
score=0
for i in range(l):
    f2.write(ans1[i]+'\n')
    score+=projectmap[ans1[i]][0][1]
    for j in range(len(ans2[i])):
        if j < len(ans2[i])-1:
            f2.write(ans2[i][j]+' ')
        else:
            f2.write(ans2[i][j]+'\n')
f2.close()
print(score)
