#open the file
ipsum_file = open('file/ipsum.txt')

#100 character from 50 character int
ipsum_file.seek(50)
#read and store in file_text
file_text=ipsum_file.read(100)
print (file_text)

#close the file
ipsum_file.close()