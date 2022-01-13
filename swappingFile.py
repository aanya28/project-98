def swapFileData():
    file1Name = input("Type file 1 name ")
    file2Name = input("Type file 2 name ")

    with open(file1Name, 'r') as a:
        data_a = a.read()

    with open(file2Name, 'r') as b:
        data_b = b.read()
    
    
    with open(file1Name, 'w') as a:
         a.write(data_b)

    with open(file2Name, 'w') as b:
         b.write(data_a)
swapFileData()

