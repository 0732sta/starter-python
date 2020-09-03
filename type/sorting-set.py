>>> nums=[1,4,2,7,3,8,3,4,8,1]
>>> sorted(nums)
[1, 1, 2, 3, 3, 4, 4, 7, 8, 8]
>>> set(nums)
{1, 2, 3, 4, 7, 8}
>>> names=['shaun','ryu','abe','Oran','bret','Ayi']
>>> sorted(names)
['Ayi', 'Oran', 'abe', 'bret', 'ryu', 'shaun']
>>> names=['shaun','ryu','abe','ryu','bret','Ayi','shaun']
>>> set(names)
{'Ayi', 'ryu', 'abe', 'shaun', 'bret'}
>>> ninjas={'ryu': 'black', 'yoshi':'red','crystal':'black'}
>>> ninjas.values()
dict_values(['black', 'red', 'black'])
>>> set(ninjas.values())
{'red', 'black'}
