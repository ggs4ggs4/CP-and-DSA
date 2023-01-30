t=int(input())
for i in range(t):
    n,p=map(int,input().split())
    costarr=[]
    for j in range(n):
        costarr.append(list(map(int,input().split())))
    ans=[[0]*p for x in range(n)]
    adder=0
    for x in range(n-1,-1,-1):
        if x==n-1:
            maxi=max(costarr[x])
            mini=min(costarr[x])
            adder+=maxi-mini
            for y in range(p):
                ans[n-1][y]=min(abs(min(costarr[n-1])-costarr[n-2][y]),abs(max(costarr[n-1])-costarr[n-2][y]))
        elif x==0:
            maxi=max(costarr[x])
            arr1=[]#top se dist
            for each in costarr[x]:
                arr1.append(maxi-each)
            for y in range(p):
                arr1[y]+=ans[x+1][y]#top se exit ka total cost
            top_se_best=min(arr1)
            top_se_best+=maxi
        else:
            maxi=max(costarr[x])
            mini=min(costarr[x])
            adder+=maxi-mini
            arr1=[]#top se dist
            arr2=[]#bottom se dist
            for each in costarr[x]:
                arr1.append(maxi-each)
                arr2.append(each-mini)
            for y in range(p):
                arr1[y]+=ans[x+1][y]#top se exit ka total cost
                arr2[y]+=ans[x+1][y]#bottom se exit ka total cost
            top_se_best=min(arr1)
            bottom_se_best=min(arr2)
            for y in range(p):
                ans[x][y]=min(abs(min(costarr[x])-costarr[x-1][y])+top_se_best,abs(max(costarr[x])-costarr[x-1][y])+bottom_se_best)
    print("Case #"+str(i+1)+": "+str(top_se_best+adder))
