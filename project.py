def swapfiledata():
    file1=input("enter first file name")
    file2 = input("enter othe file name")
    with open(file1)as a:
        data_a=a.read()
    with open(file2)as b:
        data_b=b.read()
    with open(file1,"w")as a:
        a.write (data_b)
    with open(file2,"w")as b:
        b.write (data_a)
swapfiledata()