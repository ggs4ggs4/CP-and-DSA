import re

def matcher():
    x, y, string = input().split()
    match = re.compile(r"(\?)")
    string = re.sub(match, '', string)

    temp1=string.count("CJ")
    temp2=string.count("JC")

    return (temp1*int(x)+temp2*int(y))

t=int(input())
for i in range(t):
    print("Case #{}: {}".format(i+1,matcher()))
