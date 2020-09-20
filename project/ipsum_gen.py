from random import randint

stud_name = [
    'Layzin', 'Anis', 'Anisah', 'Afiq', 'Adam', 'Joseph', 'Irfan'
]

def studrize(word): #passing each word
    random_pos=randint(0,len(stud_name)-1)
    return f'{word}{stud_name[random_pos]}'

paraghraphs=int(input('How many paragraph of student ipsum:'))

with open('ipsum.txt') as ipsum_original:
    items=ipsum_original.read().split()

    for n in range(paraghraphs):
        stud_text=list(map(studrize,items))
        with open('stud_ipsum.txt','a') as ipsum_stud:
            ipsum_stud.write(' '.join(stud_text)+ '\n\n')