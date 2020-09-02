def greet():
    print('hello world')

greet()
greet()


#############################
#pass parameter into function
def hey(name,age):
    print(f'hey my name is {name}, I am {age} years old')

name=input('enter your name:')
age=input('current age:')
hey(name,age)


##################
#default parameter
def hey1(name='cyla',age='20'):
    print(f'hey my name is {name}, I am {age} years old')

#hey1()
hey1(name='alisa') #alisa will replace cyla


#########################################
#pass function into function as parameter
def area(radius):
    return 3.142*radius*radius #return to area result

def vol(area,length):
    print(area*length)

radius=int(input('enter a radius:'))
length=int(input('enter a length:'))

vol(area(radius),length)

