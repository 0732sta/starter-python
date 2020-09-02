def ninja_intro(dictionary):

    for name,belt in dictionary.items():
        print(f'I am {name} and I am a {belt} belt')

ninja_belts={}

while True:
    ninja_name=input('enter ninja name:')
    ninja_belt=input('enter belt colour:')
    ninja_belts[ninja_name]=ninja_belt

    another=input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)