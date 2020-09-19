ipsum_file = open('file/ipsum.txt')

#cycle file line by line 
#for method
for line in ipsum_file:
    #gap between line 'rstrip'
    print(line.rstrip())

#read line of file again and what character we seek to
ipsum_file.seek(1)


lines = ipsum_file.readlines()
print(lines)
#nothing else to read because we had print the ipsum file so the output is empty list at the last text

