n=int(input())
seating=[]
sc=[]
for i in range(n):
    seating.append(input())
    sc.append(seating[i].count("_"))
genlen=len(seating[0])
arr=list(map(int,input().split(",")))
if len(arr)>=2:
    arr=arr[len(arr)//2::]+arr[:len(arr)//2:][::-1]

def sol(j):
    broke=0
    for i in range(n):
        if sc[i]>=arr[j]:
            sc[i]-=arr[j]
            broke=1
            seat=i
            break
    if broke:
        x=0
        while x<len(seating[seat]):
            if arr[j]==0:
                break
            if seating[seat][x]=="_":
                seating[seat]=seating[seat][:x:]+str(j+1)+seating[seat][x+1::]
                arr[j]-=1
            x+=1


for x in range(len(arr)):
    sol(x)
for i in range(n):
    if i==n-1:
        print(seating[i],end='')
    else:
        print(seating[i])
