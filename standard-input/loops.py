asila=['calm','love','peace','wild']

#for myself in asila:
#   print(myself)

#for myself in asila[1:3]:
#    print(myself)

for myself in asila:
    if myself == 'love':
        print(f'{myself}-sick')
        break #break the loop and after list 'love not be print'
    else:
        print(myself)