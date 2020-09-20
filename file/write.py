
with open('file/write.txt','w')as write_file:
    write_file.write('the quick brown fox jumps over the lazy dog')
    #write_file.write('\nthen the black cat follow the brown fox ')

with open('file/write.txt','w')as write_file:
    write_file.write('\nthen the black cat follow the brown fox ')

#the output is only the 2nd line, not 1st and 2nd because overwrite
#instead of passing 'w' as primitive use another word or char
with open('file/write.txt','a')as write_file:
    write_file.write('\nthen the black cat follow the brown fox ')

sentence = {
'\nthe quick brown fox jumps over the lazy dog'
'\nthen the black cat follow the brown fox'
}

with open('file/write.txt','a')as write_file:
    write_file.writelines(sentence)