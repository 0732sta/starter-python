age=21
num=0

while num<age:
    if num==0:
        num+=1
        continue #continue loop but do not print 0
    if num%2 == 0:
        print(num)
    if num>10:
        break    
    num+=1
