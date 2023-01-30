t=int(input())
for asdfghjkl in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    if arr==arr[::-1]:
        print("YES")
    else:
        start=0
        end=n-1
        while start<end:
            if arr[start]==arr[end]:
                start+=1
                end-=1
            else:
                val1=arr[start]
                val2=arr[end]
                break
        flag=0
        start=0
        end=n-1
        while start<end:
            if arr[start]==arr[end]:
                start+=1
                end-=1
            else:
                if arr[start]==val1 or arr[end]==val1:
                    if arr[start]==val1:
                        start+=1

                    else:
                        end-=1
                else:
                    flag=1
                    break
        if flag==0:
            print("YES")
        else:
            flag=0
            start=0
            end=n-1
            while start<end:
                if arr[start]==arr[end]:
                    start+=1
                    end-=1
                else:
                    if arr[start]==val2 or arr[end]==val2:
                        if arr[start]==val2:
                            start+=1

                        else:
                            end-=1
                    else:
                        flag=1
                        break
            if flag==0:
                print("YES")
            else:
                print("NO")
