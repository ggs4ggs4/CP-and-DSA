n=int(input())
if n<3:
	print(-1)
elif n==3:
	print(210)
else:
	a=['050','080','170','020','200','110']
	z=(n-3)%6-1
	ans="1"+"0"*(n-4)+a[z]
	print(ans)
