alpha=input()
N=[int(a) for a in alpha]
N.reverse()
z=0
for a in range(len(N)):
    if N[a]==6:
        N[a]=5
        z=z+10**a
print(int(alpha)-z,z)
