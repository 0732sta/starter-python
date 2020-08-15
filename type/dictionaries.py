>>> ninja_belts={"crystal":"red","ryu":"black"} #create dic use curly bracket
>>> ninja_belts
{'crystal': 'red', 'ryu': 'black'}
>>> ninja_belts['crystal']
'red'
>>> 'asila' in ninja_belts
False
>>> 'ryu' in ninja_belts
True
>>> ninja_belts.keys()
dict_keys(['crystal', 'ryu'])
>>> list(ninja_belts.keys())
['crystal', 'ryu']
>>> ninja_belts.values()
dict_values(['red', 'black'])
>>> vals=list(ninja_belts.values())
>>> vals
['red', 'black']
>>> vals.count()  #cannot be count for each vals
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: count() takes exactly one argument (0 given)
>>> vals.count('red')
1
>>> vals.count('black')
1
>>> vals.count('pink')
0
>>> ninja_belts['asila']='white'
>>> ninja_belts
{'crystal': 'red', 'ryu': 'black', 'asila': 'white'}
>>> person=dict(name='jim',age=55,height=160) #create dic use bracket
>>> person
{'name': 'jim', 'age': 55, 'height': 160}
>>> mum=person
>>> mum
{'name': 'jim', 'age': 55, 'height': 160}
