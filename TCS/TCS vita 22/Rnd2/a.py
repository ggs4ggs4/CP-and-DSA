import sys
def recur(node):
    if visited[node]:
        return -1
    elif node not in rgraph:
        return 1
    elif score[node]!=-1:
        return score[node]+1
    else:
        visited[node]=1

        for i in rgraph[node]:
            out=recur(i)
            if out==-1:
                score[node]=-1
                return -1
            if out>score[node]:
                score[node]=out
        visited[node]=0
        return score[node]+1
        
#=======================================
a=input().split("},")
graph={}
rgraph={}
visited={}
leaves=[]
score={}
m=0

for i in a:
    key,values=i.split(".{")
    key=key.strip()
    values=values.strip("}")
    values=values.strip()
    values=values.split(",")
    values=list(map(lambda x : x.strip(),values))
    score[key]=-1
    if values!=[""]:
        graph[key]=values
        for f in values:
            if f not in rgraph:
                rgraph[f]=[key]
            else:
                rgraph[f].append(key)
    else:
        graph[key]=[]
        leaves.append(key)
    visited[key]=0
for i in leaves:
    out=recur(i)
    if out==-1:
        m=-1
        sys.stdout.write("error")
        break
    if out>m:
        m=out
if m!=-1:
    print(m,end='')



