tc=int(input())
def funct(x,y=0):
    global N
    global M
    if y==N:
        print (x//2)
    else:
        x= x+M+x//3
        funct(x,y+1)
for a in range(tc):
        temp=[int(z) for z in input().split(' ')]
        M=temp[0]
        N=temp[1]-1
        funct(M)
