import sys
sys.setrecursionlimit(10000000)
def solve(arr, a, b,n, min_weight=400):
    arr_internal = list(arr)

    if max(arr_internal) > min_weight:
        return False
    if len(arr) == 1:
        return arr[0]
    if n not in arr_internal: 
        if len(arr_internal)>2 and arr_internal[0]==arr_internal[1] and arr_internal[0]==arr_internal[2]:
            return False
        elif arr[0]>=n**3/2:
            return False
    
    a1, b1 = arr_internal[0]+a, arr_internal[0]+b
    side1, side2 = a1-b, b1-a

    arr_internal1 = arr_internal[1::]
    arr_internal2 = arr_internal[1::]

    if side1 in arr_internal:
        arr_internal1.remove(side1)
    if side2 in arr_internal:
        arr_internal2.remove(side2)

    arr_internal1.append(a1)
    arr_internal2.append(b1)
   
    print("arr_internal",arr_internal,min_weight)
    print("arr1",arr_internal1)
    print("arr2",arr_internal2)
    print("#######################")
    res1 = solve(tuple(arr_internal1),a,b,n,min_weight)
    if res1 and res1<min_weight:
        min_weight = res1
    res2 = solve(tuple(arr_internal2),a,b,n,min_weight)
    
    
    if res2 and res1<min_weight:
        min_weight = res2
    return min_weight

t = int(input())

for i in range(t):
    n, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    arr1 = []
    for j in range(1,len(arr)+1):
        arr1.extend([j]*arr[j-1])
    res = solve(tuple(arr1), a, b,n)
    print(f"Case #{i+1}: {res}")

