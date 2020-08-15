>>> str="hello billie ellish"
>>> str.split(' ')
['hello', 'billie', 'ellish']
>>> fib1=[1,1,2,3,5,8,13]
>>> fib1
[1, 1, 2, 3, 5, 8, 13]
>>> fib1[2]
2
>>> fib1[-2]
8
>>> fib2=[23,30,31]
>>> fib1+fib2
[1, 1, 2, 3, 5, 8, 13, 23, 30, 31]
>>> fib1[0]=4
>>> fib1
[4, 1, 2, 3, 5, 8, 13]
>>> all=fib1+fib2
>>> all
[4, 1, 2, 3, 5, 8, 13, 23, 30, 31]
>>> all.append(89) #add new number at the back
>>> all
[4, 1, 2, 3, 5, 8, 13, 23, 30, 31, 89]
>>> all.pop()
89
>>> all
[4, 1, 2, 3, 5, 8, 13, 23, 30, 31]
>>> all.append(89)
>>> all.remove(31)
>>> all
[4, 1, 2, 3, 5, 8, 13, 23, 30, 89]
>>> del(all[9])
>>> all
[4, 1, 2, 3, 5, 8, 13, 23, 30]
>>> fwen=['layla','anis','anisah']
>>> fwen.pop()
'anisah'
>>> fwen
['layla', 'anis']
>>> fwen.append(3)
>>> fwen
['layla', 'anis', 3]
>>> nums=[fwen,fib1,[10,20,30]]
>>> nums
[['layla', 'anis', 3], [4, 1, 2, 3, 5, 8, 13], [10, 20, 30]]
>>> nums[0]
['layla', 'anis', 3]
>>> nums[0][1]
'anis'
