def  INROW (grid , n , row):
    cross   =  0
    if  'O' in grid [row]:
        return [-1 , False]
    else :
        cross_count  =  grid[row].count('.')
        posit  =  []
        if cross_count == 1:
            posit  =  [ row , grid [row].index('.') ]
        return [ cross_count , posit]

def INCOL(grid,n,column):
    cross = 0
    column_list = []
    for i in range(n):
        column_list.append(grid[i][column])
    if 'O' in column_list:
        return [-1,False]
    else:
        cross_count = column_list.count('.')
        posit = []
        if cross_count == 1:
            posit = [column_list.index('.'),column]
        return  [ cross_count , posit]

def solve (grid , n):
    min_cross  =  100000
    dic  =  {}
    l  =  []
    for  row  in  range (n):
        res , posit =  INROW (grid,n,row)
        if  res != -1 and res <= min_cross:
            min_cross = res
            if posit:
                if posit not in l:
                    if res not in dic:
                        dic [res] = 1
                    else:
                        dic [res]+=1
                    l.append (posit)
            else:
                if res  not  in  dic:
                    dic[res] = 1
                else:
                    dic[res]+=1

    for column in range(n):
        res,posit =   INCOL(grid,n,column)
        if res!=-1 and res<=min_cross:
            min_cross = res
            if posit:
                if posit not in l:
                    if res not in dic:
                        dic[res] = 1
                    else:
                        dic[res]+=1
                    l.append(posit)
            else:
                if res not in dic:
                    dic[res] = 1
                else:
                    dic[res]+=1
    if min_cross == 100000:
        return -1
    else:
        return (min_cross,dic[min_cross])


def main():
    read=open("xs_and_os_input.txt","r")
    output = open("output.txt","w")
    t = int(read.readline())
    for i in range(t):
        n = int(read.readline())
        grid = []
        for j in range(n):
            row = list(read.readline())
            grid.append(row)
        result = solve(grid,n)
        if result == -1:
            output.write(f"Case #{i+1}: Impossible\n")
        else:
            output.write(f"Case #{i+1}: {result[0]} {result[1]}\n")
main()
