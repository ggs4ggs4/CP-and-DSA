f1 = "txt.txt"
f2 = "ts2_output.txt"
a = open(f1,"r").readlines()
b = open(f2,"r").readlines()
for i in range(len(a)):
    if(a[i]!=b[i]):
        print(f"line number :{i}\nfile1: {a[i]}\nfile2: {b[i]}")
        print("##################################################")
